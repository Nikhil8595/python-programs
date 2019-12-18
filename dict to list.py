# a={1:'hey',2:'hello',3:'how',4:'are',5:'you'}
# b=[]
#
# b.append(a.items())
# print("only values:",a.values())
# print(b)
#
# list=[(x) for x in a.values()]
# print(list)

# a=[1,2,3,4,5]
# print(a[3:0:-1])
#
# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# import random
# fruit=['apple', 'banana', 'papaya', 'cherry']
# random.shuffle(fruit)
# print(fruit)
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
# print(fun(data[0]))
# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop(),end=' ')
# a=[1,9,3,5,2,8,4]
# a.sort()
# print(a[-1])
# print(a.pop())
# print(a)
# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
#     print()
# for i in range(0, 6):
#     print(arr[i], end = " ")
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     #print(arr[i])
#     arr[i - 1] = arr[i]
#     print()
# for i in range(0,6):
#     print(arr[i],end=' ')
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#print(fruit_list2)
#print(fruit_list3)
# init_tuple = ()
# print (init_tuple.__len__())
# init_tuple = [(0, 1), (1, 2), (2, 3)]
#
# result = sum(n for _, n in init_tuple)
#
# print(result)
# l = [1, 2, 3]
# print(l.__len__())
# print(l[::-1][0])
# (l.__len__() - l[::-1][0])
#
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
# init_tuple = ((1, 2),) * 7
# print(init_tuple)
# print(init_tuple[3:8])
# print(len(init_tuple[3:8]))
# a = {(1,2):1,(2,3):2}
# print(a.keys())
# print(a.values())
# print(a[1,2])
# a = {'a':1,'b':2,'c':3}
# print (a['a'],a['b'])
# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
#
# print (sum)
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#
# print (sum)
# print(my_dict)
# dict = {'a': 97, 'c': 96, 'b': 98}
#
# for a in sorted(dict):
#     print (dict[a])
# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r))
# # print(id(rec))
# print(list("i love python."))
# hey={n:n*n for n in range(1,11)}
# hi=[n*n for n in range(10)]
# dict=hey.copy()
# print(dict)
# # print(hi)
# class Test:
#     def __init__(self, name):
#         self.cards = []
#         self.name = name
#
#     def __str__(self):
#         return '{} holds ...'.format(self.name)
#
#
# obj1 = Test('obj1')
# print (obj1)
#
# obj2 = Test('obj2')
# print (obj2)
# # isinstance(obj, (class1, class2, ...))
# Mailbox=[]
# Document=[]
# def lookUp(obj):
#     if isinstance(obj, Mailbox ):
#         print ("Look for a mailbox")
#     elif isinstance(obj, Document):
#         print ("Look for a document")
#     else:
# #         print ("Unidentified object")
#
# def multiplexers ():
#
#     return [lambda n: index * n for index in range (4)]
# multiplexers()
#a=[lambda n: index * n for index in range (4)]
# def fast(lt=[]):
#     lt.append(11)
#     print(lt)
# fast()
# fast()
# keyword = 'aeioubcdfg'
# print (keyword [:3])
# print(keyword [3:])
# duplicates = ['a','b','c','d','d','d','e','a','b','f','g','g','h']
# unique=set(duplicates)
# print (sorted(unique))
# def wordcount(str):
#     counts=dict()
#     words=str.split(',')
#
#     for word in words:
#         if word in counts:
#             counts[word]=+1
#         else:
#             counts[word]=1
#     return counts
# print(word_count("he hi hello how are hi and where are you"))
# def noscounts(str):
#     counts=dict()
#     nos=str.split(',')
#
#     for  in nos:
#         if no in counts:
#             counts[no]=+1
#         else:
#             counts[no]=1
#     return counts
# wordlist='1,1,2,2,2,3,34,4,45,5,67,7,4,7,8'.split(',')
# def dic(words):
#     wordlist={}
#     for index in words:
#         try:
#             wordlist[index]=+1
#         except KeyError:
#             wordlist[index]=1
#     return wordlist
# wordlist='1,1,2,2,2,3,34,4,34,5,67,7,4,7,8'.split(',')
# print(wordlist)
# print(dic(wordlist))
# def dic(words):
#     wordList = {}
#     for index in words:
#         try:
#             wordList[index] += 1
#         except KeyError:
#             wordList[index] = 1
#     return wordList
#
#
# wordList = '1,3,2,4,4,3,5,3,2,1,4,3,2'.split(',')
# print(wordList)
#
# print(dic(wordList))
# def wordcount(str):
#     counts=dict()
#     words=str.split(',')
#
#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts
# print(wordcount('1,2,3,4,5,6,1,2,3,4,5,6,7,8,9'))
#=int(input("please give input no:"))
#lx=[0,1]
#ff=[lx.append(lx[-1]+lx[-2]) for a in range(2,x)]
#print(lx)
# a=0
# b=1
# for i in range(x):
#     print(a,end=' ')
#     #(a,b)=(b,a+b)
#     #a,b=b,a+b
#     c=a+b
#     a=b
#     b=c
# print(a,end=' ')

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
        print(end=' ')
fib(6)