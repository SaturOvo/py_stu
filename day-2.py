#条件判断语句,if 如果/else 否则/elif或者
#      多分支
#from symbol import pass_stmt
from wsgiref.types import InputStream

height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('体重过轻')
elif 18.5 <= bmi <25:
    print('身体不错')
elif 25 <= bmi < 30:
    print('体重偏重')
else:
    print('你的身体还不够标准啊')

#循环结构  while(判断循环条件是否为真，不满足就结束循环)
num=1
while num <= 10:
    print(f'我在抄书，这是第{num}遍')
    num +=1
    if num == 5:#我在抄书，这是第4遍
        break

#循环结构  for/pass
for i in range(5):#不指定范围，则遍历从0 开始
    print(i)

for i in range(1,10,3):
    pass

for i in range(1,10):
    if i ==3 or i==5 or i==7:
        continue#(跳过)
    print(f'我在抄书，这是第{i}页')

#循环嵌套
#eg1:我想做个数字方阵长宽各为5 该怎么输出呢
for i in range(5):
    for j in range(5):
        print(1,end='')#里面有一个属性叫做end='\n',所以写一条print
#                       就会换行的原因
    print()#归外层循环管的,循环5次1 就换行

#eg2:写一个登录系统.判断登录的用户名和密码是否正确,
#可以用num来保存密码输入次数.如果密码正确就登录成功,
#如果错误就提醒. 密码输入超过3次就结束程序.就直接break

#id=int(input('请输入你的账号'))
#code1=input('请输入你的密码')
id_11=123
code_11='aaa11'
num1=1
for i in range(3):
    i1d = int(input('请输入你的账号'))
    code1 = input('请输入你的密码')
    if i1d==id_11 and code1==code_11:
            print('账号密码正确，登录成功')
            break
    else:
        print('账号密码错误，请重新输入')
        if num1 ==3:
            print('输错3次，登录失败')
            break
    num1+=1

list1=[5,5,3,32,224,13]
num2=1
num3=1
for i in list1:
    num2 +=i
    num3 *=i
print(num2)
print(num3)



status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)
'''
#使用match case构建分支
'''
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
'''
'''

status_code1 = int(input('响应状态码:'))
match status_code1:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418 : description = 'I an a teapot'
    case 429 : description = 'Too many requests'
    case _ : description = 'Unknwn Status Code'
print('状态码描述: ',description)
'''
#eg3:
'''
x=float(input('请输入x'))
y1= x*3-5
y2= x+2
y3= x*5+3
if x>1:
    print(y1)
elif -1<= x <=1:
    print(y2)
else:
    print(y3)
'''
'''
x=float(input('请输入x:'))
if x >1:
    y =3*x-5
else:
    if x>=-1:
        y=x+2
    else:
        y=5*x +3
print(f'{y}')


#eg3:要求：如果输入的成绩在90分以上（含90分），
# 则输出A；输入的成绩在80分到90分之间（不含90分），
# 则输出B；输入的成绩在70分到80分之间（不含80分），
# 则输出C；输入的成绩在60分到70分之间（不含70分），
# 则输出D；输入的成绩在60分以下，则输出E。
score=float(input('请输入你的分数'))
if       100>score>=90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
elif score>=60 and score<70:
    print('D')
else:
    print('e')

#eg4:要求：输入三条边的长度，如果能构成三角形就计算周长和面积；
# 否则给出“不能构成三角形”的提示。
a=float(input('请输入第一条边'))
b=float(input('请输入第二条边'))
c=float(input('请输入第三条边'))

if a+b>c and a+c>b and b+c>a:
    perimeter=a+b+c
    print(f'三角形周长为{perimeter}')
    s=perimeter/2
    area= (s*(s-a)*(s-b)*(s-c))**(1/2)
    print(f'三角形面积为{area}')
else:
    print('不能构成三角形')


#循环结构
import time#模块
print('hello world')
time.sleep(1)

import time
for i in range(10):
    print('hello world')
    time.sleep(1)


total=0
for i in range(1,101):
    total+=i

print(total)

total=0
for i in range (2,101,2):
    total+=i
print(total)



total=0
i=2
while i<=100:
    total+=i
    i+=2
print(total)


#break和continue
total=0
i=2
while True:
    total+=i
    i+=2
    if i >101:
        break
print(total)

#continue可以用来放弃本次循环后续的代码， 直接让循环
#进入下一轮
total=0
for i in range(1,101):
    if i % 2 != 0:
        continue
    total+=i
print(total)

#嵌套的循环结构
#eg6 打印乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}×{j}={i*j}',end='\t')
    print()

#eg7  输入一个大于 1 的正整数，判断它是不是素数。

num=int(input('请输入一个正整数'))
end=int(num**0.5)
is_prime=True
for i in range(2,end + 1):
    if num % i == 0:
        is_prime=False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
#最后，我们根据is_prime的值是True还是False来给出不同的输出。

#eg8   输入两个大于 0 的正整数，求两个数的最大公约数。

x=int(input('x=  '))
y=int(input('y=  '))
for i in range (x,0,-1):
    if i % x == 0 and i % y == 0:
        print(f'最大公约数：{i}')
        break


        #算法
x=int(input('x=  '))
y=int(input('y=  '))
while y%x != 0 :
    x,y =y %x ,x
print(f'最大公约数{x}')


#猜数字小游戏

import random
answer = random.randint(1,101)
cou=0
while True:
    cou+=1
    num = int(input('请输入：  '))
    if num == answer:
        print('你猜对了')
    elif num > answer:
        print('小一点')
    elif num < answer:
        print('大一点')
        break
print(f'你一共猜了{cou}次')
