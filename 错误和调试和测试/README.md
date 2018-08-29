## 错误，调试和测试

### 错误处理

> 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错误，以及出错的原因；


#### try

让我们来用一个例子来看看try的机制:

```python
try:
    print('try is running')
    num = 10 / 0
    print ("result: is %s" %(num))
except ZeroDivisionError as e:
    print('except is running;this error is %s' %(e))
finally:
    print('finally is running')
print('end')
```

上面的结果会输出：

```
try is running
except is running;this error is division by zero
finally is running
end
```

使用 **try...except** 捕获错误还有一个巨大的好处，就是可以跨越多层；

因为错误会一直 一层一层地向上抛出，直到有处理位置；

所以我们不必要所有地方都去 try except 操作；只需要在适当的地方捕捉错误即可！


#### 调试

##### 1.print
print法是最为直接粗暴有效的方法，就是用 **print()** 把所有有可能出现问题的地方打印出来

但是这个方法法有一个致命的地方，那就是print()出来后。还得重新删除掉；如果删除漏了还会影响结果

也是这样衍生出了第二种方法

##### 2.断言法

凡是用 **assert()** 来辅助查看

程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

##### 3.logging

logging法是使用**logging**来替换 **print()** ;

这个方法不会抛出错误，而且可以输出到文件中；在web端调试第三方回调时候，是较为常用的一直手段


##### 4.IDE

下面介绍的是PyCharm

1.代码对应调试行前单击，添加调试断点（双击删除断点）

2.Alt+Shift+F9 快捷键启动调试

3.F8跳到下一行代码

4.F7跳到下一个断点
