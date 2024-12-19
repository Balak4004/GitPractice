
# Python Code to Check Multiple Tables:

import pandas as pd
from sqlalchemy import create_engine, inspect
mysql_engine = create_engine('mysql+pymysql://root:admin%402024@localhost:3306/etlqalabsdb')
connection = mysql_engine.connect()

# List of tables to check
table_names = ['employees', 'departments', 'table3']

# Use SQLAlchemy Inspector to get all existing table names
inspector = inspect(mysql_engine)
existing_tables = inspector.get_table_names()

# Check which tables exist
for table_name in table_names:
    if table_name in existing_tables:
        print(f"Table '{table_name}' exists.")
        # Optionally, load the table data into a DataFrame
        df = pd.read_sql_table(table_name, con=mysql_engine)
        print(f"Data from '{table_name}':")
        print(df.head())
    else:
        print(f"Table '{table_name}' does not exist.")