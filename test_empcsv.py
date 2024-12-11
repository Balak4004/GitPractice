import pandas as pd
import pytest



def test_emp_data_check():
    df_source = pd.read_csv('Data1/empsrc.csv')
    df_target = pd.read_csv('Data1/emptgt.csv')


    assert df_source.equals(df_target), "source and target not matching"


'''
    if(df_source.equals(df_target)):
        print("matching")
    else:
        print("Not matching")
'''
