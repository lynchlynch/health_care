import pandas as pd
import numpy as np
import os
import chardet

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


def deconde_str(string):
    """
    解码 dta文件防止 乱码
    """
    # re = string.encode('latin-1').decode('utf-8')
    print(string.dtypes)
    print('1')
    re = string.encode('gb18030').decode('utf-8')
    return re


# example
df_2002_path = 'D:/pydir/health_care/raw_data/Charles2018/Demographic_Background.dta'
df_2002 = load_large_dta(df_2002_path)
print(df_2002.dtypes)
df_2002.to_csv('D:/pydir/health_care/raw_data/Charles2018/Demographic_Background.csv',index=False,encoding="utf_8_sig")