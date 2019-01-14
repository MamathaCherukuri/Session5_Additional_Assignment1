#!/usr/bin/env python
# coding: utf-8

# 1.Write a python program which creates a class named Cone and write a function calculate_area which calculates the area of the Cone.

# In[7]:


import math
class cone():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * r * s + math.pi * r * r

r=int(input("Enter radius of circle: "))
s=int(input("Enter height of circle: "))
obj=cone(r)
print("Area of cone:",round(obj.area(),2))


# 2.Define a class MathOperation which implements pow(x,n) without usingpython's in-built pow() method

# In[10]:


class py_solution:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(2, 3));
print(py_solution().pow(5,-3));
print(py_solution().pow(-2, 5));
print(py_solution().pow(-5,-3));
print(py_solution().pow(2000, 0));


# 4)Write a python program that creates base class Person which has two
# methods
# def __init__(self, first, last)
# def __str__(self)
# Also create a derived class named Employee which uses the base class
# method “def __str__(self)” using “super()” to concatenate first name with last name

# In[11]:


class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last):
        super().__init__(first, last)
        


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson")

print(x)
print(y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




