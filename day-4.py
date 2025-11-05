#分支和循环结构实战
#1---输出100以内的素数
from calendar import firstweekday
from runpy import run_path

for num in range(2,101):
    is_prime = True
    for i in range (2,int(num**0.5)+1):
        if num % i ==0 :
            is_prime = False
            break
    if is_prime:
        print(num)

#2----输出斐波那契数列中的前 20 个数。
a,b=0,1
for _ in range (20):
    a,b= b,a+b
    print(a)

#3---输出 100 到 999 范围内的所有水仙花数。
for nunm in range (100,1000):
    low = nunm % 10
    high = nunm // 100
    mid = nunm // 10 %10
    if nunm ==low **3 + mid  **3 + high **3:
        print(nunm)

a=4
b=10
a //=b
print(a)#40

num = int(input('num=   '))
reversed_num=0
while num>0:
    reversed_num= reversed_num*10 + num %10
    num //=10
print(reversed_num)
'''
#4----百钱百鸡问题，公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，
# 用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range (0,21):
    for y in range (0,34):
        for z in range (0,101,3):
            if x+y+ z==100 and x*5+y*3+z//3==100:
                print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')
                #break
'''

for x in range (0,21):
    for y in range (0,34):
        z=100- x- y
        if z%3==0 and x*5+y*3+z//3==100:
            print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')

#例子5：CRAPS赌博游戏

import random

money=1000
while money>0:
    print('你现在的总资产为{}元'.format(money))
    while True :
        debt = int(input('请下注:   '))
        if 0< debt <= money :
            break
    firstpoint=random.randrange(1,7)+random.randrange(1,7)
    print(f'玩家掷出了{firstpoint}点')
    if firstpoint==7 or firstpoint==11:
        print('玩家胜！\n ')
        money+= debt*1.5
        print('你现在还有资产{}元'.format(money))
    elif firstpoint==2 or firstpoint==3 or firstpoint==12:
        print('庄家胜！\n')
        money-= debt*1.1
        print(f'你现在还有资产{money}元')
    else:
        while True:
            secondpoint=random.randrange(1,7)+random.randrange(1,7)
            print(f'玩家掷出了{secondpoint}点')
            if secondpoint==7 :
                print('庄家胜！\n')
                money-=debt*1.1
                print(f'你现在还有资产{money}元')
                break
            elif secondpoint ==firstpoint:
                print('玩家胜！\n ')
                money+= debt*1.5
                print(f'你现在还有资产{money}元')
                break
print('你破产了, 游戏结束!')




