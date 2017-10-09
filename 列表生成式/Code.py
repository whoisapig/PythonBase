#!/usr/bin/python
#coding:utf-8-8


# 请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
#
# 提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]

print [x * (x+1) for x in range(1,100,2)]


# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
#
# 提示：
#
# 1. isinstance(x, str) 可以判断变量 x 是否是字符串；
#
# 2. 字符串的 upper() 方法可以返回大写的字母。

def toUppers(L):
    return [s.upper() for s in L if isinstance(s,str)]

print toUppers(['Hello', 'world', 101])


# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

print [int(str(x)+str(y)+str(z)) for x in range(1,10) for y in range(0,10) for z in range(1,10) if x == z ]