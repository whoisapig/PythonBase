#!/usr/bin/python
# coding:utf-8

" 学生对象创建  __slts__"

__author__ = 'XiaoYang'

from types import MethodType


class Person(object):
    __slots__ = ('name', 'age')


class Student(Person):
    __slots__ = ("score")


# 子类对象能使用父类定义的 __slots__
S1 = Student()
S1.name = "Bail"

# __slots__ 只对对象有限制作用
Student.sex = "name"
