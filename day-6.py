#数据结构之 list ,tuple ,str ,set ,dict
#list------2 详见 day-3

#列表生成式
#场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
item12=[]
for _ in range(1,100):
    if _  %3==0 or _ %5==0 :
        item12.append(_)
print(item12)

item1=[i for i in range(1,100) if i % 3==0 or i % 5==0]
print(item1)


#场景二：有一个整数列表nums1，创建一个新的列表nums2，
# nums2中的元素是nums1中对应元素的平方。
nums1=[23,42,55,75,27]
nums2=[]
for num in nums1:
    nums2.append(num**2)
print(nums2)

nums11=[23,42,55,75,27]
nums22=[num**2 for num in nums11]
print(nums22)

#场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums111=[13,43,465,12,88,11,7]
nums222=[]
'''
for num in nums111:
    nums222.append(num > 50
                )
print(nums222)
#[False, False, True, False, True, False, False]
'''#错误
for num in nums111:
    if num > 50:
        nums222.append(num)
print(nums222)


nums1111=[13,43,465,12,88,11,7]
nums2222=[num for num in nums1111 if num > 50]
print(nums2222)

'''
scores=[]
for _ in range(5):
    temp=[]
    for i  in range(3):# 避免与下面变量名一致
        scores_1  =int(input('请输入成绩'))#注：scores_1 前后变量一致
        temp.append(scores_1)
    scores.append(temp)
print(scores)
'''

#列表的应用
#生成一组随机号码

import random

red_balls = list (range(1,34))
selected_balls = []
for _ in range(6):
    index =random.randrange(len(red_balls))
    selected_balls.append(red_balls.pop(index))
selected_balls.sort()
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end='\t')
blue_ball = random.randrange(1,17)
print(f'\033[034m{blue_ball:0>2d}\033[0m',end='\t\n')

#\033[0m是一个控制码，表示关闭所有属性，也就是说之前的控制码将会失效，
#   m前面的0表示控制台的显示方式为默认值，0可以省略，1表示高亮，5表示闪烁，7表示反显等。
# 在0和m的中间，我们可以写上代表颜色的数字，
# 比如30代表黑色，31代表红色，32代表绿色，33代表黄色，34代表蓝色等。


#random 提供的sample  和  choice函数

import random

red_ball1= [i for i in range(1,34)]
blue_ball1= [i for i in range(1,17)]
selected_balls1 = random.sample(red_ball1,6)
selected_balls1.sort()
for ball1 in selected_balls1:
    print(f'\033[031m{ball1:0>2d}\033[0m',end=' \t')
blue_ball = random.choice(blue_ball1)
print(f'\033[034m{blue_ball:0>2d}\033[0m',end = '\t\n')

#sample 可实现无放回抽取   \\\\  choice 可实现随机抽取一个元素


#若要生成几注号码，可以加一个n次循环

import random

n = int(input('生成几注号码'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

for _ in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m',end='\t')
    blue_ball  = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m',end='\n')

#11.10 20.56 install rich     \\\2025\\\

import random

from rich.console import Console
from rich.table import Table
# 创建控制台
console = Console()

n= int(input('生成几注号码') )
red_balls = [i for i in range(1,34)] #For dicts or sets, use sorted(d).")
blue_balls = [i for i in range(1,17)]#注意表达 ---()为元组无法排序
# 创建表格并添加表头
table=Table(show_header=True)

for col_name in ('序号','红球','蓝球'):
    table.add_column(col_name,justify = 'center')

for i in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    #向表格中添加行(序号 , red_ball,  blue_ball )
    table.add_row(
        str(i+1 ),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'

    )
# 通过控制台输出表格
console.print(table)


