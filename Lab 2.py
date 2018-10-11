# a = [1,3,9,6,5]
# even = False
# for i in a:
#     if i % 2 == 0:
#         print ("The number is Even ", i)
#         even = True
#         break
#     else:
#         print("The number is Odd ", i )
#         break


#
# a = 'y'
# list = ['zain','hashir','hamza','noman']
# print( "Current list ",list)
# while a == 'y':
#     print("Enter String to insert in a list")
#     b = input()
#
#     print("Where do you nwant to insert your string")
#     c = int(input())
#
#     list.insert(c, b)
#
#     print("Do you want to insert another String (y/n)")
#     a = input()
#
#     if a == "n":
#         print(list)
#         break


# *********** TASK 1 *****************
# d = {"apple": 2, "orange": 4, "mango": 6}
# a = 0;
# for i in d:
#     a = a+d[i]
# print(a)



# *********** TASK 2 *****************
# from math import sqrt
#
# a = int(input("Enter a Number: "))
# dic = {}
# for r in range(1,a+1):
#     dic[r] = sqrt(r)
# print(dic)


# import math
# x = int(input('Enter the 1st Number '))
# y = int(input('Enter the 2nd Number '))
# op = input('Enter the operator')
#
# def add(x, y):
#     Answer = x + y
#     return Answer
#
# def sub(x, y):
#     Answer = x - y
#     return Answer
#
# def mul(x, y):
#     Answer = x * y
#     return Answer
#
# def div(x, y):
#     Answer = x / y
#     return Answer
#
# if (op=="+"):
#
#        print(add(x,y))
# if (op=="-"):
#
#        print( sub(x,y))
# if (op=="*"):
#
#        print(mul(x,y))
# if (op=="/"):
#
#        print(div(x,y))


# *********** TASK 3 *****************
# list = []
# print ("Enter a number: ")
# a = int(input())
#
# def square(x):
#     ans = x*x
#     return ans
#
# for i in range(1, a):
#     list.append(square(i))
#     print("The Square of ", i, " is ", square(i))



# *********** TASK 4 *****************
# class Shape():
#     def draw(self):
#         print("Draw")
#     def area(self):
#         print("Area")
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length = 23
#         self.width = 34
#
# class Triangle(Shape):
#     def __init__(self):
#         self.a = 2
#         self.b = 3
#         self.c = 4
#
#     def draw(self):
#         print("OVERRIDE DRAW")
#     def area(self):
#         print("OVERRIDE AREA")
#
#
# s = Shape()
# r = Rectangle()
# t = Triangle()
# s.area()
# s.draw()
# r.draw()
# t.draw()
# t.area()



# *********** TASK 5 *****************
a = input("Enter any String:")
# def rreverse(a):
#     if a == "":
#         return ""
#     else:
#         return rreverse(a[1:])+a[0]
# print("Answer: ",rreverse(a))