# class Demo:
#     def myFunction(self):
#         print("This is myFunction of class...")


#     def show(self, name):
#         print("Value is", name)
# d1 = Demo()
# d1.myFunction()
# d1.show('Shobit')



# example 2

# class myClass:
#     def func1(self, n1,n2):
#         ans = n1+ n2
#         print(ans)

# m1 = myClass()
# m1.func1(2, 3)

# constructor  

# class Demo:
#     def myFunction(self):
#         print("This is myFunction of class...")


#     def show(self, name):
#         print("Value is", name)


#     def __init__(self): # constructor
#         print("This is demo class")
# d1 = Demo()
# d1.myFunction()
# d1.show('Shobit')


# parameter constructor
# class Demo:
#     def myFunction(self):
#         print("This is myFunction of class...")


#     def show(self, name):
#         print("Value is", name)


#     def __init__(self, nm): # constructor
#         print("This is demo class")
#         print()


# d1 = Demo()
# d1.myFunction()
# d1.show('Shobit')

# class Demo():
#     name = ""

#     def func1(self):
#         print("this is normal method")

#     def func2(self, name):
#         self.name = name

#     def show(self):
#         print("name is  ",self.name)

    
# d1  = Demo()
# d1.func1()
# d1.func2("Shobit")
# d1.show()





#Inheritance

#class subClass

# 1. single level 
# 2. Multi level



# single level inheritance

# class Demo:
#     def __init__(self):
#         print("This is parent class const")
#     def func1(self):
#         print("This is parent class")

# class Demo1(Demo):
#     def __init__(self):
#         print("This is child class const")
#     def func2(self):
#         print("This is child class")

# d1 = Demo1()
# d1.func1()
# d1.func2()


# Multilevel inheritanc

# class Demo:
#     def __init__(self):
#         print("This is parent class const")
#     def func1(self):
#         print("This is parent class")

# class Demo1(Demo):
#     def __init__(self):
#         print("This is child class const")
#     def func2(self):
#         print("This is child class")

# class Demo2(Demo1):
#     def func3(self):
#         print("this is third child class")

# d1 = Demo2()
# d1.func1()
# d1.func2()
# d1.func3()


# Multiple parent inheritance

# class Demo:
#     def __init__(self):
#         print("This is parent class const")
#     def func1(self):
#         print("This is parent class")

# class Demo1(Demo):
#     def __init__(self):
#         print("This is child class const")
#     def func2(self):
#         print("This is child class")

# class Demo2(Demo1):
#     def func3(self):
#         print("this is third child class")

# d1 = Demo2()
# d1.func1()
# d1.func2()
# d1.func3()

# overriding
class Demo:
    def func1(self):
        print("this is Demo class..")


class Demo1(Demo):
    def func1(self):
        print("this is Demo1 class..")

d1 = Demo1()
d1.Demo()




