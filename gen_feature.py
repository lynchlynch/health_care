import pandas as pd
import os
import numpy as np

# raw_data_path = '/Users/pei/pydir/health_care/raw_data/Charles2018/'
raw_data_path = 'D:/pydir/health_care/raw_data/Charles2018/'
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
#
cognition_data = pd.read_csv(raw_data_path + 'Cognition.csv')
# print(list(set(cognition_data['dc001_w4'].tolist())))
for index in range(len(cognition_data)):
    if pd.isnull(cognition_data['dc001_w4'].tolist()[index]):
        print(index)