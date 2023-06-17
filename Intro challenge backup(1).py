#!/usr/bin/env python
# coding: utf-8

# # Data Analytics - Challenge
# 

# The goal of this challenge is to analyze a restaurant invoices. Some celles are already implemented, you just need to **run** them. Some other cells need you to write some code.
# 
# Start the challenge by running the two following cells:

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


tips_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")


# ---
# 
# ❓ Display the 10 first rows of the dataset (no need to sort)
# 
# <details>
#     <summary>🙈 Reveal solution</summary>
# 
# <p>
# You can use the <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html"><code>pandas.DataFrame.head()</code></a> function:
#     
# <pre>
# tips_df.head(10)
# </pre>
# </p>
# </details>

# In[3]:


tips_df.head(10)


# ---
# 
# ❓ How many days per week is the restaurant open?
# 
# <details>
#     <summary>🙈 Reveal solution</summary>
# 
# <p>
# You can use the <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html"><code>pandas.Series.unique()</code></a> function combiend with the <code>len()</code> Python built-in.
#     
# <pre>
# len(tips_df['day'].unique())
# </pre>
# </p>
# </details>

# In[4]:


len(tips_df['day'].unique())


# ---
# 
# ❓ What day of the week is there more bills? Plot this with a Seaborn Countplot.
# 
# <details>
#     <summary>🙈 Reveal solution</summary>
# 
# <p>
# <pre>
# tips_df['day'].value_counts()
# </pre>
#     
# <pre>
# sns.countplot(data=tips_df, x='day', order=['Thur', 'Fri', 'Sat', 'Sun'])
# </pre>
# </p>
# </details>

# In[5]:


tips_df['day'].value_counts()


# In[6]:


sns.countplot(data=tips_df, x='day', order=['Thur', 'Fri', 'Sat', 'Sun'])


# ---
# 
# ❓ Try to do some other countplots, varying `x` with one of the categorical column (`sex`, `smoker`, `time`)

# In[7]:


tips_df['sex'].value_counts()


# In[8]:


sns.countplot(data=tips_df, x='sex', order=['Male', 'Female'])


# ---
# ❓ Let's plot the distribution of `total_bill` based on a given category. Start with `day`:
# 
# ```python
# sns.catplot(data=tips_df, x='day', y='total_bill', kind="box")
# ```
# 
# 1. Change the value of `x` with one of the categorical column of the dataset and the value of `kind` (`"bar"`, `"box"`, `"violin"`, `"boxen"`)
# 1. Change the value of `y` with one of the numerical column of the dataset

# In[9]:


sns.catplot(data=tips_df, x='day', y='total_bill', kind="box")


# In[10]:


sns.catplot(data=tips_df, x='sex', y='total_bill', kind="bar")


# In[11]:


sns.catplot(data=tips_df, x='tip', y='total_bill', kind="violin")


# ---
# ❓ Let's use [`seaborn.FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
# 
# 1. Run the cell below. What do you observe?
# 2. Change `col` in the first line with another column (e.g. `"time"`). Run the cell again. What do you observe?

# In[12]:


g = sns.FacetGrid(tips_df, col="day")
g.map(plt.hist, "total_bill")


# ---
# ❓ Let's continue with FacetGrid and add a `row="smoker"` parameter. How many cells do you get in the plot?
# 
# <details>
#     <summary>🙈 Reveal solution</summary>
# 
# You get 2 * 4 = 8 cells!
#     
# <pre>
# g = sns.FacetGrid(tips_df, col="day", row="smoker")
# g.map(plt.hist, "total_bill")
# </pre>
# </p>
# </details>

# In[13]:


g = sns.FacetGrid(tips_df, col="time", row="smoker")
g.map(plt.hist, "total_bill")


# In[14]:


num_cells = g.axes.shape[0] * g.axes.shape[1]
print(f"There are {num_cells} cells in the plot! ")


# ## Correlation
# 
# Let's start looking for correlation between columns in the dataset.
# 

# ---
# ❓ What is your intuition about the relationship between the columns `tip` and `total_bill`?

# In[25]:


sns.catplot(data=tips_df, x='total_bill', y='tip')


# ---
# ❓ Let's look at the data to see if our intuition is correct. We will do a **scatterplot** with `x` being `total_bill` and `y` the tip.

# In[15]:


with sns.axes_style(style="whitegrid"):
    sns.relplot(x="total_bill", y="tip", data=tips_df)


# ---
# ❓ Another way of looking at this data is to use a [`seaborn.jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html).

# In[16]:


with sns.axes_style("white"):
    sns.jointplot(x="total_bill", y="tip", kind="hex", data=tips_df)


# ❓ A very useful tool to **identify** correlations is the [`seaborn.pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html):

# In[17]:


sns.pairplot(tips_df, height=2, hue="smoker")


# ## Regression
# 
# We are not doing Machine Learning yet but we can use [`seaborn.lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) to graphically read a linear correlation between two columns:

# In[18]:


sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips_df)


# ## Good job!
# 
# Save your notebook, go back to the **Le Wagon - Learn** platform to upload your progress. A quiz awaits you!
