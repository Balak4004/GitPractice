import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import pytest

def get_difference(df_orcl,df_mysql,file_path):
    conncat_df = pd.concat([df_orcl,df_mysql])
    diffe_df = conncat_df.drop_duplicates(keep=False)
    if not (diffe_df).empty:
        diffe_df.to_csv(file_path,index=False)
        return diffe_df

@pytest.fixture()
def conn_orcle_src():
    orcle_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')
    conn_oracle = orcle_engine.connect()
    yield conn_oracle
    conn_oracle.close()

@pytest.fixture()
def conn_mysql_tgt():
    mysql_engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb')
    conn_mysql = mysql_engine.connect()
    yield conn_mysql
    conn_mysql.close()

def test_DataExtractOrcleMysql(conn_orcle_src, conn_mysql_tgt):
    query_orcl = """select * from city order by id"""
    df_orcl = pd.read_sql(query_orcl, conn_orcle_src)
    query_mysql = """select * from city order by id"""
    df_mysql = pd.read_sql(query_mysql, conn_mysql_tgt)
    db_difference_df = get_difference(df_orcl, df_mysql, 'H:\pythonprojects\myProj\TestResult_Output\diff_city.csv')
    if not db_difference_df.empty:
        print(f"Data mismatch found and saved to 'diff_city,csv'")
    assert df_mysql.equals(df_orcl), "oracle and mysql data not matching for city"






