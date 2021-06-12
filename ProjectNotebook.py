#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[93]:


class Baby:
    def __init__(Baby_girl, name, age):
        #using instance we will create a variable unique to name
        Baby_girl.name = name
        
        #using instance we will create a variable unique to age
        Baby_girl.age = 1
        
        #using the function mybaby we will add strings and methods to return an introduction"
    def mybaby(Baby_girl):
        print("Hello my name is " + Baby_girl.name + " I am a newborn baby come see what a week with me is like!")

p = Baby ("Valencia", 1)

# using p.mybaby will return the introduction
p.mybaby()


# In[94]:


#p.age will return Valencia's age
p.age 


# In[95]:


#p.name will return Valencia's name
p.name 


# My project will pick my niece's feeding habits for random days of the week!

# In[96]:


import random
import pandas as pd
def Hungry():
    
    # The Hungry function will randomly pick Valencias typical experience from a list of days of the week
    # Can be used to help the user see if my niece has any feeding habits based on days of the week
    
    Monday = {'Baby_V':'Monday', 'drank  in mL': 100, 'nursed in minutes' : 10, 'wet diaper': 'Large'}

    Tuesday = {'Baby_V': 'Tuesday', 'drank  in mL': 120, 'nursed in minutes' : 12, 'wet diaper': 'Medium'}

    Wednesday = {'Baby_V': 'Wednesday', 'drank  in mL': 90, 'nursed in minutes' : 33, 'wet diaper': 'Large'}

    Thursday = {'Baby_V': 'Thursday', 'drank  in mL': 120, 'nursed in minutes' : 25, 'wet diaper': 'Small'}

    Friday = {'Baby_V': 'Friday', 'drank  in mL': 110, 'nursed in minutes' : 18, 'wet diaper': 'Large'}

    Saturday = {'Baby_V': 'Saturday', 'drank  in mL': 90, 'nursed in minutes' : 21, 'wet diaper': 'Medium'}

    Sunday = {'Baby_V': 'Sunday', 'drank  in mL': 100, 'nursed in minutes' : 15, 'wet diaper': 'Small'}

    Days_of_week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
    
    # The random module will randomize the methods (Days_of_week)
    random_day = random.choice(Days_of_week)
    
    return random_day

# This will return a random day my niece is hungry and her feeding habits associated with the specific day
Hungry() 


# In[97]:


import matplotlib.pyplot as plt

#plot_Graph will produce a bar graph of milk consumed by days of the week and Drank_in_mL
Days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']

#rersnts the amount of milk drank
Drank_in_mL = [100, 120, 90, 120, 110, 90, 100]

#Represents the color options
New_Colors = ['green','blue','purple','pink','orange', 'grey', 'red']

def plotGraph():
    #makes sure each bar has a new color according to the day and amount of milk consumed
    plt.bar(Days_of_week, Drank_in_mL,color= New_Colors) 
    
    #adjusts the font size of the title
    plt.title('How much Val Drank per day', fontsize= 18)
    
    #adjusts the font size of the x-axis title
    plt.xlabel('Days of the week', fontsize=16)
    
    #adjusts the font size of the y-axis title
    plt.ylabel('Milk Consumed in mL', fontsize=16) 
    
#returns bar graph    
plotGraph() 


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project

# My project means a lot to me because it is based off of my new born Niece named Valencia. This is my first time ever writing my own code and I wanted to create something that I would be interested in showing others. First I introduced the user to Valencia Then I took data from my sisters Baby Connect app to use for the numerical values in the functions. I used the random module becaus I thought it would be more interesting to see how my nieces feeding habits change through out the week. Honestly this entire course was a challenge for me but I enjoyed creating this code and proud of myself for being able to. I had to look up how to create graphs and add cool features such as different colors.

# In[ ]:




