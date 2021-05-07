import pandas as pd
import numpy as np
from scipy import stats

import vision_impairment as vi

raw_data_path = 'D:/pydir/health_care/raw_data/Charles2018/'

health_data = pd.read_csv(raw_data_path + 'Health_Status_and_Functioning.csv')
vi.merge_vision_q(health_data)