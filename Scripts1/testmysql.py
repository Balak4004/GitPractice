import pandas as pd
import pytest
from sqlalchemy import create_engine



@pytest.fixture()
def connect_to_mysql_TGT():
    engine = create_engine("mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb")
    connection_mysql = engine.connect()
    yield connection_mysql
    connection_mysql.close()


#@pytest.mark.smoke
def test_dataExtrcationFromOracleToLoadintoMYSQL(connect_to_mysql_TGT):
    query_mysql_tgt ="""select * from city order by id"""
    df_mysql_tgt = pd.read_sql(query_mysql_tgt, connect_to_mysql_TGT)
    print("target data :", df_mysql_tgt)
