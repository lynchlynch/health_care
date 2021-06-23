import pandas as pd
import os
import numpy as np

import trans_fuc as tf

raw_data_path = '/Users/pei/pydir/health_care/raw_data/Charles2018/'
# raw_data_path = 'D:/pydir/health_care/raw_data/Charles2018/'
health_function_data = pd.read_csv(raw_data_path + 'Health_Status_and_Functioning.csv')
# 视觉能力即是否有视力障碍。
# 问卷上有几个问题：“您通畅是否戴眼镜（包括矫正视力镜片）”（da032）、
# “您看远处的东西怎么样？比如能否隔着马路认出朋友（包括戴着眼镜）？（da033）”、
# “您是否看清楚近处的东西？”（da034），
# 通过这些设计问题的回答，把老年人的视觉能力分为三种，视力正常(3)，视力中度障碍(2)和失明(1)。

vision_state = []
wear_glass_state = health_function_data['da032'].tolist()
eyesight_at_distance = health_function_data['da033'].tolist()
eyesight_up_close = health_function_data['da034'].tolist()
for index in range(len(eyesight_at_distance)):
    if wear_glass_state[index] == '3 No' and \
            (eyesight_at_distance[index] == '1 Excellent' or eyesight_at_distance[index] == '2 Very Good') and \
            (eyesight_up_close[index] == '1 Excellent' or eyesight_up_close[index] == '2 Very Good'):
        vision_state.append('3')
    elif (wear_glass_state[index] == '1 Yes' or wear_glass_state[index] == '4 Sometimes') and \
            (eyesight_at_distance[index] == '3 Good' or eyesight_at_distance[index] == '4 Fair') and \
            (eyesight_up_close[index] == '3 Good' or eyesight_up_close[index] == '4 Fair'):
        vision_state.append('2')
    elif wear_glass_state[index] == '2 Legally Blind' and eyesight_at_distance[index] == '5 Poor' and \
            eyesight_up_close[index] == '5 Poor':
        vision_state.append('1')
    else:
        vision_state.append('997')

#认知能力涵盖面很广，包含老年人的定向力、记忆力、回忆力和计算力四个方面。问卷中通过12个问题的测评。
cognition_data = pd.read_csv(raw_data_path + 'Cognition.csv')
#这张表很多空值，因此选取非空的处理。我们只用到其中的某些行，所以首先把这些用到的这些列选出来，组成新表，然后删除空值
select_col_list = ['dc001_w4','dc002_w4','dc003_w4','dc005_w4','dc006_w4',
                   'dc007_w4','dc008_w4','dc009_w4','dc010_w4','dc012_w4',
                   'dc013_w4_1_s1','dc013_w4_1_s2','dc013_w4_1_s3','dc013_w4_1_s4',
                   'dc014_w4_1_1','dc014_w4_2_1','dc014_w4_3_1','dc014_w4_4_1','dc014_w4_5_1',
                   'dc013_w4_2_s1','dc013_w4_2_s2','dc013_w4_2_s3','dc013_w4_2_s4','dc016_w4','dc017_w4','dc018_w4',
                   'dc020_w4','dc021_w4','dc022_w4','dc019_w4','dc023_w4','dc024_w4',
                   'dc009','dc010','dc011','dc012','dc013','dc014','dc015','dc016','dc017','dc018']

