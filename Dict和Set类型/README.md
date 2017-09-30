## Dict和Set类型

### Python之什么是dict

```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
```

我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。


花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。

由于dict也是集合，len() 函数可以计算任意集合的大小：

### Python之访问dict

```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

print (d['Adam'])
print (d.get('Adam'))
```

判断key是否存在

```
if 'Paul' in d:
    print d['Paul']
```


### Python中dict的特点

dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都是一样的。而list的查找速度回随着元素的增加而逐渐下降。

不过dict的查询速度快并不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按照key查找的，所以在dict中，key是不能重复的；

dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：

```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

>>> print d
{'Lisa': 85, 'Adam': 95, 'Bart': 59}
```

dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。


### Python 更新dict

```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d['Paul'] = 72
```

### Python 中什么是set

dict的作用是建立一组key和一组value的映射关系，dict的key是不能重复的

```
s = set(['A', 'B', 'C'])
>>> print s
set(['A', 'C', 'B'])
```
请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能是不同的，因为set内部存储的元素是无序的。

因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list 会怎么样呢？

```
>>> s = set(['A', 'B', 'C', 'C'])
>>> print s
set(['A', 'C', 'B'])
>>> len(s)
3
```


### Python 之访问set

```
s = set(['A', 'B', 'C'])

print 'A' in s
```


### Python之遍历set

由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。

直接使用 for 循环可以遍历 set 的元素：

```
>>> s = set(['Adam', 'Lisa', 'Bart'])
>>> for name in s:
...     print name
...
Lisa
Adam
Bart
```

### Python之更新set

由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：

- 把新的元素添加到set中；
- 把已有元素从set中删除；

添加元素时，用set的add()方法：
```
s = set([1,2,3])
s.add(4)
print(s)
```
当添加的元素已经存在，add()不会报错，但是也不会添加进去

```
s = set([1,2,3])
s.add(3)
print(s)
```
删除set中的元素时，用set的remove()方法
```
s = set([1,2,3])
s.remove(2)
print(s)
```


