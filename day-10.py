#数据结构之 list ,tuple ,str ,set ,dict
#dict


#dict函数
person=dict(name= '王大锤',age='22',height=177,weight=90,addr='成都')
print(person)
#通过zip压缩两个序列并创建字典
items= dict (zip('ABCDE','12345'))
print(items)
items2=dict(zip('ABCDE',range(1,10)))
print(items2)#{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

items3={x:x**3 for x in range(1,10)}
print(items3)


print(len(person))
for key in person:
    print(key)


person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)
#列表、集合、字典都可以作为字典中的值

print(person.get('name'))
print(person.get('sev'))
print(person.get('sev',True))
#get方法在字典中没有指定的键时不会产生异常，而是返回None或指定的默认值
print(person.items)
for key,value in person.items():
    print(f'{key}:\t{value}')

person1={'name':'王大锤','age':22}
person2={'height':120}

person1.update(person2
               )
print(person1)
person1 |= person2
print(person1)




# 可以通过pop或popitem在字典中删除元素，前者返回获得对应值，但不存在指定的键时会报错
#后者会返回键值对组成的二元组
print(person1.pop('name'))
#print(person1.pop('1'))        #KeyError: '1'
print(person1.popitem())    #('height', 120)

print(person1)
del person1['age']
print(person1)


sentence= input('请输入一段话')
counter={}
for ch in sentence :
    if 'A'<= ch <= 'Z' or 'a'<= ch <= 'z':
        counter[ch] = counter.get(ch,0) +1
sorted_key = sorted(counter,key= counter.get ,reverse=True)
for key in sorted_key:
    print(f'{key}出现了{counter[key]}次')
#Man is distinguished, not only by his reason,
# but by this singular passion from other animals,
# which is a lust of the mind, that by a perseverance of
# delight in the continued and indefatigable generation of
# knowledge, exceeds the short vehemence of any carnal pleasure.

#可以用字典的生成式语法来创建这个新字典
stocks={
    'AAP':191.22,
    'GKA':222.58,
    'GTI':120.44,
    'FB':100.23
}

stock2={key :value for key ,value in stocks.items()
        if value >=200}
print(stock2)