## Class

__Class__ 是一种抽象概念，比如我们定义的 Class——Student，是指学生这个概念，而实例（__Instance__）则是一个个具体的Student.


类(Class)和实例(Instance)是面向对象最重要的概念。


类是指抽象出的模板。实例则是根据类创建出来的具体的“对象”，每个对象都拥有从类中继承的相同的方法，但各自的数据可能不同。


在python中定义一个类:
```
class Student(object):
    pass
```
关键字class后面跟着类名，类名通常是大写字母开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的。通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承下来的类。

## dict

```
a = {} % dictionary   
a[0] = 1 
1 in a -> False    
0 in a -> True
```
