# t = ('wrist','waist','heart','stomach','cheen','knee','neck')
# print(t)
# t1 = ('a','b','c','a','b','c')
# print(t1)
# print(len(t))
#
# t_1 = ('cheen',)
# print(type(t_1))
#
# t_2 = ('cheen')
# print(type(t_2))

# t_1 = ('a','b','c')
# t_2 = (1,2,3)
# t_3 = (True,False,True)
# t_4 = ('abc', 40, True)
# print(type(t_1), type(t_2), type(t_3), type(t_4))
#
# t = tuple(('a', 'b', 'c', 'd', 'e', 'f', 'g'))
# print(t)
# print(t[1])
# print(t[-1])
# print(t[2:6])
# print(t[:6])
# print(t[3:])
# print(t[-4:-1])
# print('c' in t)
# if 'c' in t:
#     print("caramba")
#
# g = ('a','b','c')
# h = list(g)
# h[1] = 'F'
# g = tuple(h)
# print(g)
#
# u = ('angry','boring','careful','dangerous','dreamy')
# y = ['happy','hungry','lovely']
# i = list(u)
# i.append('excited')
# i.insert(2, 'glad')
# i.extend(y)
# u = tuple(i)
# print(u)
#
# r = ('hungry','angry','lovely','boring','dreamy')
# e = ('happy','careful','dangerous','existed')
# r += e
# print(r)

# t = ('dangerous', 'hungry', 'excited')
# l = list(t)
# l.remove('hungry')
# t = tuple(l)
# print(t)
#
# t_1 = ('stomach', 'head', 'nous', 'wrist', 'waist')
# del t_1
# # print(t_1) - викличе помилку так як змінну видалили
#
# fruits = ('apple', 'banana', 'cherry')
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# t_1 = ('stomach', 'head', 'nous', 'wrist', 'waist')
# (one, two, *three) = t_1
# print(three)
# print(one)
# print(two)
#
# t = ('1','2','3','4','5','6')
# (one, *two, three) = t
# print(one)
# print(two)
# print(three)


# l = ('dangerous','fany','happy','carу','careful')
# for x in l:
#     print(x)

# l = ('angry', 'hungry', 'boring', 'excited')
# for x in range(len(l)):
#     print(l[x])

i = ('1','2','3','4','5')
t = 0
while t < len(i):
    print(i[t])
    t += 1


a = ('f','d','g')
b = (1,2,3)
c = a + b
print(c)

y = ('t','r','e','r','a','a','g','l','r')
u = y * 2
print(u)
o = y.count("r")
print(o)
print(y.index("e"))

























