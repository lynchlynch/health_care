import numpy as np

transfer_mat = np.mat([[0.8218,0.1584,0.0198,0.0],
           [0.2581,0.6774,0.0387,0.0258],
           [0.0946,0.0541,0.6036,0.2477],
           [0.0526,0.0994,0.3392,0.5088]])
home_stuct_city = np.mat([0.1608,0.1512,0.4082,0.2797])
home_stuct_country = np.mat([0.1593,0.2492,0.3217,0.2697])
print(home_stuct_country)
print(home_stuct_country * np.mat([[1],[1],[1],[1]]))
for i in range(1,49):
    print('-----' + str(2012+i) + '----')
    result = home_stuct_country * transfer_mat ** i
    print(result)
    # print(result * np.mat([[1],[1],[1],[1]]))