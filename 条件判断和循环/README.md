# Python条件判断和循环

## Python之if语句

```
age = 20
if age > = 18:
    print ('your age is',age)
    print 'adult'
print 'END'

```
注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。

缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。

注意: if 语句后接表达式，然后用:表示代码块开始。

## Python 之if-else

```
age = 18
if age >= 18:
    print 'adult'
else:
    print 'teenager'
```

注意：else 后面跟的也是个 ':'


## Python 之if-elif-else

```
age = 5
if age >= 18:
    print 'adult'
elif age >= 6:
    print('teenager')
elif age >= 3:
    print('kid')
else:
    print('baby')

```
elif 意思就是 else if。

特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。


## Python之for循环

```
L = ['Adam','List','Bart']
for name in L:
    print name
```

注意:  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。

## Python 之while循环

```
N = 10
x = 0
while x < N:
    print x
    x = x + 1
```

和 for 循环不同的另一种循环是 while 循环，while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。

while循环每次先判断 x < N，如果为True，则执行循环体的代码块，否则，退出循环。


## Python 之 break退出循环

```
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
```

用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。