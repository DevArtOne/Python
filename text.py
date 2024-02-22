# print("hello")

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua"""
# print(a)
#
# a_a = "Hello World"
# print(a_a[9])

# for x in "banana" :
#     print(x)

# x = "Hello, World"
# print(len(x))

# txt = 'The best thing in the life are free'
# if "free" in txt:
#     print("yes, 'free' is present")

# txt = "The best thing in the world are free"
# print('best' not in txt)

# txt = "The expensive thing in the world are free"
# if "expensive" not in txt:
#     print("No, 'expensive' is not present in txt ")
# else:
#     print("Yes, 'expensive' is present in txt")

# b = "Hello World"
# print(b[2:5],b[7:9])
#
# text = 'The expensive thing in the world are free'
# print(text[:15])
# text = 'The expensive thing in the world are free'
# print(text[15:])

# t = "Hello, World"
# print(t[-5:-2])

# t = "Hello, World"
# print(t.upper())

# t = "Hello, World"
# print(t.lower())

# t = " Hello, World "
# print(t.strip())

# t = "Hello, World"
# print(t.replace("l", "k"))

# t = "Hello, World"
# print(t.split(","))

# a = "Hello "
# b = "Artem"
# c = a + b
# print(c)

# age = 30
# txt = "My name is Artem, I'm {}."
# print(txt.format(age))

# quantity = 3
# itemno = 574
# price = 43.1
# myOrder = "I want {} pieces of item {} for {} dollars"
# print(myOrder.format(quantity, itemno, price))

# quantity = 3
# itemno = 456
# price = 23.4
# myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"
# print(myOrder.format(quantity, itemno, price))

# txt = "\123\311"
# print(txt)

t = "Hello World and my friend \nWelcome"
myTuple = "John, Peter, Vicky"
txt = {87: 83}
n = '2'
# t = "hello world"
# t = "   "
# t = "\u0030"
# first = 1
# print(t.capitalize())
# print(t.casefold())
# print(t.center(0))
# print(t.count('l'))
# print(t.encode())
# print(t.endswith('l'))
# print(t.expandtabs(30))
# print(t.find('o'))
# print(t.format(first))
# print(t.index("l"))
# print(t.isalnum())
# print(t.isalpha())
# print(t.isascii())
# print(t.isdecimal())
# print(t.isdecimal())
# print(t.isidentifier())
# print(t.islower())
# print(t.isnumeric())
# print(t.isprintable())
# print(t.isspace())
# print(t.istitle())
# print(t.isupper())
# print("<>".join(myTuple))
# print(t.ljust(30),"and my friends")
# print(t.lower())
# print(t.lstrip())
# print(t.translate(t.maketrans("H", "M")))
# print(t.partition("and"))
# print(t.replace("World", "Galaxy"))
# print(t.rfind('friend'))
# print(t.rjust(30),'aaaaa')
# print(t.rpartition('and'))
# print(myTuple.rsplit(','))
# print(t.rstrip() + myTuple)
# print(myTuple.split(','))
# print(t.splitlines())
# print(t.startswith('Hello'))
# print(t.strip())
# print(t.swapcase())
# print(t.title())
# print(t.translate(txt))
# print(t.upper())
# print(n.zfill(10))

a = 'I love'
b = 'apple'
result = f'{a} {b}'
print(result)

print(dir(result))