# set = {"large",'long','short','small','low','narrow'}
# print(set)
# s = {'1','1','1'}
# print(s)
#
# mS = {1, 'tall', '4', True, 2}
# print(mS)
#
# setM = {'1', False, 'dangerous', 0}
# print(setM)
# print(len(setM))
#
# s_1 = {'narrow', 'tall', 'small', 'large', 'short', 'long'}
# s_2 = {1,2,3,4,5}
# s_3 = {True, False,False}
# print(type(s_1))
# print(type(s_2))
# print(type(s_3))
#
# ss = {"one", 1, False}
# for x in ss:
#     print(x)
#
# ms = {1,2,3,4,5}
# ms.add(8)
# print(ms)
# sE = (3 in ms)
# print(sE)
#
#
# sT = {"long",'short','tall','small','norrow','wide'}
# sN = {1,2,3,4,5,}
# l = ['apple','grape','kiwi']
# # sT.update(sN)
# # print(sT)
# sT.update(l)
# sT.remove('short')
# sT.discard('small')
# print(sT)

# p = {'1','2',"3"}
# k = p.pop()
# print(k)
# print(p)
#
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset) #the set after removal
#
#
# pol = {'car','bus','plane','tram','train'}
# del pol
# print(pol)

# pol = {'car','bus','plane','tram','train'}
# for f in pol:
#     print(f)

# ss = {'car','waist',5}
# nn = {2,3,4}
# k = ss.union(nn)
# print(k)
#
# s = {False, 2, 'wrist'}
# sN = {True, 5, 'car'}
# sN.update(s)
# print(sN)

a = {"car",'foot','glasses','trousers'}
b = {'shorts','gloves','trousers','foot'}
# c = a.copy()
# c = a.difference(b)
# a.difference_update(b)
# c = a.intersection(b)
# a.intersection_update(b)
# b.symmetric_difference_update(a)
# c = a.intersection(b)
# c = a.isdisjoint(b)
# c = a.issubset(b)
c = a.issuperset(b)
# print(a)
# print(c)
# print(b)
print(c)