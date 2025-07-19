# n=int(input("enter a no:"))
# for i in range(0,n+1):
#     ans=i**2
#     print(ans)
# 
# x=10
# y=5
# x,y=y,x+y
# print(x,y)
# def fun(x):
#     return x+x*2
# print(fun(4)-fun(2))

# num=3
# for i in range(2):    
#     num*=2
# num+=1
# print(num)

#add the list of the elements
# list1=[2,4,5,7,8]
# list2=0
# for i in list1:
#     list2+=i
# print(list2)

#get the max and min no in list
# list1=[23,44,66,18,30]
# value=list1[0]
# for i in list1:
#     if i < value:
#         value=i
# print(value)

#Remove duplicate form the list
# list1=[2,4,6,2,8,3,4]
# value=[]
# for i in list1:
#     is_duplicate=False
#     for j in value:
#         if i == j:
#             is_duplicate= True
#             break
#     if not is_duplicate:
#         value.append(i)
# print(value)

#second largest number in list
# a=[10,5,20,8,20]
# largest=a[0]
# for i in a:
#     if i > largest:
#         largest=i

# filtered=[]
# for i in a:
#     if i != largest:
#         filtered.append(i)

# if filtered:
#     second_largest=filtered[0]
#     for i in filtered:
#         if i > second_largest:
#             second_largest=i
#     print(second_largest)

# Remove all the vowels in list
# def without_vowels(n):
#     vowels=('a','e','i','o','u')
#     result=''
#     for char in n:
#         if char not in vowels:
#             result+=char
#     return result
# print(without_vowels("dineshkumar"))

#Count the Occurrences of a Character in a String
# def count_char(n):
#     word='a'
#     result=0
#     for char in n:
#         if char in word:
#             result+=1
#     return result
# print(count_char("dineshkumaraa"))

# count the letter from the string
# input='string'
# result=0
# for char in input:
#     result+=1
# print(result)

# add a listvalue
# input=[2,3,4,5]
# result=0
# for i in input:
#     result+=i
# print(result)

# find the len of each word in dictionary method
# d="dineshkumar","jjjh","kkk","sdd","ooo"
# zipped={}
# for i in d:
#     zipped[i]=len(i)
# print(zipped)

# name="Harry","Berry","Tina","Akriti","Harsh"
# score=37.21,37.21,37.22,41,39
# zipped=zip(name,score)
# zipp=dict(zipped)
# mini=min(zipp,key=zipp.get)
# for i in zipp:
#     if i == mini:
#         print(mini)

#arrange the list in order ascending and descending

# road=[4,8,-1,-1,3,5]
# length=len(road)

# for i in range(length):
#     for j in range(0,length-i-1):
#         if road[j]>road[j+1]:
#             road[j],road[j+1]=road[j+1],road[j]
# print(road)

#count the string
def reverse_string(n):
    output=0
    for i in n:
        output+=1
    print(f"{n}: {output}")
reverse_string("dineshkumar")

n=[2,3,4,5,3,2]
value=[]
for i in n:
    is_duplicate=False
    for j in value:
        if i==j:
            is_duplicate=True
            break
    if not is_duplicate:
        value.append(i)
print(value)
print("good things")
print("bad things")
