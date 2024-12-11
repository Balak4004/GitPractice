
#Testing the data extraction from source being CSV and compare with Expected output

import pandas as pd
import pytest

# actual data
@pytest.fixture()
def csv_file_path():
    return 'H:\pythonprojects\myProj\Data1\empsrc.csv'

#expected data
@pytest.fixture()
def expected_csv_data():
    return pd.DataFrame({'eno':[1,2,3],'ename':['a','b','c']})

def test_data_extraction(csv_file_path, expected_csv_data):
    data = pd.read_csv(csv_file_path)

    assert data.equals(expected_csv_data), "Data extraction failed"

