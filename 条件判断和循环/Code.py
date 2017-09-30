#!/usr/bin/python
#coding:utf-8-8


# 如果成绩达到60分或以上，视为passed。
#
# 假设Bart同学的分数是75，请用if语句判断是否能打印出 passed:
mark = 75
if mark >= 60:
    print ('passed')


# 如果成绩达到60分或以上，视为passed，否则视为failed。
#
# 假设Bart同学的分数是55，请用if语句打印出 passed 或者 failed:

score = 55
if score >= 60:
    print('passed')
else:
    print('failed')


# 如果按照分数划定结果：
#
#     90分或以上：excellent
#
#     80分或以上：good
#
#     60分或以上：passed
#
#     60分以下：failed
#
# 请编写程序根据分数打印结果。

score = 85
if score >=90:
    print('excellent')
elif score >= 80:
    print('good')
elif score >= 60:
    print ('passed')
else:
    print('failed')


# 班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：
#
# L = [75, 92, 59, 68]
#
# 请利用for循环计算出平均成绩。

L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum += score
print sum/4;

# 利用while循环计算100以内奇数的和。

sum = 0.0
x = 1;
while x <= 100:
    if (x%2) == 1:
        sum += x
    x += 1
print sum

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。

sum = 0.0
x = 1.0
n = 1
while True:
    sum += x
    x = x * 2
    if n > 19:
        break
    n += 1
print sum


# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2 == 0:
        continue
    sum = sum + x

print sum

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。

for x in range(1,9):
    for y in range(x+1,10):
        if y != 10:
            print str(x)+str(y)