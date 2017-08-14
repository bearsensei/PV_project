# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_train = pandas.read_csv("train.csv")
titanic_train.info()
print (titanic_train)

titanic_survived = titanic_train[titanic_train["Survived"] == 1]
titanic_died = titanic_train[titanic_train["Survived"] == 0]

titanic_survived_male = titanic_survived[titanic_survived["Sex"] == "male"]
titanic_survived_female = titanic_survived[titanic_survived["Sex"] == "female"]

#==============================================================================
# titanic_train.Age[titanic_train.Pclass == 1].plot(kind='kde')   
# titanic_train.Age[titanic_train.Pclass == 2].plot(kind='kde')
# titanic_train.Age[titanic_train.Pclass == 3].plot(kind='kde')
# plt.xlabel(u"Age")# plots an axis lable
# plt.ylabel(u"Density") 
# plt.title(u"Distribution")
# plt.legend((u'1st', u'2nd',u'3rd'),loc='best')
#==============================================================================
age_null = pd.isnull(titanic_survived["Age"])
age_null_count = len(age_null[age_null == True])

correct_mean_age = titanic_survived["Age"].mean()
correct_mean_fare = titanic_survived["Fare"].mean()
passenger_classes = [1, 2, 3]
fares_by_class = {}



for pclass in passenger_classes:
    pclass_rows = titanic_survived[titanic_survived["Pclass"] == pclass]
    pclass_fares = pclass_rows["Fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[pclass] = fare_for_class

print(pclass_fares)

passenger_survival = titanic_train.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
passenger_age = titanic_train.pivot_table(index = "Pclass", values = "Age", aggfunc= np.mean)

passenger_survival = titanic_train.pivot_table(index="Pclass", values=["Age", "Survived"], aggfunc=np.mean)

port_stats = titanic_train.pivot_table(index="Embarked", values=["Age", "Survived","Fare"], aggfunc=np.mean)
print(port_stats)

new_titanic_survival = titanic_survived.dropna(subset=["Age","Fare"])

#row_index_25 = new_titanic_survival.loc[25,:]
#row_position_fifth = new_titanic_survival.iloc[4,:]

print(titanic["Sex"].unique())

titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

# Find all the unique values for "Embarked".
print(titanic["Embarked"].unique())
titanic["Embarked"] = titanic["Embarked"].fillna("S")

titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

