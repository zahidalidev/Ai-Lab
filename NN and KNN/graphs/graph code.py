#!/usr/bin/env python
# coding: utf-8

# In[259]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

iris = datasets.load_iris()

X = iris.data[:, [0, 1]]
# X = iris.data[:, [2, 3]]
# X = iris.data # input
y = iris.target # output

print(iris.feature_names)
# X = preprocessing.normalize(X) # normalization

# replacing nan values 
imputer = SimpleImputer(missing_values=np.nan, strategy = "mean")
imputer.fit(X)
X = (imputer.transform(X))

# split data into training and test data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# colors
colors = np.array(['red', 'orange', 'pink'])

# for idx, cl in enumerate(np.unique(y)):
setosa = plt.scatter(x=X[y == 0, 0], y=X[y == 0, 1], c=colors[0])
versicolor = plt.scatter(x=X[y == 1, 0], y=X[y == 1, 1], c=colors[1])
virginica = plt.scatter(x=X[y == 2, 0], y=X[y == 2, 1], c=colors[2])

# legends for setosa,versicolor and virginica 
plt.legend((setosa, versicolor, virginica),
           ('setosa', 'versicolor', 'virginica'),
           scatterpoints=1,
           loc='upper left',
           ncol=1,
           fontsize=12)

plt.xlabel("sepal length")
plt.ylabel("sepal width")

plt.show()


# In[228]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import seaborn as sns
sns.set()

data_df=pd.read_csv("iris.csv")

# e=sns.catplot(x="sepal_width", y="sepal_length",col="species", data=data_df, kind="swarm");
#sns.axes_style('axes.linewidth': 1.0)
#plt.xlim(0,8)
#e.set_ticks(np.arange(1,4,1))
#hue="Species"
# e=sns.violinplot(x='species',y='sepal_length', data=data_df)
# e=sns.violinplot(x='species',y='sepal_width', data=data_df)
# e=sns.violinplot(x='species',y='petal_length', data=data_df)
e=sns.violinplot(x='species',y='petal_width', data=data_df)
# e.set(xticklabels=[])


# In[242]:


import seaborn as sns 
  
iris = sns.load_dataset('iris') 
  
# style used as a theme of graph  
# for example if we want black  
# graph with grid then write "blackgrid" 
sns.set_style("whitegrid") 
  
# sepal_length, petal_length are iris 
# feature data height used to define 
# Height of graph whereas hue store the 
# class of iris dataset. 
sns.FacetGrid(iris, hue ="species",  
              height = 6).map(plt.scatter,  
                              'sepal_length',  
                              'petal_length').add_legend() 


# In[ ]:




