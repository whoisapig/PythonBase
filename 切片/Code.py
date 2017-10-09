#!/usr/bin/python
#coding:utf-8-8

# range()函数可以创建一个数列：
#
# >>> range(1, 101)
# [1, 2, 3, ..., 100]
# 请利用切片，取出：
#
# 1. 前10个数；
# 2. 3的倍数；
# 3. 不大于50的5的倍数。

L = range(1,101)
print L[:10]
print L[2::3]
print L[4:50:5]



# 利用倒序切片对 1 - 100 的数列取出：
#
# * 最后10个数；
#
# * 最后10个5的倍数。

L = range(1,101)
print L[-10:]
print L[-46::5]


# 字符串有个方法 upper() 可以把字符变成大写字母：
#
# >>> 'abc'.upper()
# 'ABC'
# 但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
#
# 提示：利用切片操作简化字符串操作。

def firstCharUpper(s):
    if len(s) > 0 :
        return s[:1].upper()+s[1:]
    return s

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')