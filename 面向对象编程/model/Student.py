#!/usr/bin/python
# coding:utf-8

" 学生对象创建"

__author__ = 'XiaoYang'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 90)
bart.score = 80
bart.say = "hello world"
print(bart.say)
# bart.print_score()
# lisa.print_score()
