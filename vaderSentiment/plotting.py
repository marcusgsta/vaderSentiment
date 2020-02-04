# import numpy as np

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# create a list of names
tweets = [692, 541, 1002, 801, 1694, 1342]

# Create a list of ages
estimations = ['Cor Pos', 'Incor Pos', 'Cor Neg', 'Incor Neg', 'Cor', 'Incor']

# add new column to dataframe
# TotalCorrect = [11000, 10000, 30000, 19000]

# create a dictionary
data_dict = {'tweet': pd.Series(tweets), 'estimation': pd.Series(estimations)}

# create a pandas DataFrame from dictionary

dframe = pd.DataFrame(data_dict)

# dframe['estimations'] = pd.Series(estimations)

plt.rcParams['figure.figsize'] = (10,6)
matplotlib.style.use('ggplot')

print(dframe)

# plot dataFrame

# dframe.plot.bar()
# dframe[['salary']].plot.bar()
dframe.plot.bar(x='estimation', y="tweet", color=("g", "r", "g", "r", "g", "r"))

plt.show()

