# myList = ['apple', 'banana', 'cherry']
# print(myList)

# myList = ['apple', 'banana', 'cherry', 'apply', 'banana']
# print(myList)
# print(len(myList))
# print(type(myList))

# newList = list(('apple', 'banana', 'cherry'))
# print(newList)

# myList = ['apple', 'banana', 'cherry', 'kiwi', 'melon', 'mango']
# print(myList[2])
# print(myList[-1])
# print(myList[1:3])
# print(myList[:3])
# print(myList[3:])
# print(myList[-4:-1])
# if "melon" in myList:
#     print("Yes, melon is in this list")


# list = ['apple', 'banana', 'cherry']
# list[1] = 'blackcurrant'
# print(list)
# list[1:3] = ['blackcurrant', 'watermelon']
# print(list)
# list[1:2] = ['blackcurrant', 'watermelon']
# print(list)
# list[0:2] = ['pinapple']
# print(list)
# list.insert(2, 'grape')
# print(list)
# list.append('kiwi')
# print(list)
# list.insert(1, 'kiwi')
# print(list)

# l = ['1', '2', '3','2','5','2']
# r = ['4', '5', '6']
# l.extend(r)
# print(l)

# r = ('10', '15')
# l.extend(r)
# print(l)
# l.remove('2')
# print(l)
# l.pop(4)
# l.pop()
# del l[3]
# del l
# l.clear()
# print(l)

# for x in l:
#     print(x)

# for x in range(len(l)):
#     print(l[x])

# l = ['1','20','30','120','64']
# i = 0
# while i < len(l):
#     print(l[i])
#     i = i + 1

# l = ['1','2','3','4','5']
# [print(x) for x in l]

# f = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# l = []
# for x in f:
#     if 'a' in x:
#         l.append(x)
# print(l)
# l = [x for x in f if "a" in x]
# print(l)
# l = [x for x in f if x != "apple"]
# print(l)
# l = [x for x in f]
# print(l)
# l = [x for x in range(10) if x < 5]
# print(l)
# print(range(10))
# r = range(1,6)
# x = list(r)
# print(x)
# print(list(range(0, 100, 10)))

f = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
l = [x.upper() for x in f]
print(l)
l = [x.upper() for x in f if len(x) < 6]
print(l)
l = ['Hello' for x in f]
print(l)
l = [x if x != "banana" else 'orange' for x in f]
print(l)

body = ['brain', 'eye', 'arm', 'cheek', 'back', 'face', 'finger']
body.sort()
print(body)

num = [100,1,25,326,59,28]
num.sort()
print(num)

body_2 = ['knee', 'hair', 'lip', 'heart', 'leg', 'hand']
body_2.sort(reverse = True)
print(body_2)

num_2 = [15, 29, 1, 187, 19, 3]
num_2.sort(reverse=True)
print(num_2)

l = ["Neck", 'stomach', 'tooth', 'Skeleton','wrist', 'Waist']
l.sort()
print(l)

l_1 = ["neck", 'Stomach', 'tooth', 'Skeleton', 'Wrist', 'waist']
l_1.sort(key = str.lower)
print(l_1)

l_2 = ["wrist", 'skeleton', 'Stomach','Waist', 'Lip', 'knee']
l_2.reverse()
print(l_2)

_List = ['wrist', 'lip', 'skeleton', 'waist', 'stomach', 'neck', 'knee']
_copy_list = _List.copy()
print(_copy_list)
print(_List)

_list_1 = ['knee', 'heart', 'neck', 'stomach', 'finget', 'waist', 'wrist']
new_list = list(_list_1)
print(new_list)

n_l = ['a','b','c']
s_l = [1,2,3]
# j_l = n_l + s_l
j_l = s_l + n_l
print(j_l)

ls = ['a', 'b', 'c']
ls1 = [1,2,3]
for x in ls1:
    ls.append(x)
print(ls)

u = ['f', 'g', 't']
i = [4,5,6]
i.extend(u)
print(i)