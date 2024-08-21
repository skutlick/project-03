#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Replace 'your_file.csv' with the actual file name or path
movies_df = pd.read_csv('/Users/kevykev/Downloads/top-500-movies.csv')

# Display the first few rows to confirm the import
df.head()


# In[9]:


plt.figure(figsize=(8, 6))
sns.scatterplot(x='production_cost', y='worldwide_gross', data=movies_df)
plt.title('Production Cost vs. Worldwide Gross')
plt.xlabel('Production Cost ($)')
plt.ylabel('Worldwide Gross ($)')
plt.show()


# In[10]:


genre_avg_gross = movies_df.groupby('genre')['worldwide_gross'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 6))
genre_avg_gross.plot(kind='bar', color='skyblue')
plt.title('Top Genres by Average Gross')
plt.xlabel('Genre')
plt.ylabel('Average Worldwide Gross ($)')
plt.show()


# In[11]:


movies_per_year = movies_df.groupby('year').size()
plt.figure(figsize=(8, 6))
movies_per_year.plot(kind='line', color='green')
plt.title('Movies Released Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Movies Released')
plt.show()


# In[12]:


mpaa_distribution = movies_df['mpaa'].value_counts()
plt.figure(figsize=(8, 6))
mpaa_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of MPAA Ratings')
plt.ylabel('')
plt.show()


# In[13]:


top_10_opening = movies_df.nlargest(10, 'opening_weekend')[['title', 'opening_weekend']].set_index('title')
plt.figure(figsize=(8, 6))
top_10_opening.plot(kind='bar', color='orange')
plt.title('Top 10 Movies by Opening Weekend Gross')
plt.xlabel('Movie Title')
plt.ylabel('Opening Weekend Gross ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[14]:


plt.figure(figsize=(8, 6))
sns.scatterplot(x='theaters', y='domestic_gross', data=movies_df)
plt.title('Number of Theaters vs. Domestic Gross')
plt.xlabel('Number of Theaters')
plt.ylabel('Domestic Gross ($)')
plt.show()


# In[15]:


genre_avg_runtime = movies_df.groupby('genre')['runtime'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 6))
genre_avg_runtime.plot(kind='bar', color='purple')
plt.title('Average Runtime by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Runtime (minutes)')
plt.show()


# In[16]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='year', y='worldwide_gross', data=movies_df)
plt.title('Worldwide Gross by Year')
plt.xlabel('Year')
plt.ylabel('Worldwide Gross ($)')
plt.xticks(rotation=45)
plt.show()


# In[17]:


plt.figure(figsize=(10, 8))
corr_matrix = movies_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


# In[18]:


top_10_worldwide = movies_df.nlargest(10, 'worldwide_gross')[['title', 'worldwide_gross']].set_index('title')
plt.figure(figsize=(8, 6))
top_10_worldwide.plot(kind='bar', color='red')
plt.title('Top 10 Highest Grossing Movies Worldwide')
plt.xlabel('Movie Title')
plt.ylabel('Worldwide Gross ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[ ]:




