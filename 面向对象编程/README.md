## 面向对象编程


> 其实所谓的面向对象就是 有联系方法的集合体，

在Python中，所有的数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（class）

数据封装，继承和多态是面向对象的3大特点；
 
 
#### 类和实例

Python中，定义类是通过class关键字：

```python
class Student(object):
    pass

```
class后面紧接着着是类名，即Student，类名通常是大写开头的单词，紧接着是（object）。表示该类是从哪个类继承下来的；

定义好Student类后，就可以通过类名+（）创建实例

类里面有个__init__方法，重写这个方法，可以在对象初始化的时候实现一定逻辑；例如（对象属性初始化）

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

注意到__init__方法的第一个参数永远是self,表示创建的实例本身；


#### 访问限制

在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就可以隐藏了内部的复杂逻辑。

但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name，score属性：

如果要让内部的属性不被外部访问，可以把属性的名称前面加上两个下划线__,在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。


#### 继承和多态

在面向对象程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass）,而被继承的class称为基类，父类，或者超类

例如：

```python

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
     
```

上面定义了一个Animal的类，再定义要一个Dog类，Dog继承了Animal，就自带了run方法；当Dog类再有run方法的时候就会覆盖了Animal的run方法；

#### 获取对象信息

##### 1.使用type()

首先，我们来判断对象类型，使用type()函数：

基本类型都可以使用 type()判断：

type()函数返回的是Class类型。如果我们要再if语句中判断两个变量的 数据类型是否相同可以用type

```python
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False
```

##### 2.使用isinstance()

对于class的继承关系来说，使用type()就很不方便了；使用isinstance()会更加方便


例如：

object -> Animal -> Dog -> Husky

```python
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True
>>> isinstance(h, Dog)
True
>>> isinstance(h, Animal)
True
```