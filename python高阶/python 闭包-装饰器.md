### 闭包内容：

1. 匿名函数：能够完成简单的功能，传递这个函数的引用，只有功能
2. 普通函数：能够完成复杂的功能，传递这个函数的引用，只有功能
3. 闭包：能够完成较为复杂的功能，传递这个闭包中的函数以及数据，因此传递是功能+数据
4. 对象：能够完成最复杂的功能，传递很多数据+很多功能，因此传递的是数据+功能

———————————————————

1. 对全局函数进行修改：在函数当中加global，在闭包中外边中的变量加nonlocal
2. 闭包定义：有两个函数嵌套使用，里面的函数可以使用外面函数所传输的参数，最后可传递的是里面函数的结构与数据(个人理解)。
3. 最后闭包可以在python中引申出装饰器
   ———————————————————

```python
def closure():
    # 在函数内部再定义一个函数，
    # 并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def closure_in(x):
        print('---------我是打不死的%s--------' %x)
    return closure_in

x = closure()
x('小强')

print('*'*20)
# -----加餐---------
def closure_1(a,b,c):
    def closure_on(x):
        print('-----%s加餐-------' %b)
        print(a*x + c)
    return closure_on

demo = closure_1(2,'小强',3) #传closure_1函数
demo(4) #传clsure_on函数

#注：函数不加括号，调用的是函数本身【function】；函数加括号，调用的是函数的return结果。
```



### 装饰器内容：

代码要遵守‘开放封闭’原则；对已经写好的函数遵守封闭，对功能扩展遵守开放；

```python
# 装饰器的作用：为了对原来的代码上进行扩展
def decoration(func):
    def call_func():
        print('-------正在装饰 -------' )
        func()
    return call_func

#@decoration     #--->demo_new = decoration(demo)
def demo():
   print('demo----')

demo_new = decoration(demo)
demo_new()
```

使用装饰器来测试一个函数的运行时:

```python
import time
def set_func(func):
	def call_func():
		start_time = time.time()
		func()
		stop_func = time.time()
		print(‘alltimes is %f’ %(stop_func-start_fun))
	return call_func
@set_func
def test1():
	print(‘——-test1———’)	
test1()

#等价于：
@set_func==test1 = set_func(test1)

```

##### 1. 没有参数，没有返回值的函数进行装饰：

```python
def set_func(func):
	def call_func():
		print(‘———test2——-’)
		print(‘———-test3——’)
		func()
	return call_func
	
@set_func
def test1():
	print(‘——test1——-	’)
```

##### 2. 对有参数无返回值的函数进行装饰：

```python
def set_func(func):
	def call_func(a):  #变
		print(‘———test2——-’)
		print(‘———-test3——’)
		func(a) #变
	return call_func
	
@set_func
def test1(num):
	print(‘——test1——- %d	’ %num)

test1(100) —->call_func(100)
test1(200)——>call_func(200)
```

复现装饰器原理：


————————————————————————-

#####  只要遇到@函数 装饰器(这句话)，在程序中就已经执行了！！

##### 3. 不定长参数的函数装饰：

```python
def set_func(func):
	def call_func(*args,**kwargs):  #变
		print(‘———test2——-’)
		print(‘———-test3——’)
		func(*args,**kwargs) #(拆包)将元祖拆开，每个进行传输；
		#func(args,kwargs)—>不行，相当于传递了两个参数：一个元祖，一个字典。
	return call_func
	
@set_func
def test1(num,*args,**kwargs):
	print(‘——test1——- %d	’ %num)
	print(‘——test1——- 	’ , args)
	print(‘——test1——- ’ ,kwargs )
	
test1(100)	
test1(100,200)
test1(100,200,300,mm=100)

```

注意：`*args `保存不定长参数，以元祖保存，`**kwargs`保存字典形式（mm=...)

##### 4.对应的返回值参数进行装饰、通用装饰器：

```python
#通用装饰器
def set_func(func):
	print(“开始进行装饰———-”)
	def call_func(*args,**kwargs):  #变
		print(‘———test2——-’)
		print(‘———-test3——’)
		return func(*args,**kwargs) #(拆包)将元祖拆开，每个进行传输；如果没有return ret返回none。
		#func(args,kwargs)—>不行，相当于传递了两个参数：一个元祖，一个字典。
	return call_func
	
@set_func
def test1(num,*args,**kwargs):
	print(‘——test1——- %d	’ %num)
	print(‘——test1——- 	’ , args)
	print(‘——test1——- ’ ,kwargs )
	return ‘ok’    #—-返回给上面的func()，然后return func—ret
	
ret = test1(100)

```

##### 5. 多个装饰器对同一个函数进行装饰：

```python
def add_qx(func):
	print(“——开始进行装饰权限1———-”)
	def call_func(*args,**kwargs):  #变
		print(‘这是权限验证1’)
		return func(*args,**kwargs)
	return call_func
	

def add_xx(func):
	print(“——开始进行装饰xx功能———-”)
	def call_func(*args,**kwargs):  #变
		print(‘这是xx权限验证’)
		return func(*args,**kwargs)
	return call_func
	
@add_qx
@add_xx
def test1():
	print(‘——test1——-’)	

test1()

```

首先执行第一个，但是第一个装饰器下面不是函数（装饰器原则：下面必须是函数，否则不执行），所以第一个函数先等待，等第二个装饰器执行后形成函数在交给第一个装饰器；所以运行结果是：

1. 开始进行装饰xx的功能，
2. 开始进行装饰权限1，
3. 这是权限验证1，
4. 这是xx权限验证，
5. ——-`test1`——-，

——————装饰器练习—————-
输出格式：```<td><h1>haha</h1></td>```

```python
def set_func_1(func):
	def call_func():
		return ‘<h1>’ + func() + ’</h1>’
	return call_func
	

def set_func_2(func):
	def call_func():
		return ‘<td>’ + func() + ’</td>’
	return call_func
	
@set_func_1()
@set_func_2()
def get_str():
	return ‘haha’
	
print(get_str()) 
```

最后执行的效果：
```<h1><td>haha</td></h1>```

##### 6. 用类对函数进行装饰（了解）：

```python
class Test(object):
	def __init__(self,func):
		self.func = fun
		
	def __call__(self):
		print(‘这里是装饰器的功能。。。。’)
		return self.func()
		
@Test
def get_str():
	return ‘haha’
	
print(get_str())
```



#### 以上就是装饰器与闭包的全部内容，希望有所收获，如果有错误，希望指出，感谢！！
