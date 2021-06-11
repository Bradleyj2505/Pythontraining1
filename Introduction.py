# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:13:43 2021

@author: -
"""

height = 1.50
weight = 80.0 # <-----

bmi = weight / height ** 2
#print(bmi)


wageat = 30000
bills = 12000
takehome = wageat - bills
#print(takehome)

#number_of_pupils = 10
#print(type(number_of_pupils))


x = "Body Mass Index"
y = 'This works also'

f = False
t = True


pounds = 600
exchangerate = 1.116 

euros = pounds * exchangerate 
#print(euros)


Score = 50 
Time = 60 

Score + Time 


Team = {"Firstname": ["Bob","Bill", "James", "Sharon", "Lisa", "Claire"],
        "Lastname": ["Smith", "Jones", "Morris", "Smith", "Pearce", "Morgan"],
        "Gender": ["Male", "Male", "Male", "Female", "Female", "Female"],
        "Age": [50, 30, 18, 40, 38, 36],
        "Job Role": ["Director", "Analyst", "BI Officer", "Assistant", "Developer", "Tester"]
        }
        

Tvtuple = ("Friends", "Breaking Bad", "Prison Break", "The Office", "Line of Duty")
Tvlist = list(Tvtuple)
Tvlist[4] = "Eastenders"
Tvtuple = tuple(Tvlist)

print(Tvtuple)


Country1 = ["France", "Spain", "Germany", "England", "Wales", "Greece"]
Country2 = ["USA", "China", "Japan", "Serbia", "Mexico", "India"]
Country3 =["Pakistan", "Turkey", "Croatia", "Scotland", "Ireland", "Brazil"]
Country4 = ["Belgium", "Australia", "Sri Lanka", "Italy", "Poland", "Lebanon"]

Country1.remove("France")
Country2.remove("USA")
Country3.remove("Pakistan")
Country4.remove("Belgium")

Country1.clear()
del Country3

Country2.insert(6, "Gabon")
Country2.insert(7, "Fiji")
Country2.extend(Country4)

#a = 20
#b = 30 

#add = a + b
#print(add)

#subtract = a - b 
#print(subtract)

#multiply = a * b
#print(multiply)

#division = a / b 
#print(division)

#division2 = a // b
#print(division2)

#modulo = a % b
#print(modulo)

#power = a ** b
#print(power)



#print(a > b)

#print(a < b)

#print(a == b)

#print(a != b)

#print(a >= b)

#print(a <= b)



#Logical Operator
#a = True
#b = False

#a and b are false?
#print(a and b)

#a or b is true?
#print(a or b)

#not a is False?
#print(not a)



#firstlist = ["Tennis", "Golf", "Rugby", "Darts", "Football", "Golf", "Rugby"]
#secondlist = [1, 10, 20, 30]
#thirdlist = ["Tennis", 20, True, "Rugby", 19, False]

#firstlist.extend(thirdlist)
#firstlist.extend(secondlist)





firsttuple = ("Football", "Rugby", "Cricket", "Boxing")
#print(firsttuple[1])

#tuplechanges = list(firsttuple)
#tuplechanges.remove("Rugby")
#firsttuple = tuple(tuplechanges)

#print(firsttuple)

(team, team1, team2, individual) = firsttuple

#print(team)
#print(team1)
#print(team2)
#print(individual)


firstset = {"Biscuits", "Chocolate", "Crisps", "Cake", "Fruit"}
#print(firstset)

#print("Chocolate" in firstset)
#print("Apple" in firstset)

#firstset.add("Drinks")
#print(firstset)


#firstset.pop()
#print(firstset)


firstdict = {
        "Breed": "Pug",
        "Age": "Three",
        "Colour": "Brown",
        "Colour": "Black"
        }
#print(firstdict)

#print(firstdict["Breed"])

access = firstdict["Age"]
#print(access)

listofkeys = firstdict.keys()
print(listofkeys)


#firstdict["Breed"] = "Border Collie"
firstdict.update({"Breed": "Labrador"})

firstdict.update({"Height": 1.50})

firstdict["Weight"] = 67.5
print(firstdict) 

