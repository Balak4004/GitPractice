# Test Extraction from JSON and validate against target ( .csv file )
import pandas as pd
import pytest

def get_difference(dept_json, dept_csv,file_path):
    concat_df = pd.concat([dept_json, dept_csv])
    diff_json_csv_df = concat_df.drop_duplicates(keep=False)

    if not (diff_json_csv_df).empty:
        diff_json_csv_df.to_csv(file_path, index=False)
    return diff_json_csv_df

@pytest.fixture()
def json_file_path():
    return ('H:\pythonprojects\myProj\Data1\dept_src.json')

@pytest.fixture()
def csv_file_path():
    return ('H:\pythonprojects\myProj\Data1\dept_tgt.csv')


def test_dept_data_compare(json_file_path, csv_file_path):
    dept_json = pd.read_json(json_file_path)
    #print(dept_json.dtypes)
    #print(dept_json)
    dept_csv = pd.read_csv(csv_file_path)
    #print(dept_csv.dtypes)
    #print(dept_csv)
    diff_dept_df = get_difference(dept_json,dept_csv, 'H:\pythonprojects\myProj\TestResult_Output\diff_dept_csv')

    if not diff_dept_df.empty:
        print(f"dept json and csv not match and saved to 'diff_dept.csv'")

    assert dept_json.equals(dept_csv), "dept json and csv not matching"

