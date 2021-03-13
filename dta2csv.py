#原始数据是dta格式，需要用stata软件打开，因此转换成csv格式
import pandas as pd
import os


# from pyecharts import Geo, Map


def load_large_dta(fname):
    import sys

    reader = pd.read_stata(fname, iterator=True)
    df = pd.DataFrame()

    try:
        chunk = reader.get_chunk(100 * 1000)
        while len(chunk) > 0:
            df = df.append(chunk, ignore_index=True)
            chunk = reader.get_chunk(100 * 1000)
            print('.')
            sys.stdout.flush()
    except (StopIteration, KeyboardInterrupt):
        pass

    print('\nloaded {} rows'.format(len(df)))

    return df

raw_data_path = 'D:/pydir/health_care/raw_data/Charles2018/'

file_list = os.listdir(raw_data_path)
for single_file in file_list:
    if single_file.split('.')[1] != 'dta':
        os.remove(raw_data_path+single_file)

file_list = os.listdir(raw_data_path)
for single_file in file_list:
    print(single_file)
    trans_data = load_large_dta(single_file)
    trans_data.to_csv('D:/pydir/health_care/raw_data/Charles2018/Demographic_Background.csv',index=False,encoding='utf_8_sig')