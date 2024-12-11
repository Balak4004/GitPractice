import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle

#Data Type check

@pytest.fixture()
def conn_orcl_src():
    engine = create_engine("oracle+cx_oracle://hr:hr@localhost:1521/xe")
    conn_orcl = engine.connect()
    yield conn_orcl
    conn_orcl.close()

'''
def test_DQ_DataType_Check(conn_orcl_src):
    query = 'select * from city'
    df_actual = pd.read_sql(query, conn_orcl_src)
    print("src data types : ", df_actual.dtypes)
    df_expected = {"id":"int64", "name":"object"}
    #print(df_expected)

    assert df_actual.dtypes.to_dict() == df_expected, "Data type mismatch"
    '''
# referential integrity check

@pytest.fixture()
def conn_mysql_tgt():
    engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb')
    conn_mysql = engine.connect()
    yield conn_mysql
    conn_mysql.close()

def test_DQ_ref_int_check(conn_orcl_src, conn_mysql_tgt):
    query_parent_table = 'select country_name from country'
    df_parent = pd.read_sql(query_parent_table,conn_mysql_tgt)
    #print(df_query_parent)
    query_child_table = 'select country from city'
    df_child = pd.read_sql(query_child_table, conn_mysql_tgt)
    #print(df_query_child)

    valid = df_child['country'].isin(df_parent['country_name'])
    #print(check1)
    invalid = ~valid
    invalid_df = df_child[invalid]
    # ~ this will convert true to false so we can have only invalid values
    print(invalid_df)
    #write invalid to csv
    invalid_df.to_csv('H:\pythonprojects\myProj\Oct24Batch_TestCases\TestResult_Output\invalid_country.csv', index=False)

    assert invalid_df.empty,"referential integrity violation"









