

# ***** CLASS *****

# --> In Python everything is an Obect. Example : Fan, Lights, Computers, Employees, etc. all are objects.
# --> To create objects we required some "Model Plan" or "Blue Print", which is nothing but a "Class".
# --> We do write "Class" to represent "Properties" (attributes) and "Actions" (behaviour) of object.
# --> "Properties" can be represeted by "variables".
# --> "Actions" can be represented by "methods".
# --> Hence "Class" contains both "variables" and "methods".





# ***** How to define a Class? *****

# --> We can define class by class keyword.

# --> Syntax <--

# class class_Name:
#     '''Documentation String'''        # represents the dscripton of the string.
#     variables: instance variables, static and local variables
#     methods:   instance methods, static methods, class methods

# Note: "Functions" in OOP are called as "methods".


# --> Example <--

# class Student:
#     '''This is student class with required data'''
#     print(Student.__doc__)
#     help(Student)


# --> There are 3 types of variables used in OOP :

# 1. Instance Variables (Object Level Variables)
# 2. Static Variables (Class Level Variables)
# 3. Local Variables (Method Level Variables)



# --> There are 3 types of Methods used in OOP :

# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods





# -------------------------------      OBJECT      -----------------------------------------

# --> Object is the hysical existance of a class.
# --> We can created any number of objects for a class.
# --> SYNTAX to create object -->    referencevariable = classname()
# --> Example                 -->    s = Student()





# -------------------------      REFERENCE VARIABLE      -----------------------------------

# --> The variable is used to refer object is the reference variable.
# --> By using reference variables we can used dthe properties and methods of the objects for a class.
# -->program is the  "s1" in the below program is the reference variable.

# class Student:

#     def __init__(self,name,rollno,marks):            # This is constructor
        # self.name   = name                
#         self.rollno = rollno
#         self.marks  = marks
    
#     def talk(self):                                    # This is instance method
#         print("My name is : ",     self.name)
#         print("My roll no. is : ", self.rollno)
#         print("My marks are : ",   self.marks)

# s1 = Student("Durga", 101, 80)                         "s1" here is the reference variable
# s1.talk()





# ---------------------------     SELF  VARIABLE      -------------------------------

# --> "self" is the default variable which is always pointing to the current object.
# --> By using "self" we can access "intance variables" and "instance methods".
# --> "self" should be the first parameter inside the constructor.      --> def __init__(self)
# --> "self" should be the first parameter inside the instance methods. --> def talk(self)





# ----------------------   CONSTRUCTOR     __init__(self)      ----------------------------

# --> The main purpose of the constructor is to declare and initialize instance variables.
# --> self,name,rollno,marks are parameters inside constructor
# --> Contructor is optional. If we are not providing any constructor then Python will provide default constructor.



# *** Program to demonstrate Contructor will execute only once per object :


# class Test:

#     def __init__(self):
#         print("Contructor Execution...")

#     def m1(self):
#         print("Method Execution...")

# t1 = Test()
# t2 = Test()
# t1.m1()
# t2.m1()



# *** Program:


# class Student:

#     '''This is student class with required data'''
    
#     def __init__(self,x,y,z):
#         self.name = x
#         self.rollno = y
#         self.marks = z

#     def display(self):
#         print("Student Name: {}\nRoll No: {}\nMarks: {}".format(self.name, self.rollno, self.marks)) 

# s1 = Student("Durga", 101, 180)
# s1.display() 




# *** 1. Instance Variables :
# --> We can declare instance variables by inside :
# (a) Inside constructor by using "self variable".
# (b) Inside instance method by using "Self Variable" 
# (c) Outside of Class by using Object Reference Variables.


# class Test:

#     def __init__(self):
#         self.a = 20          # (a) Inside constructor by using "self variable"

#     def m1(self):
#         self.b = 30          # (b) Inside instance method by using "Self Variable"
    
# t = Test()
# t.m1()
# t.c=40                      # (c) Outside of Class by using Object Reference Variables.
# print(t.__dict__)



