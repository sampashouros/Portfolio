# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:47:14 2023

@author: 04660
"""
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.4f}'.format

#Function to remove outliers from a DF
def remove_outliers(df, k=1.5):
    outliers_removed = df.copy()
    for column in df.columns[1:]:
        mean = df[column].mean()
        std = df[column].std()
        lower_bound = mean - k * std
        upper_bound = mean + k * std
        outliers_removed = outliers_removed[(outliers_removed[column] > lower_bound) & 
                                            (outliers_removed[column] < upper_bound)]
    return outliers_removed

#Function to calculate Granger causality matrix
def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False, maxlag=12):    
    df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
    for c in df.columns:
        for r in df.index:
            test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
            min_p_value = np.min(p_values)
            df.loc[r, c] = min_p_value
    df.columns = [var + '_x' for var in variables]
    df.index = [var + '_y' for var in variables]
    return df

#Data loading
df=pd.read_csv(r'C:\Users\04660\Documents\moodle activity - 2021-22 v2.csv')
df=pd.DataFrame(df)
df1=pd.read_csv(r'C:\Users\04660\Documents\2021 users on modules.csv')
df1=pd.DataFrame(df1)

#Data processing
df=df.drop(columns=['users'])
df1.rename(columns={'shortname':'course'}, inplace=True)
df.rename(columns={'shortname':'course'}, inplace=True)
df=df.merge(df1, on='course', how='inner')
df.rename(columns={'count(u.id)':'user'}, inplace=True)

e_table = pd.DataFrame()
e_table['course']=df['course']
e_table['users']=df['user']
e_table['Talis Interactions per user']=df['Talis_Interactions']/df['user']
e_table['Good Interactions per user']=df['G_Act']/df['user']
e_table['Bad Interactions per user']=df['B_Act']/df['user']
e_table['Total Interactions per user']=e_table['Bad Interactions per user']+e_table['Good Interactions per user']+e_table['Talis Interactions per user']
# print(e_table.mean())
# print(e_table.median())

d_table=pd.DataFrame()
d_table['course']=df['course']
d_table['users']=df['user']
d_table['Variety of Activities']=df['total unique activities']
d_table['Total Activities']=df['total activities']
d_table['Intervention activity ratio']=df['g_act_u']/(df['g_act_u']+df['b_act_u'])
d_table['Intervention activity ratio'] = d_table['Intervention activity ratio'].fillna(0)
print(d_table.max())
# print(d_table.median())

#normailsation
e_norm_table=pd.DataFrame()
e_norm_table['course']=e_table['course']
e_norm_table['Talis Interactions per user']=(e_table['Talis Interactions per user']-e_table['Talis Interactions per user'].min())/(e_table['Talis Interactions per user'].max()-e_table['Talis Interactions per user'].min())
e_norm_table['Good Interactions per user']=(e_table['Good Interactions per user']-e_table['Good Interactions per user'].min())/(e_table['Good Interactions per user'].max()-e_table['Good Interactions per user'].min())
e_norm_table['Bad Interactions per user']=(e_table['Bad Interactions per user']-e_table['Bad Interactions per user'].min())/(e_table['Bad Interactions per user'].max()-e_table['Bad Interactions per user'].min())
e_norm_table['Total Interactions per user']=(e_table['Total Interactions per user']-e_table['Total Interactions per user'].min())/(e_table['Total Interactions per user'].max()-e_table['Total Interactions per user'].min())
# e_norm_table=e_norm_table.drop(columns='course')

d_norm_table=pd.DataFrame()
d_norm_table['course']=d_table['course']
d_norm_table['Variety of Activities']=(d_table['Variety of Activities']-d_table['Variety of Activities'].min())/(d_table['Variety of Activities'].max()-d_table['Variety of Activities'].min())
d_norm_table['Total Activities']=(d_table['Total Activities']-d_table['Total Activities'].min())/(d_table['Total Activities'].max()-d_table['Total Activities'].min())
d_norm_table['Intervention activity ratio']=(d_table['Intervention activity ratio']-d_table['Intervention activity ratio'].min())/(d_table['Intervention activity ratio'].max()-d_table['Intervention activity ratio'].min())

m_table = d_norm_table.merge(e_norm_table, on='course', how='left')

m_table_f=remove_outliers(m_table)
# m_table_f=m_table

m_table_f['Variety of Activities']=(m_table_f['Variety of Activities']-m_table_f['Variety of Activities'].min())/(m_table_f['Variety of Activities'].max()-m_table_f['Variety of Activities'].min())
m_table_f['Total Activities']=(m_table_f['Total Activities']-m_table_f['Total Activities'].min())/(m_table_f['Total Activities'].max()-m_table_f['Total Activities'].min())
m_table_f['Intervention activity ratio']=(m_table_f['Intervention activity ratio']-m_table_f['Intervention activity ratio'].min())/(m_table_f['Intervention activity ratio'].max()-m_table_f['Intervention activity ratio'].min())
m_table_f['Talis Interactions per user']=(m_table_f['Talis Interactions per user']-m_table_f['Talis Interactions per user'].min())/(m_table_f['Talis Interactions per user'].max()-m_table_f['Talis Interactions per user'].min())
m_table_f['Good Interactions per user']=(m_table_f['Good Interactions per user']-m_table_f['Good Interactions per user'].min())/(m_table_f['Good Interactions per user'].max()-m_table_f['Good Interactions per user'].min())
m_table_f['Bad Interactions per user']=(m_table_f['Bad Interactions per user']-m_table_f['Bad Interactions per user'].min())/(m_table_f['Bad Interactions per user'].max()-m_table_f['Bad Interactions per user'].min())
m_table_f['Total Interactions per user']=(m_table_f['Total Interactions per user']-m_table_f['Total Interactions per user'].min())/(m_table_f['Total Interactions per user'].max()-m_table_f['Total Interactions per user'].min())

final_table=pd.DataFrame()
final_table['course']=m_table_f['course']
final_table['Design score']=(m_table_f['Variety of Activities']+m_table_f['Intervention activity ratio']*2)/2

final_table['Quality of Engagement score']=(m_table_f['Good Interactions per user'])
final_table['Level of engagement score']=(m_table_f['Talis Interactions per user']+  m_table_f['Total Interactions per user'])/2
final_table['Level of engagement score']=(final_table['Level of engagement score']-final_table['Level of engagement score'].min())/(final_table['Level of engagement score'].max()-final_table['Level of engagement score'].min())

final_table['Design score']=(final_table['Design score']-final_table['Design score'].min())/(final_table['Design score'].max()-final_table['Design score'].min())
final_table['Quality of Engagement score']=(final_table['Quality of Engagement score']-final_table['Quality of Engagement score'].min())/(final_table['Quality of Engagement score'].max()-final_table['Quality of Engagement score'].min())

mer_test=final_table
mer_test = final_table.merge(d_table, on='course', how='left')

#Some statistical analysis
# print(final_table.mean())
# print(df.max())
# print(d_table.max())
# print(d_table.min())

# g_table_F=final_table
# g_table_F=g_table_F.drop(columns='course')
# g_table=grangers_causation_matrix(g_table_F, variables = g_table_F.columns)

#correlation coefficients
r1 = np.corrcoef(final_table['Design score'], final_table['Quality of Engagement score'])
print("\nStudent engagement quality increase: ", r1[0,1])
r2 = np.corrcoef(final_table['Design score'], final_table['Level of engagement score'])
print("\nStudent engagement level increase: ", r2[0,1])


#visualisation
x = final_table['Design score']
y = final_table['Level of engagement score']

a, b = np.polyfit(x, y, 1)
plt.scatter(x, y, 0.5, color='purple')
plt.plot(x, a*x+b,color='steelblue', linestyle='--', linewidth=1)
plt.xlim([0,1])
plt.ylim([0,1])
plt.grid(color = 'grey', linestyle = '-.', linewidth = 0.4, aa=True)
plt.title('Design vs Level of engagement')
plt.xlabel('Design')
plt.ylabel('Level of Engagement')
plt.savefig('Design vs Level of engagement.pdf')
plt.savefig('Design vs Level of engagement.png')
plt.show()
plt.clf()

x = final_table['Design score']
y = final_table['Quality of Engagement score']

a, b = np.polyfit(x, y, 1)
plt.scatter(x, y,0.5, color='steelblue')
plt.plot(x, a*x+b,color='purple', linestyle='--', linewidth=1)
plt.xlim([0,1])
plt.ylim([0,1])
plt.grid(color = 'grey', linestyle = '-.', linewidth = 0.4, aa=True)
plt.title('Design vs Quality of engagement')
plt.xlabel('Design')
plt.ylabel('Quality of Engagement')

#save visuals as PDFs
plt.savefig('Design vs Quality of engagement.pdf')
plt.savefig('Design vs Quality of engagement.png')

plt.show()
plt.clf()
