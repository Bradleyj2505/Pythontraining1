# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:43:43 2021

@author: bradley.jones
"""

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

firstlist = ["Tennis", "Golf", "Rugby", "Darts"]

Dataframe = pd.DataFrame(firstlist)
#print(Dataframe)



Dictionary = {
        "Breed": ["Pug", "Border Collie", "Jack Russell", "Yorkie"],
        "Age": ["Three", "Four", "One", "Two"],
        "Colour": ["Brown", "Brown", "Black", "Brown"],
        }

DataFrameDict = pd.DataFrame(Dictionary)
#print(DataFrameDict)

path = "C:\\Users\\bradley.jones\\Documents\\Data Analysis Training\\Spreadsheets\\"


Dataframeimport = pd.read_csv(path +"firstdata.csv")

for bigdf in pd.read_csv(path + "firstdata.csv", chunksize=15):
    print("Chunk")
    print(bigdf)


#print(Dataframeimport)
#print(Dataframeimport.head(3))
#print(Dataframeimport.tail(3))
#print(Dataframeimport.columns)
#print(Dataframeimport['City'])
#print(Dataframeimport['City'][0:5])
#print(Dataframeimport[['City', 'Nationality', 'Job Title']])
#print(Dataframeimport.iloc[1])

#print(Dataframeimport.loc[Dataframeimport['Nationality'] == "China"])


#print(Dataframeimport.sort_values('Nationality'))

Dataframeimport['Total'] = Dataframeimport['Height'] + Dataframeimport['Weight'] + Dataframeimport['Age']

Dataframeimport.head(5)

#Dataframeimport = Dataframeimport.drop(columns=["Movie Title"])

print(Dataframeimport.loc[~Dataframeimport['Nationality'].str.contains('China')])

#print(Dataframeimport.groupby(['Height']).mean())

#print(Dataframeimport.groupby(['Age']).mean())

print(Dataframeimport.groupby(['Age']).count())