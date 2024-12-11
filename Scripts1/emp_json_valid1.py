import pandas as pd
import pytest

def get_differences(df_emptgt, df_empsrc, file_path):
    concat_df = pd.concat([df_emptgt, df_empsrc])
    diff_df = concat_df.drop_duplicates(keep=False)
    if not (diff_df).empty:
        diff_df.to_csv(file_path, index=False)
        return diff_df

@pytest.fixture()
def empsrc_json_file_path():
    return 'H:\pythonprojects\myProj\Data1\employees_source.json'

@pytest.fixture()
def emptgt_json_file_path():
    return 'H:\pythonprojects\myProj\Data1\employees_target.json'

def test_empjsondatavalid(empsrc_json_file_path, emptgt_json_file_path):
    df_empsrc = pd.read_json(empsrc_json_file_path)
    df_emptgt = pd.read_json(emptgt_json_file_path)
    difference2_df = get_differences(df_emptgt, df_empsrc,'H:\pythonprojects\myProj\TestResult_Output\diff_emp_json.csv')

    if difference2_df is None:
        print("check function implemenattion")
    elif difference2_df.empty:
        print(f"empsrc_json and emptgt_json data not matching and saved to 'diff_emp_json.csv'")
    else:
        print("emp src and tgt matching")
    assert df_empsrc.equals(df_emptgt), "emp src and tgt data not matching"
