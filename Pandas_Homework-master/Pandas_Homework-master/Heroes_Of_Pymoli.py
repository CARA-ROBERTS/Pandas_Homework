#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pymoli = "purchase_data.csv"


pymoli_df = pd.read_csv(pymoli)

pymoli_df.head()


# In[3]:


players_count = len(pymoli_df["SN"].unique())
players_count


# In[4]:


Total_Players_df= pd.DataFrame({
                                 "Total Players":[players_count]})

Total_Players_df


# In[5]:


pymoli_df["Item Name"].unique()


# In[6]:


unique_items_count = len(pymoli_df["Item Name"].unique())
unique_items_count


# In[7]:


pymoli_df["Price"].mean()


# In[8]:


number_of_purchases = pymoli_df["Purchase ID"].count()
number_of_purchases


# In[9]:


total_revenue = pymoli_df["Price"].sum()
 
total_revenue


# In[10]:


print("Purchasing Analysis (Total)")
purchasing_analysis_table = pd.DataFrame({"Number of Unique Items": [unique_items_count],
                                          "Average Price":[pymoli_df["Price"].mean()],
                                          "Number of Purchases":[number_of_purchases],
                                          "Total Revenue" :[total_revenue]})
purchasing_analysis_table


# In[11]:


gender_count = pymoli_df["Gender"].value_counts()
gender_count 


# In[12]:


gender_total = pymoli_df["Gender"].count()
gender_total


# In[13]:


gender_percentage = (pymoli_df["Gender"].value_counts()/pymoli_df["Gender"].count())*100
gender_percentage.head()


# In[14]:


pymoli_df = pymoli_df.groupby(["Gender"])

print(pymoli_df)

pymoli_df.count().head()


# In[15]:


gender_table = pd.DataFrame({"Total Count":gender_count ,
                             "Percentage of Players": gender_percentage})
gender_table.head()

