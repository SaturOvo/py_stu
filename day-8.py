#数据结构之 list ,tuple ,str ,set ,dict
#str

s1='\\hello world\\'      #\hello world\
s2='\'hello world\''      #'hello world'
print(s1)
print(s2)


#s1='\it \is \time \to \read \now'
s2= r'\it \is \time \to \read \now'
#print(s1)
print(s2)


s1 = 'hello'+ ', '+ 'world'
print(s1)  #hello, world
s2= '!' *3
s1 +=s2
print(s1)

s1 *=2
print(s1)

#str +\ 支持八进制或十六进制
s1= '\141\142\143\x61\x62\x63'
print(s1)  #abcabc


s1='a whole new world'
s2='hello world'
#比较运算
#比较第一个字符的编码大小
print(s1==s2)
print(s1<=s2)
print(s1>=s2)
print(s1 == 'hello world')
print(s2 == 'hello world')
s3 = '王大锤'
print(ord('王'))
print(ord('大'))
print(ord('锤'))

#成员运算
s1='hello,world'
s2= 'goodbye-w,orld'
print('wo' in s1) #True

print('wo' in s2) #False


#索引和切片
#str是不可变类型，不可通过索引修改，只供正向或反向整数索引，且不可越界

# IndexError

#遍历

s= 'hello'
for  i in range(len(s)):
    print(s[i])


s = 'hello '
for elem in s:
    print(elem)

s1 = 'hello ,world'
print(s1.capitalize()) #首字母大写
print(s1.title())  #每个单词首字母大写
print(s1.upper())  #所有大写
print(s1.lower())

print(s1.find('or'))      # 8
print(s1.find('or', 9))   # -1
print(s1.find('of'))      # -1
print(s1.index('or'))     # 8
#print(s.index('or', 9))  # ValueError: substring not found
#find方法找不到指定的字符串会返回-1，index方法找不到指定的字符串会引发ValueError错误。
# 逆向查找
print(s1.find('o'))       # 4
print(s1.rfind('o'))      # 7
print(s1.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found

print(s1.startswith('he'))  #True
print(s1.startswith('He'))  #False
print(s1.endswith('d'))   #True
print(s1.isalpha()) #False
print(s1.isalnum()) #False 字母+数字

#格式化 性质判断
print(s1.center(20, '*'))
print(s1.rjust(20))
print(s1.ljust(20,'~'))
print('33'.zfill(5))
print('-33'.zfill(5))
#如果要在字符串的左侧补零，也可以使用zfill方法

#格式化
a=123
b=321
print('%d * %d = %d' %(a,b,a*b ))
print('{0} *{1} ={2}'.format(a,b,a*b ))
print(f'{a}*{b} = {a*b}')

'''
变量值	       占位符	    格式化结果	        说明
3.1415926	    {:.2f}	    '3.14'	        保留小数点后两位
3.1415926	    {:+.2f}	    +3.14'	        带符号保留小数点后两位
-1	            {:+.2f}	    '-1.00'	        带符号保留小数点后两位
3.1415926	    {:.0f}	    '3'	            不带小数
123	            {:0>10d}	'0000000123'	左边补0，补够10位
123	            {:x<10d}	'123xxxxxxx'	右边补x ，补够10位
123	            {:>10d}  	'       123'	左边补空格，补够10位
123	            {:<10d}	    '123       '	右边补空格，补够10位
123456789	    {:,}	    '123,456,789'	逗号分隔格式
0.123	        {:.2%}	    '12.30%'	    百分比格式
123456789	    {:.2e}	    '1.23e+08'	    科学计数法格式

'''
a=123
print('{:x<10d}'.format(a))

s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world


s= 'I%love%u%so%much '
words=s.split('%')
print(words)  #['I', 'love', 'u', 'so', 'much ']

words= s.split('%',1)
print(words)   #['I', 'love%u%so%much ']






#编码与解码

a= '王大锤'
b= a.encode('utf-8') #b'\xe7\x8e\x8b\xe5\xa4\xa7\xe9\x94\xa4'

c= a.encode('gbk')  #b'\xcd\xf5\xb4\xf3\xb4\xb8'
print(b)
print(c)
print(b.decode('utf-8'))
print(c.decode('gbk'))