## 面向对象高级编程

#### 使用__slots__

正常情况下，当我们定义了要给class，创建了一个class实例后，我们可以给这个实例绑定任何属性和方法，这就是动态语言的灵活性；

先定义class:


```python
class Student(object):
    pass

```

然后，尝试给实例绑定一个属性：

```python
>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael
```

当我们想要限制实例属性的时候；比如，只允许对Student实例添加name和age属性

为了达限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制class实例的添加属性：


#### 使用@property

在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改

```python
class Student(object):
    pass
s = Student()
s.score = 9999
```

这样显然是不合理的，可以通过一个set_score()方法来设置成绩；再通过一个get_score()来获取成绩，再方法里面检查参数

通过set_score方法的限制，对于score的修改就变得不那么随意了；
```python

class Student(object):
    def get_score(self):
        return self.score
    
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value

```




