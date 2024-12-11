import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle

@pytest.fixture()
def connect_to_oracle_SRC():
    engine = create_engine("oracle+cx_oracle://hr:hr@localhost:1521/xe")
    connection_oracle = engine.connect()
    yield connection_oracle
    connection_oracle.close()

def test_dataExtrcationFromOracleToLoadintoMYSQL(connect_to_oracle_SRC):
    query_orcl_src ="""select * from city"""
    df_orcl_src = pd.read_sql(query_orcl_src,connect_to_oracle_SRC)
    print("source data :",df_orcl_src)
