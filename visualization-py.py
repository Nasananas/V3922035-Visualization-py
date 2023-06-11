#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as plt


# In[2]:


df = pd.read_csv("C:/Users/user/data bank.csv")
df


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/data bank.csv")

plt.scatter(data['age'], data['job'])

plt.title("Scatter Plot")

plt.xlabel('Age')
plt.ylabel('Job')

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/data bank.csv")

plt.plot(data['age'])
plt.plot(data['month'])

plt.title("Line Chart")

plt.xlabel('job')
plt.ylabel('age')

plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/data bank.csv")

plt.bar(data['age'], data['month'])

plt.title("Bar Chart")

plt.xlabel('Umur')
plt.ylabel('Bulan')

plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/data bank.csv")

plt.hist(data['age'])

plt.title("Histogram")

plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/user/data bank.csv")

bank = ['day', 'duration', 'age']

data = [5, 1, 29]

plt.pie(data, labels=bank)

plt.title("bank data")

plt.show()


# In[ ]:




