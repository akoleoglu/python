# -*- coding: utf-8 -*-
"""sales_report_MyFirst_Report.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/118eDID3aqQgZv3ZkYHVTZCUg8ZXVZHEL
"""

import pandas as pd

!ls 'drive/My Drive/data.csv'

df = pd.read_csv('drive/My Drive/data.csv',encoding='cp1252')

df

df.dtypes

df['CustomerID'] = df['CustomerID'].fillna('unknown',inplace = True)
df['CustomerID'] = df['CustomerID'].astype(str)

df.dtypes

df['InvoiceDate'][0]

pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')

df['date'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')

df

df['date'].dt.month

df['month'] = df['date'].values.astype('datetime64[M]')

df

df.groupby('month')[['UnitPrice','Quantity']].agg('sum').sort_values('month')

df.groupby('month')[['UnitPrice']].sum().sort_values('month').plot()

customer=df.groupby(['month','CustomerID'])[['UnitPrice','Quantity']].agg('sum').reset_index()

len(customer)

customer

customer[customer['CustomerID']==18245.0]

user  = pd.DataFrame({'CustomerID':df['CustomerID'].unique()})

user=df.groupby('CustomerID')['month'].min().to_frame().reset_index()

user.columns

user.columns = ['CustomerID', 'reg_month']

user

month=pd.DataFrame({'month':pd.date_range('2010-12-01','2011-12-01',freq='MS')})

month

len(user)*len(month)

user['key']=1
month['key']=1

user

month

report=user.merge(month,on='key').drop('key',axis=1)

report

report=report[report['month']>=report['reg_month']].copy()

report

report[report['CustomerID'] == 12348.0]

df[df['CustomerID']==12348.0]['month'].unique()



df['revenue'] = df['UnitPrice']*df['Quantity']

sales_month = df.groupby(['month','CustomerID'])[['revenue']].agg('sum').reset_index()

report

sales_month

sales_month.groupby('month')[['revenue']].sum()

sales_month['revenue'].sum()

df['revenue'].sum()

df.isna().mean()

df.groupby('month')['revenue'].sum().reset_index().sort_values('month')

report= report.merge(sales_month,how='left',on=['month','CustomerID']).copy()

report

report[report['CustomerID']==12348.0]

report['user']=1

report

report.groupby('month')[['user']].agg('sum')

report.groupby('month')[['user']].agg('sum').plot()

report

report['active'] = (report['revenue']>0)*1

report

r =report.groupby('month')[['user','active','revenue']].agg('sum').reset_index()

r['active_%'] = r['active']/r['user']

r

r

df.groupby('month')[['revenue']].sum().reset_index().sort_values('month')

r.set_index('month')['revenue'].plot(grid=True)

r['active_%'].plot()

report.head()

r =report.groupby('month')[['user','active','revenue']].agg('sum').reset_index()

r

