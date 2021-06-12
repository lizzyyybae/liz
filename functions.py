"""A collection of function for doing my project."""


def Hungry():
    
    """ Randomly picks Valencias typical experience from a list of days of the week
    Can be used to help the user see if my niece has any feeding habits based on days of the week
    Randomly goes through days and derives its unique data
    input: days_of_week: contains data from different days
    variable: random_day: randomizes the days from days_of week
    output: random_day: returns unique responses in variable"""
    
    Monday = {'Baby_V':'Monday', 'drank  in mL': 100, 'nursed in minutes' : 10, 'wet diaper': 'Large'}

    Tuesday = {'Baby_V': 'Tuesday', 'drank  in mL': 120, 'nursed in minutes' : 12, 'wet diaper': 'Medium'}

    Wednesday = {'Baby_V': 'Wednesday', 'drank  in mL': 90, 'nursed in minutes' : 33, 'wet diaper': 'Large'}

    Thursday = {'Baby_V': 'Thursday', 'drank  in mL': 120, 'nursed in minutes' : 25, 'wet diaper': 'Small'}

    Friday = {'Baby_V': 'Friday', 'drank  in mL': 110, 'nursed in minutes' : 18, 'wet diaper': 'Large'}

    Saturday = {'Baby_V': 'Saturday', 'drank  in mL': 90, 'nursed in minutes' : 21, 'wet diaper': 'Medium'}

    Sunday = {'Baby_V': 'Sunday', 'drank  in mL': 100, 'nursed in minutes' : 15, 'wet diaper': 'Small'}

    Days_of_week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
    
    random_day = random.choice(Days_of_week)
    
    return random_day

""" Title: Functions
Author: W3schools
Date: 1999-2021
Code version: Python
Availability: https://www.w3schools.com/python/python_functions.asp """



import matplotlib.pyplot as plt

"""Bar graph of milk consumed by the days of the week
   Combines the days_of_week and Drank_in_mL and makes a bar graph
   New_Colors makes each bar have a new color based on the colors included """

Days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']

Drank_in_mL = [100, 120, 90, 120, 110, 90, 100]

New_Colors = ['green','blue','purple','pink','orange', 'grey', 'red']

def plotGraph():
    
    plt.bar(Days_of_week, Drank_in_mL,color= New_Colors) 
    
    plt.title('How much Val Drank per day', fontsize= 18) 
    
    plt.xlabel('Days of the week', fontsize=16)
    
    plt.ylabel('Milk Consumed in mL', fontsize=16) 
    
plotGraph()

""" Title: How to create a Bar Chart in Python
Author: data of fish
Date: 4 July 2020
Code version: Python
Availability: https://datatofish.com/bar-chart-python-matplotlib/"""
