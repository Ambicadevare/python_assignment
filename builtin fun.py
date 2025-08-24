# string immutable

# case_conversion_built_in function.
#lower , upper, islower,isupper,swapcase, len, captlize,count
#index----for list and strong


#tittle()fun converts the first letter of each word to uppercase.
a = "ambica hospet"
print(a.title())    #Ambica Hospet


#intersection---- means finding the common elements between two (or more) sets.
A = {1, 2, 3, 4 ,5 }
B = {2, 7 , 8 , 9 , 1}
print(A.intersection(B)) #{1,2}

#strings and lists dont have a direct .intersection() method, but you can convert them to sets first:
s1 = "ambica"
s2 = "akash"
common = set(s1).intersection(s2)
print(common)                           #a


#swapcase---change upper to lower lower to upper
a = "aarvIKa"
print(a.swapcase())      #AARvikA



#captitalize--- it converts the first character of the string to uppercase 
#the rest of the string becomes lowercase
#it doesnt change the original string beacause strings are immutable.
text1 = "ambica is a good Girl"
print(text1.capitalize())   #Ambica is a good girl


#isupper---  it checks if all the alphabetic characters in a string are uppercase.
#Returns  a boolean value:
#True-- if all letters are uppercase
#False-- if all letters are lowercase
a = "shreayansh"
print(a.isupper())    #false


#islower--- it checks if all the alphabetic charcters in a string are lowercase or not.
#Returns  a boolean value
b="aarvika"
print(b.islower())         #True


#lowercase--it returns all string in charcters to lowercase
a = "AMBICA"
print(a.lower())    #ambica


#uppercase()
a = "ambica"
print(a.upper())     #AMBICA


#len---it returns the number of items in:
#a string--- number of characters
#a list/tuple/set/dict---number of elemnts
#any iterable that supports length
text= "shreyansh"
print(len(text))   #9


#trimming and replacing builtin fun
#strip,rstrip,lstrip,replace

#strip--to remove extra spaces
#assign then print
a="    ambica  "
s = a.strip()
print(s)

#rstip--right strp means to removes spcaes from right side
a = "     ambica   "
s = a.rstrip()
print(s)          #    ambica


#lstrip--to remove spcaes from left side
a = "   ambica   "
s = a.strip()
print(s)        #ambica


#it returns a new string where all occurebces of a substring are replaced with another substring
#to replace old value to new value 
#replace(old,"new")
#if w e replace the word with other word which is there in given string it wont give  error
#but it just run the code without any op or error
a = "ambica"
a = a.replace("ambica","hospet")
print(a)      #hospet


#find--- where the elemnt is present in which index
str1 = "ambica"
print(str1.find("b"))     #3


#startswith()---we get true or false if the word starts with same
str1 = "ambica"
print(str1.startswith('a'))


#endswith()-- we get true or false if the word ends with with same
str1 = "ambica"
print(str1.endswith('ica'))


##split() fun it split each element
num1 = input("enter nums: ")
print(num1.split("."))         



#split()  it split each element
num1 = input("enter nums: ")
print(num1.split(","))        #['2','3','4','5','7']
#if we use it without map it convert into list 
#input ("enter all csv format num:").split(",")---list
#(map((float,input("enter all csv format num:").split(","))))------ we get 
#split() fun it split e       
a = num1,num2,num3 = (list(map(float,input("enter all csv format num:").split(','))))
print(a)
#
print("how r yu ambica".split('.'))


#jion
list1 = ["1","2","3","4","hi"]
encoded_string = "." .join(list1)
print(encoded_sting)













