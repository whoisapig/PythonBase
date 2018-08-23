#!/usr/bin/python
# coding:utf-8

" 学生对象创建  "

__author__ = 'XiaoYang'

from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


S1 = Student()
S2 = Student()

# # 给对象赋值要给函数属性
# S1.set_age = MethodType(set_age, S1)
# S1.set_age(10)
# print(S1.age)

# 给类class赋值赋值一个函数属性
Student.set_age = set_age
S1.set_age(10)
print(S1.age)
