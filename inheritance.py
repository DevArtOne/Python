# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def full_name(self):
#         print(self.fname, self.lname)
# x = Person('John', 'Piston')
# x.full_name()
#
# class Student(Person):
#     pass
# x = Student("Mike", "Spike")
# x.full_name()


# class f_car():
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#     def fatherCar(self):
#         print(self.model, self.year)
# x = f_car('Mazda CX-5', '2019')
# x.fatherCar()
#
# class chl_car(f_car):
#     def __init__(child, model, year):
#         child.model = model
#         child.year = year
#     def childrenCar(kids):
#         print(kids.model, kids.year)
# y = chl_car('Opel omega', '2004')
# y.childrenCar()


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
# x = Student('Mile', 'Olsen')
# x.printName()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstName = fname
#         self.lastName = lname
#     def printName(self):
#         print(self.firstName, self.lastName)
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
# x = Student('Myke', 'Tyson')
# x.printName()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstName = fname
#         self.lastName = lname
#     def printName(self):
#         print(self.firstName, self.lastName)
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
# x = Student('Myke', "Olsen", 2019)
# x.printName()
# print(x.graduationyear)


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
#     def welcome(self):
#         print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)
# x = Student('Myke', 'Olsen', 2019)
# x.welcome()


















