import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print(df['A'])
print(df.A)

print(df[0:3])  # 0,1,2三行
print(df['2013-01-02': '2013-01-04'])

print(df[['A', 'C']])

print(df.loc['2013-01-02'])
print(df.loc[:, ['A', 'C']])
print(df.loc['2013-01-02', ['A', 'C']])

print(df.iloc[3])
print(df.iloc[3:5, 1:3])

print(df['A'] > 8)

df.iloc[1,3] = np.nan
print(df)
# df.dropna(axis=0, inplace=True) # 把有NaN的行丢掉，如果axis=1，则丢掉NaN的列
df.fillna(0, inplace=True) # 把NaN换成0

print(df)
