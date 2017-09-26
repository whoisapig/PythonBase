#!/usr/bin/python
#coding:utf-8-8

# 假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
list = ["Adam",95.5,"Lisa",85,"Bart",59]
print list

# 三名同学的成绩可以用一个list表示：
# L = [95.5, 85, 59]
# 请按照索引分别打印出第一名、第二名、第三名，同时测试 print L[3]。
list =[95.5, 85, 59]
print list[0]
print list[1]
print list[2]

# 上题倒叙
list =[95.5, 85, 59]
print list[-1]
print list[-2]
print list[-3]

# 假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
list = ['Adam', 'Lisa', 'Bart']
list.insert(-1,"Paul")
print list

# 班里的同学按照分数排名是这样的：
#
# L = ['Adam', 'Lisa', 'Bart']
#
# 但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。
#
# 请通过对list的索引赋值，生成新的排名。

L = ['Adam', 'Lisa', 'Bart']
classMate = L[-1]
L[-1] = L[-3]
L[-3] = classMate
print L


# 创建一个tuple，顺序包含0 - 9这10个数。
t = (0,1,2,3,4,5,6,7,8,9)
print t