


# Importing necessary libraries
import pandas as pd # importing pandas = > useful for creating dataframes
import numpy as np   # importing numpy = > useful for creating numpy arrays 



x1 = [1, 2, 3, 4,5] # list format 
x2 = [10, 11, 12,100,11]  # list format 

x3 = list(range(5)) #0,1,2,3,4

# Creating a data frame using explicits lists
X = pd.DataFrame(columns = ["X1","X2","X3"]) 
X

#X.X1 or X["X1"]

#list -> Series -> Dataframe

#series - single column DF
#DF - More than one column in DF


X["X1"] = pd.Series(x1)  # Converting list format into pandas series format
X["X2"] = pd.Series(x2) # Converting list format into pandas series format
X["X3"] = pd.Series(x3)


X["X1"] = x1 # Converting list format into pandas series format
X["X2"] = x2 # Converting list format into pandas series format
X["X3"] = x3


# accessing columns using "." (dot) operation
X.X1
# accessing columns alternative way
X["X1"]

# Accessing multiple columns : giving column names as input in list format
variable = X[["X1","X2"]]

X[["X1","X2","X3"]]

# Accessing elements using ".iloc" and loc : accessing each cell by row and column 

#iloc - integer location
#loc - string location


# index values
X.iloc[0:3,1]  #0,1,2-rows of 1st column

X.iloc[:,[1,2]] #0,1,2 rows of 0 and 1 columns

X.iloc[:,:] # to get entire data frame 

X.loc[1:3,"X3"]
X.loc[1:3,["X1","X3"]]

X.loc[[1,3,4],["X1","X2"]]

X.loc[0:3,["X1","X2"]] #0,1,2
# checking the type of variable 
type(X.X1) # pandas series object
type(X)
# to create a data frame 

type(X.X2)
type(X["X2"])


import pandas as pd
x = pd.DataFrame(columns=["A","B","C"])

# np.random.randint(a,b,c) 
# a - > starting number
# b - > Ending number
# c - > no. of numbers to be generated 
import numpy as np

x["A"] = pd.Series(list(np.random.randint(1,100,50)))   #randint - random integers
x["B"] = pd.Series(list(np.random.choice([0,1],size = 55))) #first
x["C"] = 15
# Importing necessary libraries
import pandas as pd
import numpy as np


# importing data set using pandas
mba = pd.read_csv("file:///C:/Users/Pravin/Downloads/mba.csv")


type(mba)

mba.head(20)
mba.loc[[1,2],["gmat"]]


# Finding 3rd and 4rth Business Moments
mba.skew()
mba.kurt()

mba['gmat'].kurt()


import matplotlib.pyplot as plt
# Graphical Representation of data
#import matplotlib.pyplot as plt
# Histogram
plt.hist(mba['gmat']) # left skew 

#Boxplot
help(plt.boxplot)
plt.boxplot(mba["gmat"],vert = False)
plt.boxplot(mba['gmat'],vert =False);plt.ylabel("GMAT");plt.xlabel("Boxplot");plt.title("Boxplot")  # for vertical
plt.boxplot(mba['gmat'],1,'rs',1)# For Horizontal
help(plt.boxplot)
plt.boxplot(mba)


# Barplot
# bar plot we need height i.e value of each data
# left - for starting point of each bar plot of data on X-axis(Horizontal axis). Here data is mba['gmat']
index = np.arange(773) # np.arange(a)  = > creates consecutive numbers from 
# 0 to 772 

mba.shape # dimensions of data frame 
help(plt.bar)
plt.bar(height = mba["gmat"], x=np.arange(773)) # initializing the parameter #0 to 773
# left with index values 
help(plt.bar)
import pandas as pd
mtcars = pd.read_csv("file:///E:/data sets/Cars (1).csv")


# table 
pd.crosstab(mtcars.gear,mtcars.cyl)

# bar plot between 2 different categories 
pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar")

mtcars["gear"].value_counts()


mtcars.gear.value_counts().plot(kind="pie")

import seaborn as sns 
# getting boxplot of mpg with respect to each category of gears 
sns.boxplot(x="gear",y="mpg",data=mtcars)

sns.pairplot(mtcars.iloc[:,0:4]) # histogram of each column and 
# scatter plot of each variable with respect to other columns 

import numpy as np
plt.plot(mtcars.mpg,"rs-") # scatter plot of single variable

plt.plot(mtcars.mpg,"ro-")
plt.scatter(mtcars.mpg,mtcars.qsec)## scatter plot of two variables

help(plt.plot) # explore different visualizations among the scatter plot
