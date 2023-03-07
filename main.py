from MyLib import is_numeric
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# first_name = "Ab"
# is_online = False
# name = input("What is your name? \n")
# date_of_birth = int(input("What year were you born? \n"))
# age = 2023 - date_of_birth
# description = f"you're {name} and you're {age} years old"
# print(description)

# course = "Geography"
# print(f"course starts with G: {course.lower().startswith('g')}")
# print(f"{course} has {len(course)} letters")
# print(course.lower().count("g"))  # returns count of sub str
# print(course.upper())  # transforms to upper case
# print(course.find('g'))  # returns index of character
# contains = "G" in course
# print(contains)

# x = 10
# x = x + 3
# x += 3
# print(x)

# price = 25
# if price > 25 or price > 3:
#     print("yes")
# else:
#     print("no")
# if 5 not in range(3):
#     print("yes")
# for i in range(10):
#     print(i)
# temp = 25
# if temp > 30:
#     print("it's a hot day")
#     print("Drink plenty water")
# elif temp < 30:
#     print("so cool")
# exercise using flow control to convert Kg to pound or pound to kg
# k to p = weight / 0.45, p to k = weight * 0.45
# i = 1
#     while i <= 10:
#         print(i)
#         i += 1
#  names = ["Ab", "Erna", "Samia"]
#     names.insert(0, "Udo")
#     names.append("Nk")
#     names.clear()
#     print(len(names))
def basics():
    numbers = range(0, 10, 2)


def sorted_list():
    initial_list = [1, 2, 4, -5, 7, 9, 3, 2]
    for i in range(len(initial_list)):
        for j in range(i + 1, len(initial_list)):
            if initial_list[i] > initial_list[j]:
                temp = initial_list[j]
                initial_list[j] = initial_list[i]
                initial_list[i] = temp

    print(initial_list)


# def add(x, y):
#     return x + y

def test(**args):
    s = 0
    for i in args:
        s += args[i]
    return s


def dict_test():
    dictionary = {"apple": 44, "cherry": 22, "avocado": 22}
    for key in dictionary.keys():
        if not key.startswith("a"):
            continue
        print(key)


def with_default_values(num=4):
    print(num)


def num_py_examples():
    a = np.array([1, 2, 3, 4])
    b = np.array([[1, 2, 4, 4], [3, 4, 0, 9]])
    # shape = (dimension, size)
    # print(b.shape[1])
    for i in np.arange(0, 10, 3):
        print(i)


if __name__ == '__main__':
    num_py_examples()
