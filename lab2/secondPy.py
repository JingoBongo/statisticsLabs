# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import math


# %%
# 1.	Load and print the first 20 observations of the dataset. Report if you see any unusual values.
dataset = pd.read_csv('HousingData.csv')
# short notes for myself that describe the columns
# CRIM crime rate
# CHAS near bridge or not
# RM average room number
# AGE proportion of built houses somewhere before 1940
# DIS weighted mean to distances to 5 employment centres
# TAX property taxes per 10.000 dollars
# LSTAT somehow percentage of lower status people
# MEDV median value of home in 1000 dollars

dataset.head(20)

# %% [markdown]
# Somehow I see places with very high crime rate but low lower status rate; crime == rich?
# %% [markdown]
# 2.	Discuss what effects you would expect to see on the med home values (medv) for each variable.
#     I expect to see more expensive homes with such conditions as: high room number, low criome rate, near the bridge 
#     Values like AGE and DIS seem subjective for me and I think they differ from case to case. Also I don't think taxes matter that much,  
#     and sadly I suppose towns/homes with lower LSTAT value are more expensive because rich ones want to stick to other rich

# %%
# 3.	Compile the table with summary statistics (min, max, med, etc). Add the measure of skewness to this table. 
# Comment on the table and report briefly if you see anything unusual in the statistics of your variables.
described_dataset = dataset.describe()
# described_dataset.loc['median'] = dataset.median() - 50 percentile is just our median
described_dataset.loc['skewness'] = dataset.skew()
described_dataset
# I found negative percentage of age and I think that's odd. say 0% if there are no houses built before 1940. What can be -0.5? 
# What is average room number of 0.4? Some houses don't have rooms?
# Some places don't have taxes (0.669) almost at all, given the median is 330 and max is 711
# * In general crime rate is about 0.2, but there are maxed places with 88 which looks way too much, must be an outlier; did it
#   affect the std this much?
# * Most of the houses are not near the bridge
# * Most common room number is 6, nothing special. Maybe only the one with 8.78 is as expensive as the others, I thought it would cost more
# * Most of the house percentage is built before 1940, therefore I don't think the price relies on this metric
# * Distance to employment centres is about 3 in average, so 12 should feel like a real outcast and price would be corresponding.
# * So far no idea how taxes would differ based on other parameters, maybe being close to bridge causes some additional water repair 
#   related costs
# * Originally I had an idea that the bigger the house, more the price. I was wrong. Then that it differs from position. This seems to be true


# %%
# 4.	Check the types of your data. Change the types as appropriate (if any categorical variable present change its type to category).
print(dataset.dtypes)
dataset['CHAS'] = dataset['CHAS'].astype('category')
print(dataset.dtypes)
print(dataset)


# %%
# 5.	Substitute the NaN values with appropriate measures of central tendency 
# (mean, median, or mode – for the categorical variable – if you can’t change to mode, 
# then check what is the most frequent value of that variable (you can use value_counts) and change it to the most frequent value).
#  You may want to do this procedure for all variables to make sure that you did not miss a variable because you were not able to see 
# that the variable contains NaNs while inspecting the table. 
counter = 0
for column in dataset:
    for value in dataset[column].values:
        if math.isnan(value):
            # print(column+' has nan')
            counter += 1
            
print(counter)


