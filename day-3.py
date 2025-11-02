#序列类型
#1. 列表方法

food = ['麻辣烫','螺蛳粉','火锅','泡菜']
food.append('21')#增，添加到最后一位
food.append(['蜜雪冰城',5])
print(food)
food.insert(3,'da')#插入
print(food)
food.extend('dbabd')#打散追加
print(food)
food.extend(['绿豆雪糕',1])#追加序列类型，把值分别加进去
#区别于append的一起加进去
print(food)
food.pop()#默认删除最后一位(仅下标)
print(food)
food.remove('21')#删除指定元素，从第一个开始删
print(food)
food.clear()#清空
print(food)
'''del food'''#删除整个变量

food[1:3]='草莓','葡萄','芒果','榴莲'
print(food)#切片修改
num=[1,2,5,3,4,68,4,2,6,1,1]
print(num.index(3))#默认从下标为0的位置开始搜索找第一个你要查的这个数据的下标
print(num.index(2,3))
#从起点下标开始找数据(数据,起点下标)，#从3这个下标开是找第一个数据2的下标
print(num.count(1))#统计数据出现的次数
num2=[6.66,520,70,123,888,False,9]
num2.sort()# 排序
print(num2)#对列表的内容进行排序.如果列表里面有字符串是不可以排序.
#默认是升序排序,从小到大
num2.sort(reverse=True)#降序排序
print(num2)


#2.  元组不能修改元素()
#3.  str类型
#join:指定字符串连接序列中元素后生成一个新的字符串
s='-'
talk='哈哈哈哈哈'
print(s.join(talk))
li=['aa','bb','cc']
print('..'.join(li))##aa..bb..cc
talk1='你这傻逼玩的这么傻逼的操作还来玩游戏'
print(talk1.replace('傻逼',' '))
#替换或删除
print(talk1.replace('傻逼',' ',1))

talk2=' hollo world '
print(talk2.upper())#全部大写
print(talk2.lower())#全部小写
print(talk2.title())#首字母大写
print(talk2.strip())#去除左右两边空格
print(talk2.split('o'))#切分，切分字符串
#[' h', 'll', ' w', 'rld ']   ('分割对象‘)
a = '212132'
b = 'dda'
print(a.find(b))#(内容,下标) -1
print(a.isdigit())#判断字符串里是否为纯数字.结果为布尔值
print(b.isalpha())#判断字符串是否为纯中文或者字母
c='大家很帅.png'
print(c.endswith('.png'))
print(c.endswith('帅'))#判断字符串的后缀.是否为指定字符.结果为布尔


#4 集合 set {} 唯一性，无序性(不能有下标)
#可以进行简单的逻辑运算 &交 |并 -差


num1={1,2,3}
num2={3,4,5}
print(num1 & num2)
print(num1 | num2)
print(num1 - num2)
print(num2 - num1)
#遍历
numbere={1,2,3,4,5,6,7,8}
for i  in numbere:
    print(i)


room = {'麻子', '高启盛', '老莫', '高启强'}
room.add('ggga')#随机加入
room.update('哈ok')#打散后随机加入
room.pop()#随机删一个
room.remove('ggga')
room.clear()
#print(room)

#字典 dict 储存键值对 key : value 还可以嵌套
info={
'姓名':'SaturOVo'
,
'余额':8.8,
'年龄':18
}
print(info)
print(type(info))
print(info['余额'])
info1={
'姓名':'伊诺'
,
'余额':[8.8,100,1313],
'年龄':18,
'住址':{1:'工作',2:'家乡'}

}
print(info1)

info2={
'姓名':'伊诺'
,
'余额':8.8,
'年龄':18,
'年龄':38,
}
print(info2)#只会保留最后一个年龄这个键值对

for i in info2:
    print(info2[i])#值
    print(i)#名
#or
for i,j in info2.items():
    print(i)
    print(j)

info.setdefault('电话')#默认为None
info.setdefault('电话',111)
info.pop('年龄')#指定
info.popitem()#从最后一个开始删
#info.clear()
info.update({'姓名':'dad'})#有就改，无就增(可多个)
print(info.get('余额'))#查，无则输出None
print(info.keys())#获取所有键
print(info.values())#all 值
print(info.items())#键值对

#声明空变量

name1=[]#声明空列表
name2=()#声明空元组
name3=''#声明空str
name4=set()#声明空集合
name5={}#声明空字典
name6=None#声明空值



