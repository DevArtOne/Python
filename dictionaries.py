# d = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(d)
# print(d['brand'])

# d = {
#     'brand':'Ford',
#     'model':'Mustang',
#     'year':1964,
#     'year':1985
# }
# print(d)
# print(len(d))

# d = {
#     'brand':'Ford',
#     'electric':False,
#     'year':1964,
#     'color': ['red','white','blue']
# }
# print(d)
# print(type(d))

# d = dict(name = 'John', age = 35, country = 'Norway')
# print(d)
# print(d["name"])
# print(d.get('age'))
# print(d.keys())

# d = {
#     'brand':'Ford',
#     'model':'Mustang',
#     'year':1943
# }
# a = d.keys()
# print(a)
# d['color'] = 'white'
# print(a)
# # print(d.values())
#
# d1 = {
#     'car':'mazda',
#     'model': 6,
#     'year':2010
# }
# b = d1.values()
# print(b)
# d1['year'] = 2013
# print(b)

# f = {
#     'thing':'fruit',
#     'type':'mango',
#     'color':'red'
# }
# v = f.values()
# print(v)
# f['weight'] = 15
# print(v)
# print(f)
# print(f.items())

# car = {
#     'brand': 'ferrari',
#     'year': 1963
# }
# x = car.items()
# print(x)
# car['year'] = 2022
# car['clor'] = 'blue'
# print(x)
#
# if 'brand' in car:
#     print('Yes')

# man = {'name': 'Kevin', 'age': 49}
# man['age'] = 32
# man.update({"name":"Jack"})
# print(man)
#
# number = {
#     'num_1':23,
#     'num_2':54,
#     'num_3':12
# }
# number['num_4'] = 47
# number.update({'num_5':98})
# print(number)
#
# number.pop('num_1')
# print(number)
#
# number.popitem()
# print(number)
#
# del number['num_3']
# print(number)
#
# number.clear()
# print(number)

# d = {
#     'num_1':'87',
#     'num_2':'70',
#     'num_3':'12'
# }
# for x in d:
#     print(x)
#
# for y in d:
#     print(d[y])
#
# for u in d.values():
#     print(u)
#
# for f in d.items():
#     print(f)

# d = {
#     'car':'audi',
#     'fruit':'kiwi',
#     'sport':'swimming'
# }
#
# d_1 = d.copy()
# print(d_1)
#
# d_2 = dict(d)
# print(d_2)


# family = {
#     'child_1':{
#         'name':'Emil',
#         'year':2004
#     },
#     'child_2':{
#         'name':'Tobias',
#         'year':2007
#     },
#     'child_3':{
#         'name':'Linus',
#         'year':2011
#     }
# }
# print(family)

# child_1 = {
#     'name' : 'Emil',
#     'year' : 2004
# }
# child_2 = {
#     'name' : 'Tobias',
#     'year' : 2007
# }
# child_3 = {
#     'name' : 'Linus',
#     'year' : 2011
# }
# family = {
#     'child_1' : child_1,
#     'child_2' : child_2,
#     'child_3' : child_3
# }
# print(family)
# print(family['child_3']['name'])
# print(family['child_2']['year'])
#
# b = family.get('child_1')
# print(b)
# x = ('num1','num2','num3')
# y = 0
# d = dict.fromkeys(x, y)
# print(d)
















