
import pandas as pd
df = pd.read_csv('sales_data.csv',  dtype = {'sales_id':float, 'price':int})
df['sales_date'] = pd.to_datetime( df['sales_date'])
df['year'] = df['sales_date'].dt.year
df = df[['year','sales_id', 'price']]
print(df)