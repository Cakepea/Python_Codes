# -*- coding: utf-8 -*-
"""Computer Homework 1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h73IEJG7A8gImtkGhqLG5uS9PUtSEp56
"""

First 50 even numbers

start, end= 1,51

for num in range(start,end+1):
   if num % 2 == 0:
        print(num, end = " ")

Multiplication table for 17

num=17

for i in range(1,11):
  print(num, 'x', i, '=', num*i)

Factorial of a number n

num= int(input("enter a number: "))
for i in range(1, num+1):
 fac=fac*1
print("factorial of ", num, " is ", fac)