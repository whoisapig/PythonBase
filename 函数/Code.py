#!/usr/bin/python
#coding:utf-8


# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。

L = []
for num in range(1,101):
    L.append(num*num)
print sum(L)


# 请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
def square_of_sum(l):
    my_list = []
    for num in l:
        my_list.append(num * num )
    return sum(my_list)

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])


# 请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'

def greet(str = 'world'):
    print("Hello, %s" %(str))

greet()
greet('Bart')


# 可变平均数

def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    else:
        for num in args:
            sum += num
        return sum/len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)