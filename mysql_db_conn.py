



import pandas as pd
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb')

connection = mysql_engine.connect()
df = pd.read_sql("select * from employees", connection)
print(df)