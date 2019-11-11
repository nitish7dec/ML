#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas_profiling as pp
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob


# In[2]:


df = pd.read_csv(r'C:\Users\nitishkumar\Desktop\P\Cred\Data\Combined_Data\combined_final_sheet.csv')


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.rename(columns={df.columns[0]:'A',df.columns[1]:'G'}, inplace=True)


# In[6]:


df


# In[7]:


df['A'] = df['A'].map(lambda x: x.lstrip('report.'))


# In[8]:


df


# In[9]:


new = df['A'].str.split('.', expand=True)


# In[10]:


new


# In[11]:


new.shape


# In[12]:


df_final = pd.concat([new,df ], axis = 1)


# In[13]:


df_final.drop(['A'], axis = 1) 


# In[14]:


df_final.columns = ['x','a','b','c','d','e','f','G','U_USER_ID']


# In[15]:


df_final


# In[16]:


df_final.drop(['f'], axis = 1,inplace = True) 


# In[17]:


df_final.columns = ['a','b','c','d','e','f','G','U_USER_ID']


# In[18]:


df_final


# In[19]:


OPEN_DATE = df_final[df_final['d'].str.match('DISBURSED-DT').fillna(False)]
OPEN_DATE.rename(columns = {"G": "OPEN_DATE"},inplace = True)
OPEN_DATE.reset_index(inplace = True) 
OPEN_DATE


# In[20]:


DATE_CLOSED  = df_final[df_final['d'].str.match('CLOSED-DATE').fillna(False)]
DATE_CLOSED.rename(columns = {"G": "DATE_CLOSED"},inplace = True)
DATE_CLOSED.reset_index(inplace = True) 
DATE_CLOSED


# In[21]:


ACCOUNT_TYPE  = df_final[df_final['d'].str.match('ACCT-TYPE').fillna(False)]
ACCOUNT_TYPE.rename(columns = {"G": "ACCOUNT_TYPE"},inplace = True)
ACCOUNT_TYPE.reset_index(inplace = True) 
ACCOUNT_TYPE


# In[22]:


AMOUNT_PAST_DUE  = df_final[df_final['d'].str.match('OVERDUE-AMT').fillna(False)]
AMOUNT_PAST_DUE.rename(columns = {"G": "AMOUNT_PAST_DUE"},inplace = True)
AMOUNT_PAST_DUE.reset_index(inplace = True) 
AMOUNT_PAST_DUE


# In[23]:


ACCOUNT_STATUS  = df_final[df_final['d'].str.match('ACCOUNT-STATUS').fillna(False)]
ACCOUNT_STATUS.rename(columns = {"G": "ACCOUNT_STATUS"},inplace = True)
ACCOUNT_STATUS.reset_index(inplace = True) 
ACCOUNT_STATUS


# In[24]:


ACCOUNTHOLDER_TYPE_CODE  = df_final[df_final['d'].str.match('OWNERSHIP-IND').fillna(False)]
ACCOUNTHOLDER_TYPE_CODE.rename(columns = {"G": "ACCOUNTHOLDER_TYPE_CODE"},inplace = True)
ACCOUNTHOLDER_TYPE_CODE.reset_index(inplace = True) 
ACCOUNTHOLDER_TYPE_CODE


# In[25]:


HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT   = df_final[df_final['d'].str.match('DISBURSED-AMT').fillna(False)]
HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT.rename(columns = {"G": "HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT"},inplace = True)
HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT.reset_index(inplace = True) 
HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT


# In[26]:


CURRENT_BALANCE    = df_final[df_final['d'].str.match('CURRENT-BAL').fillna(False)]
CURRENT_BALANCE.rename(columns = {"G": "CURRENT_BALANCE"},inplace = True)
CURRENT_BALANCE.reset_index(inplace = True) 
CURRENT_BALANCE


# In[27]:


Credit_Limit_Amount      = df_final[df_final['d'].str.match('CREDIT-LIMIT').fillna(False)]
Credit_Limit_Amount.rename(columns = {"G": "Credit_Limit_Amount"}, inplace = True)
Credit_Limit_Amount.reset_index(inplace = True) 
Credit_Limit_Amount


