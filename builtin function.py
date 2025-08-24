print(ord("a"))
print(ord("S"))
#check strings is lower or upper case
#case converstion inbuilt functions
s="A" 
print(s.isupper())
s="ambica"
print(s.isupper())
s="Sravan"
print(s.swapcase())
s="sRAVAN"
print(s.swapcase())
s="ambica"
print(s.title())
s="ambica is a good girl"
print(s.title())
#it just to convert first char of first word in a string
s="shreyansh"
print(s.capitalize())
s="  ambica"
s=s.strip()
print(s.capitalize())
#Trimming and replacing built in function
#s.strip()
#TO remove excess space in a string(starting,ending)
s="  ambica "
#to remove excess spaces at start of string
s.lstrip()
#to remove excess spaces at end of string
s.rstrip() 
s="iam a java student"
 # to repalce a word or a char in a string
# s.replace("java","python")
s="iam a java student"
print(s.replace("java","python"))

#joins 
list1= ["1","4","66","hi"]
encode_str = ".".join(list1)
print(encode_str)

#discard
s= {1,4,5,6}
s.discard(7)
print(s)

#pop
s={1,2,3}
s.pop()
print(s)


#intersection


s1={}


#isdisjoint set
Returns True if the sets have no elements 