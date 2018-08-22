#!/usr/bin/python
#coding:utf-8


# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。

L = []
for num in range(1,101):
    L.append(num*num)
print (sum(L))


# 请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
def square_of_sum(l):
    my_list = []
    for num in l:
        my_list.append(num * num )
    return sum(my_list)

print (square_of_sum([1, 2, 3, 4, 5]))
print (square_of_sum([-5, 0, 5, 15, 25]))


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

print (average())
print (average(1, 2))
print (average(1, 2, 2, 3, 4))


# map高级函数
def f(x):
    return x * x
r = map(f, [1,2,3,4])
print(list(r))

# reduce 高级函数
from functools import  reduce
def my_sum(x, y):
    return x + y
r = reduce(my_sum, [1,2,3,4])
print(r)

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0:1].upper() + name[-1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# 方法一
def prod(L):
    num = 1
    for x in L:
        num = num * x
    return num
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 方法二
def chengfa(x, y):
    return x * y
def prod2(L):
    return reduce(chengfa, L)
print('3 * 5 * 7 * 9 =', prod2([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def HuanYuan(L):
    num = 1.0
    if L == '.':
        return 0
    for a in range(1, int(L)):
        num = num * 10
    return L * 100 / num
def LeiJia(x, y):
    return x + y
def str2float(s):
    return reduce(LeiJia, list(map(HuanYuan, s)))

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    return n == int(str(n)[::-1])
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)


# 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)


# 闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
            print(ax)
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
# f()
# f()

# 闭包测试2

def createCounter():
    i=[0]
    def count():
        i[0]+=1
        return i[0]
    return count

fun = fun2 = createCounter()
print(fun())
print(fun())

# 匿名函数

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
