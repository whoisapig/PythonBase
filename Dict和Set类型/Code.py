#!/usr/bin/python
#coding:utf-8

# 根据如下dict：
#
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# 请打印出：
#
# Adam: 95
# Lisa: 85
# Bart: 59

d = {
    'Adam':95,
    'Lisa':85,
    'Bart':59
}
for (key,value) in d.items():
    print ("%s:%s" %(key,value))



# 请设计一个dict，可以根据分数来查找名字，已知成绩如下：
#
# Adam: 95,
#
# Lisa: 85,
#
# Bart: 59.

# d = {
#     'Adam':95,
#     'Lisa':85,
#     'Bart':59
# }
#
# score = input('请输入成绩：')
# classMate = ""
# for (key, value) in d.items():
#     if value == score:
#         classMate = key
#         break
# if classMate == "":
#     print("没有找到该同学")
# else:
#     print("%s : %s" %(classMate,score))


# 请用set表示班里的4位同学：
#
# Adam, Lisa, Bart, Paul
s = set(['Adam','Lisa','Bart','Paul'])
print s

# 月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。
#
# 月份可以用字符串'Jan', 'Feb', ...表示。

inputMonth = 'Jan'
month = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])
if inputMonth in month:
    print("Month is OK")
else:
    print('Month is not OK')

#
# 请用 for 循环遍历如下的set，打印出 name: score 来。
#
# s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

s = set([('Adam', 95,1), ('Lisa', 85,2), ('Bart', 59,1)])
for (key,value,x) in s:
    print key
    print value
    print x

l = ['Adam','Lisa','Bart']
for key in l:
    print key


# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
#
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print(s)