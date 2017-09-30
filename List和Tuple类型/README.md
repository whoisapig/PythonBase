## List和Tuple类型

### Python创建list

Python内置的一种数据类型是列表：list 。

list是一种有序的集合，可以随时添加和删除其中的元素。


构造list非常简单，按照上面的代码，直接用 [ ] 把list的所有元素都括起来，就是一个list对象。通常，我们会把list赋值给一个变量，这样，就可以通过变量来引用list：

```
 classmates = ['Michael', 'Bob', 'Tracy']
```

### Python按照索引访问list

集合中每个元素都有对应的一个角标，通过指定角标可以获取指定的元素;如:

```
 >>> L = ['Adam', 'Lisa', 'Bart']
 >>> print L[0]
 Adam
```
注意：索引从0开始，也就是说，第一个元素的索引是0；


### Python之倒叙

```
 >>> L = ['Adam', 'Lisa', 'Bart']
 >>> print L[-1]
 Bart
```
注意：索引倒取，从-1开始；-1就是倒数第一个；-2就是倒数第二个；


### Python之添加新元素

append()总是把新的元素添加到list的尾部

```
>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.append('Paul')
>>> print L
['Adam', 'Lisa', 'Bart', 'Paul']
```

insert()方法，它接受两个参数，第一个参数是索引，第二参数是待添加的新元素:

```
>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.insert(0, 'Paul')
>>> print L
['Paul', 'Adam', 'Lisa', 'Bart']
```

### Python从list删除元素

pop()方法默认删掉list的最后一个元素，并且它还返回这个元素。

```
>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L.pop()
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
```
pop()方法有个参数，删除元素的角标；
```
>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L.pop(-2)
'Bart'
>>> print L
['Adam', 'Lisa', 'Paul']
```

### Python中替换元素

```
>>> L = ['Adam', 'Lisa', 'Bart']
>>> L[2] = 'Paul'
>>> print L
L = ['Adam', 'Lisa', 'Paul']
```

### Python之创建tuple

tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。


创建tuple 使用（）

```
>>> t = ('Adam', 'Lisa', 'Bart')
```

注意：()既可以表示tuple,也可以作为括号表示运算时候的优先级；所以Python规定，单元素tuple要多加一个逗号","；目的是为了避免歧义；但是打印tuple的时候Python会自动去掉最后一个"，"


### Python 之"可变"的tuple

前面我们看到了tuple一旦创建就不能修改。现在，我们看一个“可变”的tuple

```
>>> t = ('a', 'b', ['A', 'B'])
>>> L = t[2]
>>> L[0] = 'X'
>>> L[1] = 'Y'
>>> print t
('a', 'b', ['X', 'Y'])
```

tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
