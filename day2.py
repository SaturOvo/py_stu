#条件判断语句,if 如果/else 否则/elif或者
#      多分支
#from symbol import pass_stmt

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


'''
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


status_code1 = int(input('响应状态码:'))
match status_code1:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418 : description = 'I an a teapot'
    case 429 : description = 'Too many requests'
    case _ : description = 'Unknwn Status Code'
print('状态码描述: ',description)

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
x=float(input('请输入x:'))
if x >1:
    y =3*x-5
else:
    if x>=-1:
        y=x+2
    else:
        y=5*x +3
print(f'{y}')