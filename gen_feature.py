import pandas as pd
import os

raw_data_path = '/Users/pei/pydir/health_care/raw_data/Charles2018/'
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
    if wear_glass_state[index] == '3 No' and eyesight_at_distance[index] <= 2 and eyesight_up_close[index] <= 2:
        vision_state.append('3')
    elif (wear_glass_state[index] == '1 Yes' or wear_glass_state[index] == '4 Sometimes') and \
            (eyesight_at_distance[index] == 3 or eyesight_at_distance[index]) == 4 and \
            (eyesight_up_close[index] == 3 or eyesight_up_close[index] == 4):
        vision_state.append('2')
    elif wear_glass_state[index] == '2 Legally Blind' and eyesight_at_distance[index] == 5 and eyesight_up_close[index] == 5:
        vision_state.append('1')
    else:
        vision_state.append('997')
print(vision_state)