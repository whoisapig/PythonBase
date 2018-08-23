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