# In[28]:


REPORT_DATE = df_final[df_final['b'].str.match('DATE-OF-REQUEST').fillna(False)]
REPORT_DATE.rename(columns = {"G": "DATE-OF-REQUEST"}, inplace = True)
REPORT_DATE.reset_index(inplace = True) 
REPORT_DATE


# In[29]:


REPORT_DATE = REPORT_DATE.drop(['index','a','b','c','d','e','f'],axis=1)


# In[30]:


REPORT_DATE


# In[31]:


REPORT_DATE['DATE-OF-REQUEST']= pd.to_datetime(REPORT_DATE['DATE-OF-REQUEST'], errors = 'coerce')


# In[32]:


REPORT_DATE


# In[ ]:





# In[33]:


REPORT_DATE.to_csv(r'C:\Users\nitishkumar\Desktop\P\Cred\Data\Combined_Data\Final_converted_sheet_accounts\Report_date_v5.csv', index= False)


# In[ ]:





# In[ ]:





# In[34]:


Account_Table = pd.concat([OPEN_DATE,DATE_CLOSED,ACCOUNT_TYPE,AMOUNT_PAST_DUE,ACCOUNT_STATUS,ACCOUNTHOLDER_TYPE_CODE,HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT,CURRENT_BALANCE,Credit_Limit_Amount], axis=1,)


# In[35]:


Account_Table


# In[36]:


Account_Table.drop(['index','a','b','c','d','e','f'], axis = 1,inplace = True)


# In[37]:


Account_Table


# In[ ]:





# In[38]:


Account_Table.columns = ['OPEN_DATE','U_USER_ID','DATE_CLOSED','u_USER_ID','ACCOUNT_TYPE','u_USER_ID','AMOUNT_PAST_DUE','u_USER_ID','ACCOUNT_STATUS','u_USER_ID','ACCOUNTHOLDER_TYPE_CODE','u_USER_ID','HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT','u_USER_ID','CURRENT_BALANCE','u_USER_ID','Credit_Limit_Amount','u_USER_ID']


# In[39]:


Account_Table


# In[40]:


Account_Table.drop(['u_USER_ID'], axis = 1,inplace = True)


# In[41]:


Account_Table


# In[42]:


Account_Table.insert(0, "XML_SEQ_NO",1)


# In[43]:


Account_Table.insert(2, "Account_Number",'NA')


# In[44]:


Account_Table.shape


# In[45]:


Account_Table


# In[46]:


Account_Table = Account_Table[['U_USER_ID','XML_SEQ_NO','Account_Number','OPEN_DATE','DATE_CLOSED','ACCOUNT_TYPE','AMOUNT_PAST_DUE','ACCOUNT_STATUS','ACCOUNTHOLDER_TYPE_CODE','HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT','CURRENT_BALANCE','Credit_Limit_Amount']]


# In[47]:


Account_Table


# In[ ]:





# In[48]:


Account_Table


# In[49]:


def f(flag):
    global previous_seq
    previous_seq = 1 if flag == 0 else previous_seq + 1
    return previous_seq

previous_seq = 0
Account_Table['seq'] = Account_Table[['U_USER_ID']].apply(lambda x: f(*x), axis=1)


# In[50]:


Account_Table


# In[51]:


Account_Table['seq'] = Account_Table['seq'].astype(str)


# In[52]:


Account_Table = Account_Table.drop(['Account_Number'], axis = 1) 


# In[53]:


Account_Table['ACCOUNT_NUMBER'] = Account_Table['U_USER_ID'] + '_'+ Account_Table['seq']
Account_Table


# In[54]:


Account_Table['ACCOUNT_STATUS'].value_counts()


# In[55]:


Account_Table['HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT'] = Account_Table['HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT'].str.replace(' ', '')


# In[56]:


Account_Table


# In[57]:


