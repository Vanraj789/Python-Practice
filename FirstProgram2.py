print("Hello World")
name = "Vanraj"
age = "28"
print(name)
print(age)

name2 = "Jay"
age2 = "23"
print(name2)
print(age2)
is_adult = True

name3 = input("What is your name?")

print("Hello" + name3)

name4 = input("What is your superhero name?")
print("Hello" + name4)

old_age = input("Enter your old age : ")
int(old_age)
new_age = int(old_age) + 2
print(new_age)

number = 18
print(float(18))

first = input("Enter your first number: ")
second = input("Enter your second number: ")

sum = int(first) + int(second)
print("The sum is: " + str(sum))

name5 = "Vanraj Gadhavi"
print(name5.upper())

print(name5.find("m"))

print(name5.replace("G", "M"))
print("V" in name5)

print(5 // 2)
print(10 % 2)
print(5 + 2)
print(110 * 2)
print(5 ** 2)

i = 5
i = i + 2
i += 2
i -= 2
i *= 2

result = (2 + 3) * 5
print(result)

result2 = 2 + 3 * 5
print(result2)

# taking input



# calculating sum


print(3>2)

print(3 == 3)
print(3 != 3)

print(2>3 or 2>1)
print(2>3 and 1>0)
print(not 2>3)

age3 = 21

if age3 >= 18:
    print("You are an adult")
    print("You can vote")

elif age3 < 18 and age3 > 3:
    print("You are in school")

else:
    print("You are a child")

# mini project - calculator

first = input("Enter first number : ")
operator = input("Enter operator (+,-,*,/,%) : ")
second = input("Enter second number : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

elif operator == "%":
    print(first % second)

else:
    print("Invalid Operation")

numbers2 = range(5)
print(numbers2)

print(1)
print(2)
print(3)
print(4)
print(5)

i = 1
while i <= 5:
    print(i)
    i = i + 1

for item in range(6):
    print(item)

marks = [95, 98, 90, "maths"]
print(marks)
print(marks[0])
print(marks[0:2])

for score in marks:
    print(score)

marks.append(99)
print(marks)

marks.insert(1, 77)
print(marks)

print(45 in marks)

print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

students = ["ram", "kishan", "kuki", "puko", "pika"]

for student in students:
    if student == "puko":
        break;
    print(student)

for student in students:
    if student == "kuki":
        continue;
    print(student)

# Tuple

marks = (95, 97, 98, 98)

print(marks.count(98))

print(marks.index(97))

# set

marks = {95, 97, 98, 98}
print(marks)

for score in marks:
    print(score)

# dictionary

marks = {"english": 96, "chemistry": 98}
print(marks["english"])
marks["physics"] = 96;
print(marks)

marks["english"] = 60;
print(marks)

# Functions 1. In-Built Functions, 2. Module Functions, 3. User Defined Functions

int()
str()
bool()

import math
print(dir(math))

from math import sqrt
print(sqrt(16))

from math import *
print(sqrt())



def print_sum(first, second=55):
    print(first + second)

print_sum(1)