# *** How to access Instance Variables:

# class Test:

#     def __init__(self):
#         self.a=10
#         self.b=20
    
#     def display(self):
#         print(self.a)
#         print(self.b)

# t=Test()
# t.display()
# print(t.a, t.b)




# *** How to delete Instance Variable from the Object:


# class Test:

#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
    
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)

# t1=Test()
# t2=Test()

# del t1.c
# print(t1.__dict__)
# print(t2.__dict__)





# *** Changing Values of instance Variables:

# class Test:

#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
    
# t1=Test()
# t2=Test()

# t1.a=15
# t1.b=25
# t1.c=35

# print("t1: ", t1.a, t1.b, t1.c)
# print("t2: ", t2.a, t2.b, t2.c)





# ***  ---------------------------   (2).  STATIC VARIABLES     ------------------------------------

# --> Static variables doesn't varies from object to object.
# --> Static variables are declared directly in the class but outside of the methods.
# --> For total class only 1 copy of "static variable" will be created and shared by all objects of that class.
# --> We can access "static variables" either by class name or object reference. But recommended to used class name.
# --> "Instance Variables" v/s "Static Variables" : a separate copy will ve created for instance variables for every object , but in case of static variables for total class only 1 copy of will be created and can be shared by objects of that class.


# class Test:
#     x=10
    
#     def __init__(self):
#         self.y=20

# t1=Test()
# t2=Test()

# print("t1: ", t1.x, t1.y)
# print("t2: ", t2.x, t2.y)

# Test.x=15

# print("t1: ", t1.x, t1.y)
# print("t2: ", t2.x, t2.y)



# *** Various Places to declare static variables:
# --> within the class but from outside the mehod.
# --> inside "constructor" by using class name.
# --> inside "instance method" by using class name or cls variable.
# --> inside "static method" by using class name.


# class Test:
#     # a=10                                 # inside class but outside methods

#     def __init__(self):                    # Constructor
#         Test.b=20
    
#     def m1(self):                          # Instace Method
#         Test.c=30
    
#     @classmethod                           # We need to mention class method.
#     def m2(x):                             # Class Medthod, x is cls variable.
#         x.d1=40
#         Test.d2=400
    
#     @staticmethod                          # We need to mention static method.
#     def m3():                              # Static Medthod
#         Test.e=50
    
# print(Test.a)
# t=Test()
# print(Test.b)
# t.m1()
# print(Test.c)
# t.m2()
# print(Test.d1,Test.d2)
# t.m3()
# print(Test.e)
# Test.f=60                                 # outside the class by object reference.
# print(Test.f)



# ------------------------- accessing Static Variables : ------------------------------------


# class Test:
#     a=10

#     def __init__(self):
#         print("Constructor: ", self.a)
#         print("Constructor: ", Test.a)   
#     def m1(self):
#         print("Instance Method: ", self.a)
#         print("Instance Method: ", Test.a)
    
#     @classmethod
#     def m2(cls):
#         print("Class Method: ", cls.a)                               # cls is cls variable.
#         print("Class Method: ", Test.a)
#     @staticmethod
#     def m3():
#         print("Static Method: ", Test.a)
    
# t=Test()
# print("Class: ", Test.a)
# print("Calling Class by Object: ", t.a)
# t.m1()
# t.m2()
# t.m3()




# --------------------- modiyfying value of Static Variables : --------------------------------


# --> anywhere either within the class or outside the class we can modify the "static variable" by using classname.
# --> But indside "class method" the modification can also be done by using "cls variable.


# class Test:
#     a=777
    
#     @classmethod
#     def m1(cls):
#         cls.a=888
#         Test.b=10
        

#     @staticmethod
#     def m2():
#         Test.a=999
    
# print(Test.a)
# Test.m1()
# print(Test.a, Test.b)
# Test.m2()
# print(Test.a)





