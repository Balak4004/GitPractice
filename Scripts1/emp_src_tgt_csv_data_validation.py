import pandas as pd
import pytest

def get_defferences(df_emptgt, df_empsrc, file_path):
    concat_df = pd.concat([df_emptgt, df_empsrc])
    diff_df = concat_df.drop_duplicates(keep=False)

    if not (diff_df).empty:
        diff_df.to_csv(file_path,index=False)
    return diff_df


# Test Case Data comparison
def test_EmpDataValdation():
    df_empsrc = pd.read_csv('H:\pythonprojects\myProj\Data1\empsrc.csv')
    df_emptgt = pd.read_csv('H:\pythonprojects\myProj\Data1\emptgt.csv')
    differences_df = get_defferences(df_emptgt, df_empsrc, 'H:\pythonprojects\myProj\TestResult_Output\diff_empcsv.csv')
    if not differences_df.empty:
        print(f"there is difference in empsrc and emptgt and saved to 'diff_empcsv.csv'")

    assert df_empsrc.equals(df_emptgt), "Source and target not matching"