"""Classes used throughout project"""
import matplotlib.pyplot as plt

class Baby:
    
    """prints Valencia's greeting, and executes it on the p object"""
    
    def __init__(baby_girl, name, age):
        
        """------baby_girl is a parameter---
        Objects of type of Baby: baby_girl.name, baby_girl.age
        
        Class methods for objects of type Baby
       
        Adds strings plus methods to return an introduction
        """
        baby_girl.name = name 
        
        baby_girl.age = 1            
       
    def mybaby(baby_girl):
        
        print("Hello my name is " + baby_girl.name + " I am a newborn baby come see what a week with me is like!")

p = Baby ("Valencia", 1)

p.mybaby()
 
p.age


""" Title: Python Classes and Objects
Author: W3schools 
Date: 1999-2021
Code version: Python
Availability: https://www.w3schools.com/python/python_classes.asp"""