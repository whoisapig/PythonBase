#!/usr/bin/python
# coding:utf-8

" 学生对象创建 私有属性"

__author__ = 'XiaoYang'


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def print_gender(self):
        print('%s %s' % (self.__name, self.__gender))

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
