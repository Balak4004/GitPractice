import pandas as pd
import pytest

def get_defferences1(df_emptgt1, df_empsrc1, file_path):
    concat_df1 = pd.concat([df_emptgt1, df_empsrc1])
    diff_df1 = concat_df1.drop_duplicates(keep=False)


    if not (diff_df1).empty:
        diff_df1.to_csv(file_path,index=False)
    return diff_df1


# Test Case Data comparison
def test_EmpDataValdation():
    df_empsrc1 = pd.read_csv('H:\pythonprojects\myProj\Data1\empsrc1.csv')
    df_emptgt1 = pd.read_csv('H:\pythonprojects\myProj\Data1\emptgt1.csv')
    differences1_df = get_defferences1(df_emptgt1, df_empsrc1, 'H:\pythonprojects\myProj\TestResult_Output\diff_empcsv1.csv')
    if not differences1_df.empty:
        print(f"there is difference in empsrc and emptgt and saved to 'diff_empcsv1.csv'")



    assert df_empsrc1.equals(df_emptgt1), "Source and target not matching"