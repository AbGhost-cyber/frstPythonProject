import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
df = df.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split Ratio'])
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df.drop(columns=['Adj. Open', 'Adj. High', 'Adj. Low'])

# data = {'Name': ['Ali', 'Abraham', 'Joseph', 'David'],
#         'Age': [25, 28, 37, 29],
#         'Gender': ['Male', 'Male', 'Female', 'Male']}
# df = pd.DataFrame(data)
#  df['Gender'] = (df['Gender'] == 'Male').astype(int)
# df = df.drop(columns=['Gender', 'Age'])

if __name__ == '__main__':
    print(df)
