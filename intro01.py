import sys
#print('hello worlccd')

#courses = ['history','math','english','urdu']
#print(courses)


#def add(a,b):
#	return a+b

#a = 10
#def changeit(b):
#	print("The value of b is",b)
#	b=100
#	print("The new value of b is",b)
#changeit(a)

#a = [10,20,30]
#def func(d):
#	print("The value of d is",d)
#	d[0] = 90
#	print("The new value of d is",d)
#func(a)


#f = open("D:/testyfy.txt",'r')
#print(f.readline())
#print(f.readline())


# class ClassName:
# 	var = "this is a class variable"
# 	def func(self):
# 		print("IM inside the class")


# obj1 = ClassName()
# print(obj1.var)
# obj1.func()


# obj2 = ClassName()
# obj2.var = "this is update ...."
# print(obj1.var,"\n",obj2.var)
# obj2.func()

# print(ClassName.var)

# class student:
# 	def __init__(self,name,branch,year):
# 		self.n = name
# 		self.b = branch
# 		self.y = year
# 	def print_method(self):
# 		print("Name :", self.n)
# 		print("branch :", self.b)
# 		print("year :", self.y)



# obj = student("kash", "VFTD", "htr")
# obj.print_method()
	
# # **********

# class Vehicle:
# 	name = ""
# 	kind = "car"
# 	color = ""
# 	value = 100.00
# 	def description(self):
# 		desc_str = "%s is a %s %s worth $%.3f." % (self.name, self.kind, self.color, self.value)
# 		return desc_str


# car1 = Vehicle()
# car2 = Vehicle()
# car1.name = "Ferrari"
# car1.kind = "Red convertible"
# car1.color = "Red"
# car1.value = 70000.00

# car2.name = "Jeep"
# car2.kind = "Van"
# car2.color = "Blue"
# car2.value = 15000.00

# print(car1.description())
# print(car2.description())

# *************

# class fruit:
# 	def __init__(self):
# 		print("I am fruit")

# class citrus(fruit):
# 	def __init__(self):
# 		super().__init__()
# 		print("I am citrus as well")

# obj = citrus()

# ************

# class A:
# 	x = 1
# class B(A):
# 	pass
# class C(B):
# 	pass
# tr = C()
# print(tr.x)

# import numpy as np

# x = np.arange(16).reshape(4,4)
# print(x)


# a = ['m','o','n','t','y',' ','p']

# print(a[0:4])

import pandas as pd 

# data = [1,2,3,4]
# series1 = pd.Series(data) 
# print(series1)
# print(type(series1))

# series1 = pd.Series(data, index = [['a','b','c','d'],['a','b','w','d'],['a','b','w','d']])
# print(series1)


# Dictionary into DataFrame:
# dictionary = {'fruits':['mangoes','apples','bananas'],'count':[10,20,30]}
# df = pd.DataFrame(dictionary)
# print(df)


# Making Dataframe from lists
player = ['Player1','Player2','Player3']
point = [8,9,6]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Player':player, 'Points':point, 'Title':title})
print(df1,'\n')

player = ['Player1','Player5','Player6']
power = ['Punch','Kick','Elbow']
title = ['Game1','Game5','Game6']
df2 = pd.DataFrame({'Player':player, 'Power':power, 'Title':title})
print(df2, '\n')

# print(df1.merge(df2, on = 'Player', how = 'inner'),'\n')
# print(df1.merge(df2, on = 'Title', how = 'inner'),'\n')

# print('left merge with player')
# print(df1.merge(df2, on = 'Player', how = 'left'))
# print('Right merge with player')
# print(df1.merge(df2, on = 'Player', how = 'right'))
print('outer merge with player')
print(df1.merge(df2, on = 'Player', how = 'outer'))



















