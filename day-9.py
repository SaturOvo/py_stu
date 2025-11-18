#数据结构之 list ,tuple ,str ,set ,dict
#set

#无序性: 一个集合中，地位是相同且无序的
#互异性: 一个集合中，任何两个元素是不相同的
#确定性: 给定一个集合和一个任意元素，这个元素要么属于这个集合，要么不属于

#不支持索引运算


set1= {1,2,23,3,3,42,24,}
print(set1)

#遍历
for elem in set1:
    print(elem)
# &交(.intersection)  |并(.update)   -差(.difference)
set1.add(111)
set1.discard(2)
if 111 in set1:#删除
    set1.remove(111)

set1.clear()



set2=(1,45,666,7)
print(set1.isdisjoint(set2))#True
    #集合类型还有一个名为isdisjoint的方法可以判断两个集合有没有相同的元素，
# 如果没有相同元素，该方法返回True，否则该方法返回False，代码如下所示。


#不可变集合
fset1=frozenset({1,2,3})#frozenset({1, 2, 3})
print(fset1)

#除了不能添加和删除元素，
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False