# class Test:
#     a=10
#     def m1(self):
#         self.a=20
# print(Test.a)
# t1=Test()
# print(t1.a)
# t1.m1()                 # We need to call the method here to get the changed value
# print(t1.a)



# class Test:
#     x=10
#     def __init__(self):
#         self.y=20
# t1 = Test()
# t2 = Test()
# # print(t1.x, t1.y)
# # print(t2.x, t2.y)

# Test.x=88
# t1.x=77
# t1.y=99
# print("t1:", t1.x, t1.y)
# print("t2:", t2.x, t2.y)




# class Test():
#     a=10
#     def __init__(self):
#         self.b=20
#     @classmethod
#     def m1(cls):
#         cls.a=100
#         cls.b=200
# t1=Test()
# t2=Test()
# t1.m1()
# print(t1.a, t1.b)
# print(t2.a, t2.b)
# print(Test.a, Test.b)





# --------------------- Deleting Static Variables of a CLASS --------------------------------

# --> Syntax anywhere except @classmethod is --> del classname.variablename
# --> Syntax inside the @classmethod is      --> del cls.variablename

# class Test():
#     a=10
#     @classmethod
#     def m1(cls):
#         cls.b=20
#         del cls.a
# t1=Test()
# # print(Test.__dict__)
# t1.m1()
# # print(Test.a, Test.b)        #This will give you error since static variable a is alredy deleted.
# print(Test.b)





# --> Example:

# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
#         del Test.a
#     def m1(self):
#         Test.c=30
#         del Test.b
#     @classmethod
#     def m2(cls):
#         cls.d=40
#         del Test.c
#         # del cls.c                 # here --> del cls.c   or  --> del Test.c    both will work
#     @staticmethod
#     def m3():
#         Test.e=50
#         del Test.d
# print(Test.__dict__)
# t=Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# t.m2()
# print(Test.__dict__)
# t.m3()
# print(Test.__dict__)
# Test.f=60
# print(Test.__dict__)
# del Test.e
# print(Test.__dict__)


# *** Note: 
# 1. By using object reference variable/self we can read static variables, but we cannot modfify or delete. 
# 2. If we are trying to modify, then a new instance variable will be added  to that particular object.      --> t1.a =70
# 3. If we are trying to delete we will get an error.


# class Test:
#     a=10
# t1=Test()
# # t1.a=70
# del t1.a
# print(t1.a)





# -------------    sys  Module    -------------------

# import sys
# # print(sys.copyright)
# # print(sys.executable)
# # print(sys.getrecursionlimit())
# # print(sys.setrecursionlimit(2000))              #we can set our own recursion limit.
# # print(sys.getrecursionlimit())                  # here it will display the set recursion limit
# # print(sys.getwindowsversion())                  # this will work in the Command Prompt
# # print(sys.base_exec_prefix)
# # print(sys.platform)                             # win 32
# print(sys.version)                                # This will give you the python version  

# --> The sys. exit() function allows the developer to exit from Python.

# To know more about "sys module" visit: https://docs.python.org/3/library/sys.html#module-sys






# *** We can modify or delete static variables by usiing "classname" or "class variable".


# import sys
# class Customer:
#     bankname = "DURGABANK"

#     def __init__(self,name,balance=0.0):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amt):
#         self.balance = self.balance + amt
#         print("Balance after deposit : ", self.balance)
#     def withdraw(self,amt):
#         if amt > self.balance:
#             print("Insufficient Funds... cannot perform this operation")
#             sys.exit()
#         self.balance = self.balance - amt
#         print("Balance after withdraw : ", self.balance)

# print("Welcome to: ",Customer.bankname)
# name = input("Enter your name: ")
# c=Customer(name)
# while True:
#     print("d-Deposit \nw-Withdraw \ne-Exit")
#     option = input("Choose your option: ")
#     if option=="d" or option=="D":
#         amt=float(input("Enter the amount: "))
#         c.deposit(amt)
#     elif option=="w" or option=="W":
#         amt=float(input("Enter the amount: "))
#         c.withdraw(amt)
#     elif option=="e" or option=="E":
#         print("Thank you for Banking wih us!")
#     else:
#         print("This is an invalid input!")





