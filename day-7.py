#数据结构之 list ,tuple ,str ,set ,dict
#tuple
ti=(34,23,24,25)
ti2=('ad','dff','fdg')
for elem in ti :
    print(elem)

print(90 in ti)
print(34 in ti )
print('ad' not in ti)
#比较运算

#若只有一个元素，则需要加 ,   否则是str
a =()
print(type(a))#tuple

b=('fhhf')
print(type(b))#str
c=('fhhf',)
print(type(c))#tuple


#打包操作
a= 1,10,100
print(type(a))
print(a)

#解包操作

j,i ,l = a
print(i,j,l)# 逐一赋值  10 1 100

#通过*号表达，可以让一个变量接收多个值
a= 1,10,100,1000
i ,j ,*k =a
print(i,j,k)  #1 10 [100, 1000]
i, *j ,k =a
print(i,j,k) #1 [10, 100] 1000
*i ,j ,k =a
print(i,j,k)  #[1, 10] 100 1000

*i,j =a
print(i,j) #[1, 10, 100] 1000

i , j ,k ,*l =a
print(i,j,k,l)   #1 10 100 [1000]
i,j,k,l, *n =a
print(i,j,k,l,n)  #1 10 100 1000 []


a ,b, *c =range(1,10)
print(a,b,c)

a, b,c =[1,10,100]
print(a,b,c)

a,*b,c= 'hello'
print(a,b,c) #h ['e', 'l', 'l'] o

#交换变量
a,b =b,a
a ,b,c= b, c,a

#可与列表相互转换

