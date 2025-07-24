# if语句
*if语句，我一开始理解它是一种结构，但《python，从入门到实践》指出应是一种测试，确定当前处于一种什么情形。*
## 条件测试


每条if语句的核心都是一个True或False的表达式，这种表达式被称为条件测试。python通过条件测试的值为True还是False来决定是否执行if语句中的代码。如果为True，就执行。为False，就忽略。
常见的几种条件测试（也称为布尔表达式）：
1. 判断是否**相等**
示例：
    car='world'
    car=='world'
    True

注意在python中，字母的大小写是有区别的。
示例：
    car='world'
    car=='World'
    False

面对这种情况，如果需要忽视大小写的情况下，我们可以采取将他们全都转换为大写或者小写来进行比较。
示例：
    car=='world'
    car.lower()=='World'.lower()
    True

2. 判断是否**不相等**
*我们将**不相等**也视为一种判断条件，看它True还是False*
示例：
    car=world
    car!=World
    True

3. 数值比较
判断符号有
>,<,>=,<=,=,!=
示例：
    number=1234
    number<12345
    True

4. 同时测试多个条件
判断符号有：
and ， or，
示例：
    number1=123
    number2=234
    number1<1234 and number2>123
    True

    number1=123
    number2=234
    number1<1234 or number2>1234
    True
5. 检查特定值是否**包含在列表中**
判断符号有：
in
示例：
    list=['1','11']
    '1' in list
    True
6. 检查特定值是否**不包含在列表中**
判断符号有：
not in

示例：
    list=['1','11']
    '2' not in list
    True

## if 语句

几种if语句类型

1. if-else
示例：
    number=123
    if number >1234:
        number=1234
    else:
        print('yes')
* else这一结构是可以省略的
即：
    number=123
    if number>1234:
        number=1234

2. if-elif-else：
示例：
    number=123
    if number>1234:
        number=1234
    elif number<1000:
        number=100
    elif number<10:
        number=10
    elif number<1
        number=1
    else:
        number=111
* 在if-elif-else结构中，只会接受一个条件语句判断，一旦判断为True，后面的elif-else语句将会被跳过.
要想判断多个条件，只能使用多个if语句
示例：
    number=123
    if number>1234:
        number=1234
    if number<1000:
        number=100
    if number<10:
        number=10
    if number<1
        number=1
    else:
        number=111

* 
    number=[]
    if number：
        number=100
表示number为空列表亦可，执行后面的语句块