# ------------------------------ 3.  LOCAL  VARIABLES   --------------------------------

# --> We use Local variables for temporary requirements.
# --> Local variable will be created at the time of method excecution and will destroyed once method completes. 
# --> Local variables of a method cannot be used from outside of a method.


# class Test:
#     def m1(self):
#         a=1000
#         print(a)
#     def m2(self):
#         b=2000
#         print(b)
# t=Test()
# t.m1()
# t.m2()


# class Test:
#     def m1(self):
#         a=1000
#         print(a)
#     def m2(self):
#         # print(a)         # Local variables of a method cannot be used from outside of a method.
#         b=2000
#         print(b)
# t=Test()
# t.m1()
# t.m2()





# -------------------------    TYPES of METHODS    ----------------------------

# --> There are 3 types of Methods used in OOP´s :
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods


# 1. INSTANCE METHODS :

# --> Inside method implementation --- if we are using instance variables then such type of methods are instance methods.
# --> Inside instance method declariation we have to pass self variable.         def m1(self):
# --> By using self variable inside method we can access the instance variables.
# --> Within the Class we can call the Instance method by using the --- "self variable" and from outside of the class we can call the instance method by using the --- "Object Reference"


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Hello ", self.name)
#         print("Your marks are: ", self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print("You got First Grade!")
#         elif self.marks>=50:
#             print("You got Second Grade!")
#         elif self.marks>=35:
#             print("You got Third Grade!")
#         else:
#             print("You are Failed!")
# 
# n=int(input("Enter the number of students: "))                 # Outside the class.
# for i in range(n):
#     name=input("Enter Name: ")
#     marks=int(input("Enter Marks: "))
#     s=Student(name,marks)
#     s.display()
#     s.grade()
#     print()





# The same code can also be written without using "FOR LOOP":


# class Student:
    
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("Hello ", self.name)
#         print("Your marks are: ", self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print("You got First Grade!")
#         elif self.marks>=50:
#             print("You got Second Grade!")
#         elif self.marks>=35:
#             print("You got Third Grade!")
#         else:
#             print("You are Failed!")

# n=int(input("Enter the number of students: "))                   # Outside the class.
# name=input("Enter Name: ")
# marks=int(input("Enter Marks: "))
# s=Student(name,marks)
# s.display()
# s.grade()





# ---------------------    SETTER  and  GETTER  Methods     ---------------------------

# We can set and get values by using setter and getter methods



# *** (1) SETTER Method :
# --> Setter methods can be used to set the values of instance variables.
# --> Setter methods are also know as "Mutator Methods".

# --> Syntax:
#     def setVariable(slef,variable):
#         self.variable = variable

# --> Example:
#     def setName(self,name):
#         self.name = name


# *** (2) GETTER Method :
# --> Getter methods is used to get values of instance variables.
# --> Getter methods are also known as "Accessor Methods".

# --> Syntax:
#     def getVariable(self):
#         return self.name

# --> Example:
#     def getName(self,name):
#         return self.name



# Program:


# class Student:

#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name    
#     def setMarks(self,marks):
#         self.marks = marks
#     def getMarks(self):
#         return self.marks
    
# n = int(input("Enter the number of students: "))
# for i in range(n):
#     s = Student()
#     name = input("Enter Name: ")
#     s.setName(name)
#     marks = input("Enter Marks: ")
#     s.setMarks(marks)
#     print("Hi", s.getName())
#     print("Your Marks are: ", s.getMarks())
#     print()



# class Student:

#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name

# n = int(input("number of students:"))
# for i in range(n):
#     s=Student()
#     name=input("Enter the name: ")
#     s.setName(name)
#     print("Hi", s.getName())





# --(2)------------------------  CLASS  METHODS  -----------------------------

