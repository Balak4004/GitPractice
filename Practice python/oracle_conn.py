

import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle


orcle_engine = create_engine('oracle+cx_oracle://hr:hr@localhost:1521/xe')

connection = orcle_engine.connect()
df = pd.read_sql("select * from city", connection).tail(5)
print(df)