Account_Table['CURRENT_BALANCE'] = Account_Table['CURRENT_BALANCE'].str.replace(' ', '')


# In[58]:


Account_Table['Credit_Limit_Amount'] = Account_Table['Credit_Limit_Amount'].str.replace(' ', '')


# In[59]:


#Account_Table = Account_Table.fillna(0)


# In[60]:


Account_Table


# In[61]:


Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Credit Card', 10,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Housing Loan',2,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Property Loan',3,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Personal Loan',5,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Consumer Loan', 6,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Gold Loan', 7,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Auto Loan (Personal)', 1,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Loan to Professional', 9,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Secured Credit Card', 31,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Used Car Loan', 32,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan Priority Sector Agriculture', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan General', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan Priority Sector Small Business', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan Unsecured', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan Against Bank Deposits', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan Priority Sector Others', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Loan - Secured', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Non-Funded Credit Facility General', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Business Non-Funded Credit Facility-Priority Sector- Small Business', 51,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Other', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Overdraft', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Education Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Corporate Credit Card', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Loan Against Bank Deposits', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Loan Against Shares / Securities', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Commercial Vehicle Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Two-Wheeler Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Kisan Credit Card', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Pradhan Mantri Awas Yojana - CLSS', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='JLG Individual', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Non-Funded Credit Facility', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Microfinance Personal Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Mudra Loans Shishu / Kishor / Tarun', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Construction Equipment Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Tractor Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Commercial Equipment Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Individual', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Prime Minister Jaan Dhan Yojana - Overdraft', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Loan on Credit Card', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Microfinance Business Loan', 0,Account_Table.ACCOUNT_TYPE)
Account_Table.ACCOUNT_TYPE = np.where(Account_Table.ACCOUNT_TYPE=='Microfinance Housing Loan', 0,Account_Table.ACCOUNT_TYPE)


# In[62]:


Account_Table['ACCOUNT_TYPE'].value_counts()


# In[63]:


Account_Table['ACCOUNT_TYPE'] 


# In[64]:


Account_Table=Account_Table.drop(['seq'], axis = 1) 


# In[65]:


Account_Table


# In[66]:


Account_Table['OPEN_DATE']= pd.to_datetime(Account_Table.OPEN_DATE, errors = 'coerce')


# In[67]:


Account_Table['OPEN_DATE'].value_counts()


# In[ ]:





# In[68]:


Account_Table


# In[69]:


Account_Table


# In[70]:


Account_Table['DATE_CLOSED'] = Account_Table['DATE_CLOSED'].replace(np.nan, '01-01-1990')
Account_Table


# In[71]:


Account_Table['DATE_CLOSED']= pd.to_datetime(Account_Table.DATE_CLOSED, errors = 'coerce')


# In[72]:


Account_Table


# In[73]:


Account_Table


# In[74]:


Account_Table['OPEN_DATE'].value_counts()


# In[75]:


Account_Table['AMOUNT_PAST_DUE'] = Account_Table['AMOUNT_PAST_DUE'].str.replace(' ', '')


# In[76]:


Account_Table['AMOUNT_PAST_DUE'] .value_counts()


# In[77]:


Account_Table['AMOUNT_PAST_DUE'] = Account_Table['AMOUNT_PAST_DUE'].fillna(0)
Account_Table['HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT'] = Account_Table['HIGHEST_CREDIT_OR_ORIGINAL_LOAN_AMOUNT'].fillna(0)
Account_Table['CURRENT_BALANCE'] = Account_Table['CURRENT_BALANCE'].fillna(0)
Account_Table['Credit_Limit_Amount'] = Account_Table['Credit_Limit_Amount'].fillna(0)


# In[78]:


Account_Table['DATE_CLOSED'].value_counts()


# In[79]:


Account_Table


# In[81]:


pp.ProfileReport(Account_Table)


# In[ ]:





# In[ ]:


#Account_Table.to_csv(r'C:\Users\nitishkumar\Desktop\P\Cred\Data\Combined_Data\Final_converted_sheet_accounts\Cred_Account_Table_v5.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




