
#Table count validation between source and target


import pandas as pd
from sqlalchemy import create_engine

#Declare Source, Target & Schema values
srt = 'employees'
tgt = 'tgt_empl'
src_schema = 'etlqalabsdb'
tgt_schema = 'target'

#Connect to the MySQL database
mysql_engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb')
conn1 = mysql_engine.connect()

mysql_engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/target')
conn2 = mysql_engine.connect()

if len(srt) ==0 or len(tgt)==0 or len(src_schema)==0 or len(tgt_schema)==0:
    print ("There are no tables/Schema to compare the counts")
else:
    sqry = f"select count(*) cnt from {src_schema}.{srt}"
    res=pd.read_sql(sqry,conn1)
    tqry = f"select count(*) cnt from {tgt_schema}.{tgt}"
    res1=pd.read_sql(tqry,conn2)

    if res.iloc[0,0] == res1.iloc[0,0]:
        print(f"The counts between {srt} table count:({res.iloc[0,0]}) and {tgt} table count:({res1.iloc[0,0]}) are matched")
    else:
        print(f"The counts between {srt} table count:({res.iloc[0,0]}) and {tgt} table count:({res1.iloc[0,0]}) are not matched")

        conn1.close()
        conn2.close()