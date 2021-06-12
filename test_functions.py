
import random
def Hungry():
    
    """ Randomly picks Valencias typical experience from a list of days of the week
     Can be used to help the user see if my niece has any feeding habits based on days of the week"""
    
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
    

assert Hungry is not None 

def plotGraph():
    
    plt.bar(Days_of_week, Drank_in_mL,color= New_Colors) 
    
    
    plt.title('How much Val Drank per day', fontsize= 18)
    
    
    plt.xlabel('Days of the week', fontsize=16)
    
    
    plt.ylabel('Milk Consumed in mL', fontsize=16) 
assert plotGraph is not None 


class Baby:
    def __init__(Baby_girl, name, age):
        Baby_girl.name = name
        Baby_girl.age = 1

    def mybaby(Baby_girl):
        print("Hello my name is " + Baby_girl.name + " I am a newborn baby come see what a week with me is like!")

p = Baby ("Valencia", 1)
p.mybaby()


assert callable(Baby)

assert p.name is not None

assert p.age is not None 




    