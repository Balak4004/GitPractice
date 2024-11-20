

import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle


mysql_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')

connection = mysql_engine.connect()
df = pd.read_sql("select * from employees", connection).tail(5)
print(df)