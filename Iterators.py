# myTuple = ('apple', 'cherry', 'banana')
# myIter = iter(myTuple)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
#
#
# myStr = 'banana'
# my_itr = iter(myStr)
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))
# print(next(my_itr))


# myTuple = ('apple', 'banana', 'cherry')
# for x in myTuple:
#     print(x)

# myStr = 'banana'
# for x in myStr:
#     print(x)


# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumber()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumber()
# myiter = iter(myclass)
# for x in myiter:
#     print(x)




































