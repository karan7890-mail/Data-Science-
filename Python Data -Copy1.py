#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df=pd.read_csv("Open Market.csv",sep=",")
df


# In[2]:


import pandas as pd

df = pd.DataFrame({
    'SYMBOL': ['SBILIFE', 'KOTAKBANK', 'BHARTIARTL', 'TATASTEEL', 'ICICIBANK', 'ADANIPORTS', 'HDFCBANK', 'BPCL', 'COALINDIA', 'LT'],
    'PREV_CLOSE': [1449.20, 1746.70, 1392.35, 180.02, 1144.45, 1448.40, 1657.85, 615.8, 477.95, 3589.95],
    'IEP': [1476.00, 1765.00, 1405.95, 181.60, 1154.05, 1459.30, 1669.80, 620.0, 481.05, 3584.95],
    'CHNG': [26.8, 18.3, 13.6, 1.58, 9.6, 10.9, 11.95, 4.2, 3.1, 23.0],
    '%CHNG': [1.85, 1.05, 0.98, 0.88, 0.84, 0.75, 0.72, 0.68, 0.65, 0.65],
    'FINAL': [1476.00, 1765.00, 1405.95, 181.60, 1154.05, 1459.30, 1669.80, 620.0, 481.05, 3584.95],
    'VALUE': [2.4, 6.79, 5.21, 2.96, 25.88, 2.45, 55.93, 2.1, 1.06, 4.2],
    'FFM_CAP': [65349.14, 256704.15, 364895.37, 148361.98, None, 106641.74, None, 58819.29, 109336.04, 426474.72],
    'NM_52W_H': [1569.40, 1987.75, 1455.95, 184.6, 1173.00, 1621.40, 1757.50, 687.95, 527.4, 3919.90],
    'NM_52W_L': [1251.65, 1543.85, 826.85, 108.1, 899, 703, 1363.55, 331.45, 223.25, 2354.45]
})

print(df.head())


# In[3]:


# Check for missing values
print(df.isnull().sum())

# Fill missing values with appropriate method, for example, forward fill
df = df.fillna(method='ffill')

# Convert columns to appropriate data types if necessary
df['PREV_CLOSE'] = df['PREV_CLOSE'].astype(float)
df['IEP'] = df['IEP'].astype(float)
df['CHNG'] = df['CHNG'].astype(float)
df['%CHNG'] = df['%CHNG'].astype(float)
df['FINAL'] = df['FINAL'].astype(float)
df['VALUE'] = df['VALUE'].astype(float)
df['FFM_CAP'] = df['FFM_CAP'].astype(float)
df['NM_52W_H'] = df['NM_52W_H'].astype(float)
df['NM_52W_L'] = df['NM_52W_L'].astype(float)

print(df.info())


# In[4]:


# Summary statistics
print(df.describe())

# Information about the dataset
print(df.info())


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data similar to the provided image
df = pd.DataFrame({
    'SYMBOL': ['SBILIFE', 'KOTAKBANK', 'BHARTIARTL', 'TATASTEEL', 'ICICIBANK', 'ADANIPORTS', 'HDFCBANK', 'BPCL', 'COALINDIA', 'LT'],
    'PREV_CLOSE': [1449.20, 1746.70, 1392.35, 180.02, 1144.45, 1448.40, 1657.85, 615.8, 477.95, 3589.95],
    'IEP': [1476.00, 1765.00, 1405.95, 181.60, 1154.05, 1459.30, 1669.80, 620.0, 481.05, 3584.95],
    'CHNG': [26.8, 18.3, 13.6, 1.58, 9.6, 10.9, 11.95, 4.2, 3.1, 23.0],
    '%CHNG': [1.85, 1.05, 0.98, 0.88, 0.84, 0.75, 0.72, 0.68, 0.65, 0.65],
    'FINAL': [1476.00, 1765.00, 1405.95, 181.60, 1154.05, 1459.30, 1669.80, 620.0, 481.05, 3584.95],
    'VALUE': [2.4, 6.79, 5.21, 2.96, 25.88, 2.45, 55.93, 2.1, 1.06, 4.2],
    'FFM_CAP': [65349.14, 256704.15, 364895.37, 148361.98, None, 106641.74, None, 58819.29, 109336.04, 426474.72],
    'NM_52W_H': [1569.40, 1987.75, 1455.95, 184.6, 1173.00, 1621.40, 1757.50, 687.95, 527.4, 3919.90],
    'NM_52W_L': [1251.65, 1543.85, 826.85, 108.1, 899, 703, 1363.55, 331.45, 223.25, 2354.45]
})

# Fill missing values and convert columns to appropriate data types
df = df.fillna(method='ffill')
df = df.fillna(method='bfill')
df = df.apply(pd.to_numeric, errors='ignore')

print(df.head())


# In[12]:


plt.figure(figsize=(10, 6))
sns.histplot(df['%CHNG'], kde=True, color='blue', bins=10)
plt.title('Histogram of % Change')
plt.xlabel('% Change')
plt.ylabel('Frequency')
plt.show()


# In[17]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='IEP', y='FINAL', data=df, hue='SYMBOL', palette='deep', s=100)
plt.title('IEP vs. Final Price')
plt.xlabel('IEP')
plt.ylabel('Final Price')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()



# In[19]:


print(df.columns)


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming the dataframe 'df' is already loaded correctly

# Creating a dummy 'DATE' column starting from '2023-01-01'
df['DATE'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')

# Ensure the 'DATE' column is in datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Plotting the data
plt.figure(figsize=(14, 8))
sns.lineplot(x='DATE', y='IEP', hue='SYMBOL', data=df, palette='tab10', marker='o')
plt.title('IEP over Time for each SYMBOL')
plt.xlabel('Date')
plt.ylabel('IEP')
plt.legend(title='SYMBOL', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()


# In[22]:


print(df.describe())


print(df.info())


# In[25]:





# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Filter out non-numeric columns
numeric_df = df.select_dtypes(include=[float, int])

# Compute the correlation matrix
corr_matrix = numeric_df.corr()

# Plot the correlation matrix heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[27]:


from scipy import stats

# Example: T-test between PREV_CLOSE and FINAL
t_stat, p_val = stats.ttest_rel(df['PREV_CLOSE'], df['FINAL'])
print(f'T-statistic: {t_stat}, P-value: {p_val}')


# In[30]:


df.to_csv('cleaned_data.csv', index=False)


# In[ ]:


#https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market
#https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050