# --> Inside method implementation if we are using only the class variables (i.e static variables), then such type of methods are called as Class Methods.
# --> We can declare Class Methods explicitly (stating clearly) by mentioning @classmethod decorater.
# --> For Class Method we should provide cls variable at the time of declaration.
# --> We can call Class Method by using class-name or object reference variable. 


# class Check:
#     legs = 4
#     @classmethod
#     def walk(cls,name):
#         print("{} walk {} legs".format(name,cls.legs))
# # Check.walk("Dogs")
# s=Check()
# s.walk("Dogs")
# s.walk("Cats")




# -------------------    Tracking no. of Objects created for a Class:    ----------------------


# class Test:
#     count=0

#     def __init__(self):
#         Test.count = Test.count + 1
#     @classmethod
#     def m1(cls):
#         print("The no. of objects in Test class : ",cls.count)

# t1=Test()
# t2=Test()
# Test.m1()
# t3=Test()
# t4=Test()
# Test.m1()






# --(2)-------------------------     STATIC  METHODS     ------------------------------

# --> In general this methods are general utility methods.
# --> Here we do not use instance or class variables.
# --> Here we won't provide self or cls arguments at the time of declaration.
# --> We can declare "static method" explicitly by using @staticmethod decorator.
# --> We can access "Static Method" by using "classname" or "object reference".



# class Mathematics:    
#     @staticmethod
#     def add(x,y):
#         print("The sum is: ", x + y)
#     @staticmethod
#     def product(x,y):
#         print("The Product: ", x*y)    
#     @staticmethod
#     def average(x,y):
#         print("The average: ", (x+y)/2)
# Mathematics.add(10,20)
# Mathematics.product(10,20)
# Mathematics.average(10,20)



# *** Note:
# --> In general we can use only instance and static methods. Inside static we can access class level variables by using class names.
# --> Class Methods are most rarely used in Python.





# --------------------  Passing memebrs of one Class to another Class  -------------------- 

# --> We can access members of one to in another class.


# class Employee:

#     def __init__(self,eno,ename,esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
    
#     def m1(self):
#         print("Employee Number: ", self.eno)
#         print("Employee   Name: ", self.ename)
#         print("Employee Salary: ", self.esal)
        
# class Test:
    
#     def m2(abc):
#         abc.esal = abc.esal + 500
#         abc.m1()

# e = Employee(100, "Arif", 10000)
# Test.m2(e)



# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def m1(self):
#         print("a: ", self.a)
#         print("b: ", self.b)
# class c2:
#     def m2(x):
#         x.a=x.a+7
#         x.m1()
# s=c1(10,20)
# c2.m2(s)                  

# # y=c2
# # y.m2(s)





# ----------------------------    INNER CLASSES    ---------------------------


# --> Sometimes we can declare one class inside another class. Such type of classes are called "Inner Classes".
# --> Without existing one type of object if there is no chance of existing another type of object, then we should go for "Inner Classes"

# --> Syntax:
#     class Car:
#         .....
#         class Engine:
#         .....

# --> Example: Without existing University object there is no chance of existing Department object.
#     class University:
#         .....
#         class Department:
#         .....

# --> Example: Without existing of Human there is no chance of existing Head. Hence Head must be a part of Human.
#     class Human:
#         .....
#         class Head: 
#         .....

# --> Note: Without existing of the outer class object there is no chance of existing inner class object.
#           Hence inner class object is always associated with the outer class object.





# *** Demo Program-1


# class Outer:
#     def __init__(self):
#         print("Outer class object!")
#     def m1(self):
#         print("Outer class method!")
#     class Inner:
#         def __init__(self):
#             print("Inner class object!")
#         def m2(self):
#             print("Inner class method!")
# o=Outer()
# o.m1()
# i=o.Inner()
# i.m2()
# Outer().Inner().m2()              # This will not call m1






# *** Demo Program-2

# class Father:
# 	def __init__(self):
# 		self.name = "Arif Ali"
# 		self.db = self.Son()                # Son is the inner classname
# 	def m1(self):
# 		print("Name: ", self.name)

