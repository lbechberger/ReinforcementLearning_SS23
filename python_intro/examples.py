# print a string
print("Hello world")

# dynamic typing & data types
i = 5
print(i, type(i))
s = "Hello world!"
print(s, type(s))
f = 3.1516
print(f, type(f))
b = True
print(b, type(b))

# type conversion
x = 10.3
print(x, type(x))
print(int(x), type(int(x)))
y = "2.5"
print(y, type(y))
print(float(y), type(float(y)))

# lists
empty_list = []
string_list = ["a", "b", "c"]
int_list = [1, 2, 3]
mixed_list = [1, "a", True, 3.5]

# list operations
my_list = [1,2,3,4]
my_list.append(42)
print(len(my_list))
print(0 in my_list)
print(1 in my_list)

# list indexing
indexing_list = [1,2,3,2,4,1]
print(indexing_list[2])
print(indexing_list[:4])
print(indexing_list[4:])
print(indexing_list[-1])
print(indexing_list[-3:])

# strings
s1 = "Hello"
s2 = 'Hello'
print(s1 == s2)
s3 = """Multi-
line string"""
print(s3)
print(s3[0], s3[:3], len(s3))
# f-strings
answer = 42
print(f"The answer to life, universe, and the rest is {answer}")

# reading input
name = input("What's your name? ")
print(f"Hello, {name}! :-)")

# --> Task 1 <--

# conditional statements
x = [1,2,3]
if len(x) > 3:
    print("long list")
elif 1 in x:
    print("list contains one")
else:
    print("default case")

# for loops
for i in [1,2,3]:
    print(i)

x = [2,2,2]
for idx, number in enumerate(x):
    print(f"number {number} at index {idx}")

for i in range(5):
    print(i)

for i in range(100,0,-10):
    print(i)

# while loops
n = 1
while n < 10000:
    print(n)
    n *= 3

# do-while loops
n = 1
while True:
    print(n)
    n *= 3
    if n >= 10000:
        break

# --> Task 2 <--

# functions
def multiply(x,y):
    z = x * y
    return z
print(multiply(6,7))

# classes and objects
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

fido = Dog("Fido")
fido.add_trick("roll over")
buddy = Dog("Buddy")
buddy.add_trick("play dead")

print(fido.tricks)
print(buddy.tricks)

# inheritance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self._graduation_year = year

student = Student("Aiman", "Abdallah", 1999)
student.printname()

# --> Task 3 <--

# sets
set_1 = {"apple", "banana", "cherry"}
set_1.add("orange")
print("banana" in set_1)
set_1.remove("banana")
print(set_1)
set_2 = {"banana", "apple"}
set_3 = set_1.union(set_2)
print(set_3)

# dictionaries
dict_1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict_1["model"]
print(x)
dict_1["year"] = 2018
dict_1["color"] = "red"
print(dict_1)
print("model" in dict_1)

# lambda functions
list_1 = [1, 5, 10, 20]
list_2 = map(lambda x: x/2, list_1)
print(list(list_2))
list_3 = list(filter(lambda x: x > 5, list_1))
print(list_3)

# list comprehensions
list_1 = [1, 2, 3]
list_plus_one = [x+1 for x in list_1]
print(list_plus_one)

list_filtered = [x + 1 for x in list_1 if x > 1]
print(list_filtered)

celsius = [39.2, 36.5, 37.3]
fahrenheit = [(9/5) * x + 32 for x in celsius]
for c, f in zip(celsius, fahrenheit):
    print(f"{c} degrees Celsius = {f} degrees Fahrenheit")

# --> Task 4 <--
