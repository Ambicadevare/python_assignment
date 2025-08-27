
#zip()---The zip function combines two or more iterables(list,tupple,string)into a single iterabels of
#tuples, pairing elemnets by their positions.
#examples
#1.converting dictionary
d = dict(name = "aarvika",age = 5,city = "hyderabad")
print(d)

#create a dictionary from two lists
keys = ["name","age","city"]
values = ["shr eyansh",7,"hyderabad"]
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