select_df = cognition_data[select_col_list].copy(deep=True)
select_df = select_df.dropna(how='any')
select_df = select_df.reset_index(drop=True)
select_df.to_csv(raw_data_path + 'Cognition_brief.csv',index=False)
select_df = pd.read_csv(raw_data_path + 'Cognition_brief.csv')
total_score_list_mmse = []
for index in range(len(select_df)):
    q1_list = select_df.iloc[index][['dc001_w4','dc002_w4','dc003_w4','dc005_w4','dc006_w4']].tolist()
    q1_score = q1_list.count('1 Correct')
    q2_list = select_df.iloc[index][['dc007_w4','dc008_w4','dc009_w4','dc010_w4','dc012_w4']].tolist()
    q2_score = q2_list.count('1 Correct')
    q3_list = select_df.iloc[index][['dc013_w4_1_s1','dc013_w4_1_s2','dc013_w4_1_s3']].tolist()
    trans_q3_list = tf.trans_ans(q3_list)
    q3_score = len(trans_q3_list) - trans_q3_list.count(0)
    q4_list = select_df.iloc[index][['dc016_w4','dc017_w4','dc018_w4']].tolist()
    trans_q4_list = tf.trans_ans(q4_list)
    q4_score = trans_q4_list.count(1)
    q5_list = select_df.iloc[index][['dc014_w4_1_1','dc014_w4_2_1','dc014_w4_3_1','dc014_w4_4_1','dc014_w4_5_1']].tolist()
    q5_list = list(np.array(q5_list) - np.array([93,86,79,72,65]))
    q5_score = q5_list.count(0)
    q6_list = select_df.iloc[index][['dc013_w4_2_s1', 'dc013_w4_2_s2', 'dc013_w4_2_s3']].tolist()
    trans_q6_list = tf.trans_ans(q6_list)
    q6_score = len(trans_q6_list) - trans_q6_list.count(0)
    q7_list = select_df.iloc[index][['dc020_w4','dc021_w4','dc022_w4']].tolist()
    q7_score = q7_list.count('1 Correct')
    q8_list = select_df.iloc[index][['dc019_w4','dc023_w4', 'dc024_w4']].tolist()
    q8_score = q8_list.count('1 Correct')
    single_total_score = q1_score + q2_score + q3_score + q4_score + q5_score + q6_score + q7_score + q8_score
    total_score_list_mmse.append(single_total_score)

total_score_list_cesd = []
for index in range(len(select_df)):
    q_list = select_df.iloc[index][['dc009','dc010','dc011','dc012','dc013','dc014','dc015','dc016','dc017','dc018']].tolist()
    q_score = tf.trans_ans(q_list)
    # print(q_score)
    single_total_score = sum(q_score)
    # print(single_total_score)
    total_score_list_cesd.append(sum(q_score))

# print(total_score_list_cesd)
function_data = pd.read_csv(raw_data_path + 'Health_Status_and_Functioning.csv')
#日常生活生活活动能力是指具体包括基本日常生活活动能力和应用社会设施的生活活动能力，宏观来讲就是老年人独立应对日常生活活动的能力，
# 可以逐一使用IADLS量表及ADLS量表进行测量确定。CHARLS问卷考察老年人的基础日常生活自理水平，是通过老年人简单的人常生活行动，
# 即穿衣（db010）、吃饭（db012）、上下床（db013）、洗澡（db011）、自主控制大小便（db015）、上厕所（db014）
# 这六项日常基本生活行动是否独立完成来确定的，如果其中一项日常生活行动完成困难，就可确定为ADL障碍。
#这张表很多空值，因此选取非空的处理。我们只用到其中的某些行，所以首先把这些用到的这些列选出来，组成新表，然后删除空值
select_col_list = ['db010','db012','db013','db015','db011', 'db014']
select_df = function_data[select_col_list].copy(deep=True)
select_df = select_df.dropna(how='any')
select_df = select_df.reset_index(drop=True)
select_df.to_csv(raw_data_path + 'Health_Status_and_Functioning_brief.csv',index=False)
select_df = pd.read_csv(raw_data_path + 'Health_Status_and_Functioning_brief.csv')
total_score_list_adl = []
for index in range(len(select_df)):
    # print('-----------' + str(index) + '--------------')
    single_wearing = select_df.iloc[index]['db010']#.tolist()
    single_wearing_score = tf.wearing_score(single_wearing)

    single_hygiene = select_df.iloc[index]['db011']
    single_hygiene_score = tf.hygiene_score(single_hygiene)

    single_eating = select_df.iloc[index]['db012']
    single_eating_score = tf.wearing_score(single_eating)

    single_toilet = select_df.iloc[index]['db014']
    single_excrete = select_df.iloc[index]['db015']
    single_toex_score = tf.toex_score(single_toilet,single_excrete)

    single_moving = select_df.iloc[index]['db013']
    single_moving_score = tf.moving_score(single_moving)
