# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:01:10 2019

@author: Abirmoy
"""

# TESTING *args and *kwargs
# single asterisk * builds tuple
# double asterisl **  Builds dict-->keyward argument
#
##############################################################################
# 
# *args can take as many as parameter user passes
# 1
#def get_mean(*args): 
#    """a function that return mean value"""
#    return sum(args)/len(args)
#
#print(get_mean(10,10,10,10))

# 2
#def print_elem(*args):
#    '''prints all the elements'''
#    # CLONING *args
#    new_args = (*args,) # NOT A MISTAKE
#    for item in new_args:
#        print(item)
#        
#print_elem(10,20,40)        

###############################################################################
# KEYWORD ARGUMENT **kwargs,  IT TAKES TUPLE AND BUILDS DICT.

#1
#def myfunc(**kwargs):
#    print(kwargs) # WILL RETURN DICTIONARY
#    
#    if 'fruit' in kwargs:
#        print('My fruit of choice is {}.'.format(kwargs['fruit']))
##        print('My fruit of choice is '+str(kwargs['fruit']) +'. ')
#    else:
#        print('I didnt find any fruit here.')
#
#myfunc(fruit = 'apple', veggie = 'lattuce')

###############################################################################

# COMBINE *args and **kwargs

#def myfunc(*args, **kwargs):
#    # JUST TO CHECK
#    print(args)
#    print(kwargs)
#    print('I would like {} {}.' .format(args[0], kwargs['food']))
#    
#myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')

############################################################################

### MAP FUNCTION ###

#def square(num):
#    return num**2 # RETURNS THE SQUARE OF THE ARGUMENT
#
#
#my_num = [1,2,3,4,5,6,7,8,9]
#
#for item in map(square, my_num):
#    print(item)
#
## IN ORDER TO GET OUTPUT AS LIST
#my_sqr_list = list(map(square,my_num))
#print(my_sqr_list)



# WORK WITH STRING

#def splicer(mystring):
#    if len(mystring)%2 == 0: # WHICH MEANS STRING HAS EVEN CHARACTER
#        return 'Even'
#    else:
#        return mystring[0] # ELSE RETURN THE FIRST CHARACTER OF THE STRING
#
#names = ['Andy', 'Abir', 'Eve']
#
#mapedList = list(map(splicer, names))
#
#print(mapedList)

############################################################################

# A FUNCTION THAT RETURNS TRUE OF FALSE

#def check_even(num):
#    return num%2 == 0
#
#mynums = [1,2,3,4,5,6,7,8,9]
#
#filtered = list(filter(check_even, mynums))
#print(filtered)
## ANOTHER WAY TO WRITE IT
#for i in filter(check_even, mynums):
#    print(i)

#############################################################################

### LAMDA EXPRESSION ###
#
#'''WILL WRITE THE FUNCTION INSIDE THIS DOCKSTRING AS LAMBDA EXPEWSSION
#STEP 1: def square(num):
#            return num**2
#STEP 2: def square: return num**2 # BAD STYLING'''
## it also culd be assigned to a name
#STEP 3: square = lambda num: num**2
#print(square(5)) # 25
## BUT NOT A COMMON PRACTICE
#
#
#mynums = [1,2,3,4,5,6]
#print(list(map(lambda num: num**2, mynums)))
#
## Let's GRAB FIRST CHARACTER OF THE STRING
#
#name_list = ['Andy', 'Dev', 'Sally']
#print(list(map(lambda name: name[0], name_list)))
#
## REVERS THE ACTUAL NAME 
#name_list = ['Andy', 'Dev', 'Sally']
#print(list(map(lambda name: name[::-1], name_list)))
#

############################################################################

### OBJECT ORIENTED PROGRAMING ###

# BUILDING AN OWN OBJECT

### #1
#class Dog():
#    specis = 'mammal' # CLASS OBJECT ATTRIBUTE, SAME FOR ANY INSTANCE OF THE CLASS
#    def __init__ (self, breed, name, spots):
#        # ATTRIBUTES, ASSIGN IT USING self.attribute_name
#        self.breed = breed
#        self.name = name
#        self.spots = spots # EXPACTS BOOLEAN
#        
#    def bark(self):
#        print('Wolf! My name is {}.' .format(self.name))
#    def bark2(self, number):
#        print('Wolf! My name is {}, and the number is {}.' .format(self.name, number))
#
#
##my_dog = Dog(breed = 'lab', name = 'sanny', spots = False)
#my_dog = Dog('lab', 'sanny', False) # COMMONLY USED STYLE
#print(my_dog.name(), my_dog.breed, my_dog.spots)
#i= my_dog.name, my_dog.breed, my_dog.spots
#print(my_dog.bark()) # my_bark.bark WILL THROW ERROR
#print(my_dog.bark2(10))
#print(i)
#print(type(i))
#print(type(my_dog.name))
#
#
#
### #2
#class Circle():
#    pi = 3.1416
#    def __init__ (self, radius = 1):
#        self.radius = radius
#        self.area = radius*radius*Circle.pi*2 # 2pi r^2
#    def get_circumference (self):
#        return self.radius*Circle.pi*2 # 2pi r
#
#my_circle = Circle(30)
#
#print('Pi: ', my_circle.pi)
#print('Radius: ', my_circle.radius)
#print('Area: ', my_circle.area)
## PAY ATTENTION HOW METHOD is CALLED, my_circle.get_circumference WILL BE ERROR
#print("Circumference: ", my_circle.get_circumference()) 

### INHERITANCE ###
#class Animal():
#    def __init__ (self):
#        print('Animal created.')
#    def who_am_i(self):
#        print('I am an animal')
#    def eat(self):
#        print('I\'m eating.')
#        
#class Dog(Animal):
#    def __init__(self): # INHERITING FROM PREVIOUS OBJECT
#        Animal.__init__ (self) # PAY ATTENTION ON CALLING RULES
#        print('Dog created')
#        
#    # OVERWRITING METHOD
#    def eat(self):
#        print('I am a dog and eating')
#    # NEW METHOD
#    def bark(self):
#        print('Wolf!')
#
#mydog = Dog() # ANIMAL CREATED # DOG CREATED
#mydog.eat() # I AM A DOG AND EATING
#mydog.who_am_i() # I AM AN ANIMAL
#mydog.bark() # WOOF
#
#myanimal = Animal() # ANIMAL CREATED
#myanimal.eat() # I AM EATING
#myanimal.who_am_i() # I AM AN ANIMAL
#
#
### POLYMORPHISM ###
#class Dog():
#    def __init__ (self, name):
#        self.name = name
#    def speak (self):
#        print(self.name, ' says wolf!')
#class Cat():
#    def __init__ (self, name):
#        self.name = name
#    def speak(self):
#        print(self.name, ' says meow!')
#
#niko = Dog('Niko')
#felix = Cat('Felix')
#
#niko.speak() # NIKO SYAS WOOF!
#felix.speak() # FELIX SAYS MEOW!
#
#for pet in [niko, felix]:
#    print(type(pet))
#    print(type(pet.speak()))
#
#def pet_speak(pet):
#    print(pet.speak())
#pet_speak(niko) # Niko  says wolf!
#pet_speak(felix) # Felix  says meow!
#
#
#
### SPECIAL METHODS

### #1
#class Book():
#    def __init__(self, title, author, pages):
#        self.title = title
#        self.author = author
#        self.pages = pages
#    def __str__(self):
#        return f'{self.title} by {self.author}'
#    def __len__(self):
#        return self.pages
#    def __del__(self):
#        print('A book object has been deleted')
#        
#
#b = Book('Himu', 'Humayun', 300)
#
#print(b)
#print(str(b))
#print(len(b))



### 2
#class Simple():
#    def __init__(self, value):
#        self.value = value
#    def add_to_value(self, amount):
#        self.value = self.value + amount
#
#myobj = Simple(300)
#
#print(myobj.value) # 300
#print(myobj.add_to_value(500)) # NOTHING WILL VISIBLE
#print(myobj.value) # 800 CHANGED VALUE 300 + 500
############################################################################









































