class myclass:
    x=5

p1 =myclass()
print(p1.x)

# constructor -> __init__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",36)

print(p1.name)
print(p1.age)


# __str__() used to control what should be returned after the class object is represented as a string 

class Person1:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
    

    def __str__(self):
        return f"{self.name}({self.age})"
    
p2 = Person1("John",36)
print(p2)


# create own methon
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"Hello my name is  {self.name} {self.age}")

p3 = Person3("John", 36)
p3.myfunc()


# Inheritance

class Person4:
   def __init__(self,fname,lname):
      self.firstname  = fname
      self.lastname = lname

   def printname(self):
      print(self.firstname, self.lastname)

x = Person4("Anubhav","Sood")

x.printname()



class Student(Person4):
   pass
y = Student("Aditya","Patel")
y.printname()

# we can ovveride tehe parent constructor 
# to keep the inheritance of the parent functino add a call to the parent's __init__() function:
class Student1(Person4):
   def __init__(self, fname, lname,year):
    #   Person4.__init__(fname, lname)
    #   can also use super to inherit all the things from the parent class 
      super().__init__(fname,lname)
      self.graduationyear = year
    #   By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
   def welcome(self):
        print( "Welcome ",self.firstname," ",self.lastname,"to the class of ", self.graduationyear )     
z = Student1("Sood","Anubhav",21)
print(z.graduationyear)
z.welcome()

# Iterator is  an object that contains a countable number of values.
# List,tuple,dicitionaries and set all are iterable 

mytup = ("Apple","Banana","cherry")

myit = iter(mytup)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#  creating iterable in the class


class Mynumbers:
   def __iter__(self):
      self.a = 1
      return self
   
   def __next__(self):
      x = self.a
      self.a += 1
      return x
   
myclass = Mynumbers()

myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# To prevent the iteration from going on forever, we can use the StopIteration statement.

# Polymorphism - It means the same functions having the same name but different functionalities or parameters.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
     print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
     print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
     print("FLY!")


car1 = Car("Ford","Mustang")
Boat1 = Boat("Ibiza", "Touring 20")
Plane1 = Plane("Boeing","747")


for x in (car1,Boat1,Plane1):
   x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


import math 
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x,y)

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")



# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
print("Enter your name:")
name = input()
print(f"Hello {name}")


#  virtual environments is important because:

# It prevents package version conflicts between projects
# Makes projects more portable and reproducible
# Keeps your system Python installation clean
# Allows testing with different Python versions

# python -m venv myfirstproject
# myfisrtproject\Scripts\activate
# deactivate
import os

print(os.getcwd())
# os.mkdir("new_folder")
print(os.listdir())
import os

print(os.getenv('HOME'))   # Get environment variable
os.environ['MY_VAR'] = '123'  # Set environment variable

from datetime import timedelta,datetime
# add 5 minutes to the time 
times = "14:25:30"

given_time = datetime.strptime(times,"%H:%M:%S")
new_time = given_time + timedelta(minutes=15)

print(new_time.time())