#!/usr/bin/python
# coding:utf-8-8

# try:
#     print('try is running')
#     num = 10 / 0
#     print ("result: is %s" %(num))
# except ZeroDivisionError as e:
#     print('except is running;this error is %s' %(e))
# finally:
#     print('finally is running')
# print('end')


from functools import reduce
import logging


def str2num(s):
    try:
        return int(s)
    except ValueError as v:
        logging.exception("类型转换出bug")
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
