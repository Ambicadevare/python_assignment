# # # string immutable

# # # case_conversion_built_in function.
# # #lower , upper, islower,isupper,swapcase, len, captlize,count
# # #index----for list and strong


# # #tittle()fun converts the first letter of each word to uppercase.
# # a = "ambica hospet"
# # print(a.title())    #Ambica Hospet


# # #intersection---- means finding the common elements between two (or more) sets.
# # A = {1, 2, 3, 4 ,5 }
# # B = {2, 7 , 8 , 9 , 1}
# # print(A.intersection(B)) #{1,2}

# # #strings and lists dont have a direct .intersection() method, but you can convert them to sets first:
# # s1 = "ambica"
# # s2 = "akash"
# # common = set(s1).intersection(s2)
# # print(common)                           #a


# # #swapcase---change upper to lower lower to upper
# # a = "aarvIKa"
# # print(a.swapcase())      #AARvikA



# # #captitalize--- it converts the first character of the string to uppercase 
# # #the rest of the string becomes lowercase
# # #it doesnt change the original string beacause strings are immutable.
# # text1 = "ambica is a good Girl"
# # print(text1.capitalize())   #Ambica is a good girl


# # #isupper---  it checks if all the alphabetic characters in a string are uppercase.
# # #Returns  a boolean value:
# # #True-- if all letters are uppercase
# # #False-- if all letters are lowercase
# # a = "shreayansh"
# # print(a.isupper())    #false


# # #islower--- it checks if all the alphabetic charcters in a string are lowercase or not.
# # #Returns  a boolean value
# # b="aarvika"
# # print(b.islower())         #True


# # #lowercase--it returns all string in charcters to lowercase
# # a = "AMBICA"
# # print(a.lower())    #ambica


# # #uppercase()
# # a = "ambica"
# # print(a.upper())     #AMBICA


# # #len---it returns the number of items in:
# # #a string--- number of characters
# # #a list/tuple/set/dict---number of elemnts
# # #any iterable that supports length
# # text= "shreyansh"
# # print(len(text))   #9


# # #trimming and replacing builtin fun
# # #strip,rstrip,lstrip,replace

# # #strip--to remove extra spaces
# # #assign then print
# # a="    ambica  "
# # s = a.strip()
# # print(s)

# # #rstip--right strp means to removes spcaes from right side
# # a = "     ambica   "
# # s = a.rstrip()
# # print(s)          #    ambica


# # #lstrip--to remove spcaes from left side
# # a = "   ambica   "
# # s = a.strip()
# # print(s)        #ambica


# # #it returns a new string where all occurebces of a substring are replaced with another substring
# # #to replace old value to new value 
# # #replace(old,"new")
# # #if w e replace the word with other word which is there in given string it wont give  error
# # #but it just run the code without any op or error
# # a = "ambica"
# # a = a.replace("ambica","hospet")
# # print(a)      #hospet


# # #find--- where the elemnt is present in which index
# # str1 = "ambica"
# # print(str1.find("b"))     #3


# # #startswith()---we get true or false if the word starts with same
# # str1 = "ambica"
# # print(str1.startswith('a'))


# # #endswith()-- we get true or false if the word ends with with same
# # str1 = "ambica"
# # print(str1.endswith('ica'))


# # ##split() fun it split each element
# # num1 = input("enter nums: ")
# # print(num1.split("."))         



# # #split()  it split each element
# # num1 = input("enter nums: ")
# # print(num1.split(","))        #['2','3','4','5','7']
# # #if we use it without map it convert into list 
# # #input ("enter all csv format num:").split(",")---list
# # #(map((float,input("enter all csv format num:").split(","))))------ we get 
# # #split() fun it split e       
# # a = num1,num2,num3 = (list(map(float,input("enter all csv format num:").split(','))))
# # print(a)
# # #
# # print("how r yu ambica".split('.'))


# # #jion
# # list1 = ["1","2","3","4","hi"]
# # encoded_string = "," .join(list1)
# # print(encoded_sting)    #1,2,3,4



# # #set-- collection of unorderd finite unique
# # #discard---if we give element from outside also it print same input but wont give error
# # s= {1,4,5,6}
# # s.discard(7)
# # print(s)

# # #pop-----which index to delete
# # s={1,2,3}
# # s.pop()
# # print(s)


# # #6 clear()--remove all 
# # num={1,2,3,4}
# # print(num.clear())
# # a = num.clear()
# # print(a)           #none

# # #7 index(x)--first index of x
# # nums=[1,2,3,4,5]
# # print(nums.index(2))       #3

# # #8 count(x)-- frequency of x
# # x = {1,2,3,}
# # print(x.count(2))   # {3}

# # #9 sort()--sort list 
# # nums={2,4,6,5,1}
# # nums.sort()
# # print(nums)     #{1,2,3,4,5,6}

