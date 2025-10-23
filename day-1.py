#列表-list (可储存所有数据，并且可以修改): []
info=['hahah',18,18.3,True,False]
print(info)
print(len(info))
print(info[0])
print(info[1])
print(type(info))
print(type(info[2]))
print(type(info[3]))
print(type(info[4]))
print(type(info[1]))
info[0]='ALL'
print(info[0])
#嵌套
a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
print(c[0][0])#取a的第一个元素
print(c[0])


#元组-tuple(可储存所有数据，但不可以修改): ()
stu=('A7','A8','A9','A10','A11')
print(stu)
print(stu[1])
print(type(stu))

stu1=('A12',)#<class 'tuple'>
stu2=('A13')#<class 'str'>
print(type(stu1))
print(type(stu2))

#转义字符  :[+r---取消转义(常用于电脑路径或网站)] \n(换行) \t(空格)
#                        \\(输出一个\) \'(正常输出')
print('好好学习\n天天向上')
print('好好享受\t天天向上')
print('好好享受\\天天向上')
print(r'好好享受\\天天向上')
print('说 :"1111" ')

#数据类型的转换: str/bool/list/tuple<--->int/float
num=90
res=float(num)
print(res)
res1=str(num)
print(res1)
print(res1+'10')#9010
print(res+10)#100.0

#关于bool 类型的转化: 非零和有值转为True,零和空值转为False
#                   空值有:' '/ []/ None/ {}/ set()
info2=''
b001=bool(info2)
print(b001)

info3=set()
b002=bool(info3)
print(b002)

#关于input的拼接(需要相同类型的数据才能拼接，否则需要转化)
'''
hight1=int(input('请问你的密码是什么？'))
num2=hight1+10
print(num2)
print(type(num2))
'''

#运算符---> **(幂) *(乘) /(除) %(模运算--->求余数) ！=(不等于)
#           not,or,and(逻辑运算符)
#赋值运算符与复合赋值运算符
a=10
b=93
a +=b
a *=b+2
print(a)
print((a:=10))#(:=)海象运算符--->将运算符右边的值赋给左边，
                        # 且此时运算符的右边也是整个表达式的值
print(a)            #10

#比较运算符 (优先级高于赋值运算符)与逻辑运算符
#==,!=,<,>,<=,>=
#and:如果两边的布尔值都是True,则输出也是True;若两边有一个是False,
#    则输出为False,(短路)。
#or:如果两边的bool值有一个是True,则最终结果是True
#not:若后面的bool值是True,则输出结果为False;反之亦然
key=1 ==1
key1=2 >3
key2=3 <5
flag= key1 and key2
flag1=key1 or key2
flag2= not key1
print('key=',key)
print('key1=',key1)
print('key2=',key2)
print('flag=',flag)
print('flag1=',flag1)
print('flag2=',flag2)
print(key2 and not flag2)

#eg1:输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为：
    #   C=(F-32)/1.8

temp=float(input('请输入华氏温度：'))
F=temp
C=(F-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(temp,C))#占位符
print(f'{temp:.1f}华氏度={C:.1f}摄氏度')#格式化输出 %s(给字符串占位置)
#           .format(实参1,实参2)               %d(整型)     %f(浮点型)
#[要么全放下标,要么全不放 下标也不能放负向下标]
print('{0}说，要加油，成为像{0}一样拥有{1}元巨款的人'.format('张三',8000000))
#eg2:输入一个圆的半径，计算出它的周长及面积

radius=float(input('请输入半径'))
perimeter=radius * 3.14159 * 2
area=radius * 3.14159 * radius
print('周长为:%.3f'%perimeter)
print('面积为:%.3f'%area)


#内置函数
import math
radius=float(input('请输入半径'))
perimeter=radius * math.pi * 2
area=radius * math.pi * radius
print(f'周长:{perimeter:.3f}')
print(f'面积:{area:.3f}')

#eg3:输入一个 1582 年以后的年份，判断该年份是不是闰年。
year=int(input('输入一个 1582 年以后的年份，判断该年份是不是闰年。'))
is__leapyear=year % 4==0 and year % 100 !=0 or year % 400==0
print(is__leapyear)
print(f'{is__leapyear= }')#bool型的直接打印变量名