# 	class Son:
# 		def __init__(self):
# 			self.dd = 11
# 			self.mm = 5
# 			self.yy = 2020
# 		def m2(self):
# 			print("Son: {}-{}-{}".format(self.dd,self.mm,self.yy))

# p=Father()
# p.m1()
# x=p.db
# x.m2()




# *** Demo Program-3

# class Human:	
# 	def __init__(self):
# 		self.name = "Arif Ali"
# 		self.part = self.Head()
# 	def m1(self):
# 		print("Name: ", self.name)
# 	class Head:
# 		def __init__(self):
# 			self.age=26
# 		def m2(self):
# 			print("Age: ", self.age)
# x = Human()
# x.m1()
# y=x.Head()
# y.m2()




# *** Demo Program-4: Inside a class we can declare any number of "Inner Classes".


# class Human:
# 	def __init__(self):
# 		self.name="Arif Ali"
# 		self.head=self.Head()
# 		self.brain=self.Brain()
# 	def m1(self):
# 		print("Name: ", self.name)
# 	class Head:
# 		def __init__(self):
# 			self.a = "This is your head"
# 		def m2(self):
# 			print(self.a)
# 	class Brain:
# 		def __init__(self):
# 			self.b = "This is your brain"
# 		def m3(self):
# 			print(self.b)
# x=Human()
# x.m1()
# y=x.Head()
# y.m2()
# z=x.Brain()
# z.m3()			





# ------------------------    GARBAGE COLLECTION    ----------------------

# --> The main purpose of the Garbage Collecttion is to destroy useless objects to save memory.
# --> In an object does not have any reference variable then that object is eligible for "Garbage Collecttion".



# *** How to enable Garbage Collector?

# (1)       gc.isenabled()  -->  Returns True if GC is enabled
# (2)       gc.disable()    -->  To disable GC explicitly.
# (3)       gc.enable()     -->  To enable GC explicitly.

# import gc
# print(gc.isenabled())              # returns True
# gc.disable()                   
# print(gc.isenabled())              # returns False
# gc.enable()
# print(gc.isenabled())              # returns True




# *** DESTRUCTORS :

# --> Destructor is a special method and named as        __del__
# --> Just before destroying an object the Garbage Collector always calls destructor to perform clean up activities.
# --> Once destructor excecution completes then the Garbage Collector automatically destroys the object.


# import time
# class Test:	
# 	def __init__(self):
# 		print("Object initialization...")
# 	def __del__(self):
# 		print("Fulfilling last wish and performing clean up activities...")
# t1=Test()
# t2=None
# time.sleep(5)
# print("End of Application")




# import time
# class Test:	
# 	def __init__(self):
# 		print("Constructor Execution")
# 	def __del__(self):
# 		print("Destructor Execution")
# t1=Test()
# t2=t1
# t3=t2
# del t1
# time.sleep(5)
# print("Object is not yet destroyed after deleting t1")
# del t2
# time.sleep(5)
# print("Object is not yet destroyed after deleting t2")
# print("I am trying to delete the last reference variable")
# del t3




# import time
# class Test:	
# 	def __init__(self):
# 		print("Constructor Execution")
# 	def __del__(self):
# 		print("Destructor Execution")

# list=[Test(),Test(),Test()]
# del list
# time.sleep(5)                 # it defines that it will take minimum of 5 secs time to the output after this linetime.sleep(5).
# print("End of Application")





# ---------------  Finding the Number of References of an Object  -------------------


# import sys
# a = [1,2,3]                     #1st ref count towards a
# b=a                             #2nd ref count towards a
# c=b                             #3rd ref count towards a
# print(sys.getrefcount(a))       #4th ref count towards a


# import sys
# class Test:
# 	pass
# t1=Test()
# t2=t1
# t3=t1
# t4=t1
# print(sys.getrefcount(t1))       # ref count included towards t1 for this line.




# a=[1,2,3]
# b=a
# print(b)
# def


	




































