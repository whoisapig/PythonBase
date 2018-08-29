#!/usr/bin/python
# coding:utf-8

" 枚举"

__author__ = 'XiaoYang'

from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return "Type is Object;Name is Student"

    def __getattr__(self, attr):
        return "%s 属性不存在" % (attr)


# 测试:
bart = Student('Bart', Gender.Male)
print(bart)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
