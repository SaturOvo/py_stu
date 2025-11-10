#数据结构之 list ,tuple ,str ,set ,dict
'''
import random

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0

for _ in range(6000):
    point=random.randrange(1,7)
    if point==1:
        a1+=1
    elif point==2:
        a2+=1
    elif point==3:
        a3+=1
    elif point==4:
        a4+=1
    elif point==5:
        a5+=1
    else:
        a6+=1
print(f'1出现了{a1}')
print(f'2出现了{a2}')
print(f'3出现了{a3}')
print(f'4出现了{a4}')
print(f'5出现了{a5}')
print(f'6出现了{a6}')
'''



item1=list(range(1,11))
item2=list('hello')
print(item1)
print(item2)#['h', 'e', 'l', 'l', 'o']
#list 创建了列表对象
# + --->拼接   * --->重复
#可以使用in 或 not in 来判断元素是否在列表中
#例
print(8 in item1)
print(18 in item1)
print('a' not in item2)
print('e' not in item2)
#切片 (若希望一次性访问多个元素) [start:end:stride]
print(item1[0:7:3])   #[1, 4, 7]
print(item1[-1:-7:2]) #注意顺序  []
print(item1[-7:-1:2]) #[4, 6, 8]
print(item1[::2])     # [1, 3, 5, 7, 9]
print(item1[::-1])    #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(item1[-2:-7:-2])#[9, 7, 5]

#遍历
#way 1 通过索引运算
languages=['python','java','c++','kotlin']
for index in range(len(languages)):
    print(languages[index])

# way 2 直接循环
languages=['python','java','c++','kotlin']
for languages1 in languages:
    print(languages1)



import random
counter=[0]*6

for _ in range(6000):
    face=random.randrange(1,7)
    counter[face -1] += 1
for face in range(1,7):
    print(f'{face}点输出了{counter[face -1]}次')