# # #10 reverse()--reverse order
# # nums = {1,2,3,4,5}
# # nums.reverse()
# # print(nums)       #{5,4,3,2,1}

# # #11 copy()-- shallow copy 
# # new_list = nums.copy()

# # #add --to add elem into set
# # num1 = {1,2,3}
# # num1.add(12)
# # print(num1)    #{1,2,3,12}


# # #difference---if a-b we get a elem which are not in b
# # #if b-a we get b elment which are not in a
# # a = {1,2,3}
# # b = {1,2,4,5,6,7}
# # print(a.difference(b))   #{3}
# # print(b.difference(a))   #{4,5,6,7}


# # #symmetric_difference --- which are same that elem we wont get
# # a = {1,2,3,4,5}
# # b = {1,2,3,4,6,7,8,9}
# # print(a.symmetric_difference(b)) #{5,6,7,8,9}


# # #isdisjoint()--- no common elem we get true or false
# # a = (1,2,3)
# # b = {1,3,45,55} 
# # print(a.isdisjoint(b))    #False
# # a = {1,2,3}
# # b = {4,5,6}
# # print(a.isdisjoint(b))    # true 

# # #union--- combine both sets
# # a = {1,2,3,4,5}
# # b = {6,7,8,9,}
# # print(a.union(b))   #{1,2,3,4,5,6,7,8,9}

# # #remove()---in remove if we give emenent from outside we get error  
# # a = {1,2,3}
# # a.remove(10)
# # print(a)      #error
# # a = {1,2,3}
# # a.remove(3)    
# # print(a)     #{1,2}



# # #map---map(function,iterable)
# # def square(x):
# #     return x*x
# # num = [1,2,3,4,5,6]
# # result = map (square, numbers)

# # print(list(result))
# # #output: {1,4,9,16,25,36}


# # #issuperset---checks if the set contains all elements of another set
# s1 = {1,2,3}
# s2 = {1,2}
# print(s1.issuperset(s2))  #True


# # #issubset--- checks if all elemnts of the set are in another set
# s1 = {1,2,4}
# s2 = {1,2,3}
# print(s1.issubset(s2))


# # #union or |
# # s1 = {1,2,4}
# # s2 = {1,2,3}
# # print(s1 | s2) #union
# # print(s1 - s2)  #difference
# # print(s1 + s2)  #append
# # print(s1 & s2)   #----intersection symbol


# #sort---
# list = [1,2,3,-65,87,-98]
# list.sort()
# print(list)


# list1 = ['ball','apple','cat']
# list1.sort()
# print(list1)


# # #string sorted
# # print("ambica" > "siddu")

# # #string and integer
# # list = ["ambica","cat",55,-9]
# # list.sort()
# # print(list)


# list1 = [[1,2,3],[-3,4,5,6],[0.5,8,9,10]]
# list1.sort(key = lambda x: (x[0],x[2]))
# print(list1)

# #copy----
# # list1 = [1,2,3,4,[6,7,8]]
# # list2 = list1
# # list1.append(9)
# # print(list2)


# #shallow copy
# list1 = [1,2,3,[5,6,7]]
# shallowcopy = list1.copy()
# print(list1)
# print(shallowcopy)
# list[1] = 90
# list[3][2]=66
# print(list1)
# print(shallowcopy)

# #deepcopy
# list1 = [1,2,3,4[1,2,3,4]]
# list1[4][1]=43
# list3 = .copydeepcopy


#zip()---The zip function combines two or more iterables(list,tupple,string)into a single iterabels of
#tuples, pairing elemnets by their positions.
#examples
#1.converting dictionary
d = dict(name = "aarvika",age = 5,city = "hyderabad")
print(d)

#create a dictionary from two lists
keys = ["name","age","city"]
values = ["shreyansh",7,"hyderabad"]
d = dict(zip(keys,values))
print(d)

# 4keys,2values
keys = ["name","city","age","hobbies"]
values = ["siddu","hyderabad"]
d = dict(zip(keys,values))
print(d)

# 2keys, 4values
keys = ["name","city"]
values = ["akash","hyderabad","telangana","karnataka"]
d = dict(zip(keys,values))
print(d)

#duplicate keys,values
fruits = ["Apple","banana","orange","Apple","pineapple"]
colors = ["red","yellow","orange"]
d = dict(zip(fruits,colors))
print(d)


#duplicate values,keys
vegetables = ["tomato","potato","brinjal","carrot"]
colors = ["red","red","orange"]
d = dict(zip(vegetables,colors))
print(d)

#update dictionary
marks = [90,80,70,77,88,88]
subjects =['english','maths','telugu','hindi','evs''ccs']
student = {"a":1}
student.update(zip(marks,subjects))
print(student)





