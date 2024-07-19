### More in List 
# lst = ["apple","banana","cherry"]
# lst.insert(2,"mango")
# print(lst)

# lst = ["apple","banana","cherry"]
# lst.append("orange")
# print(lst)

# lst1 = ["apple","banana","cherry"]
# lst2 = ["orange","watermelon"]
# lst1.extend(lst2)
# print(lst1)

# lst = ["apple","banana","cherry"]
# lst.remove("apple")   
# print(lst)

# lst = ["apple","banana","cherry"]
# lst.pop(1)
# print(lst)


# lst = ["apple","banana","cherry"]
# lst.pop()
# print(lst)

# lst = ["apple","banana","cherry"]
# lst.clear()
# print(lst)

## sort() asc , desc 

# lst = ["apple","banana","cherry","pineapple","melon"]
# lst.sort()                             #--> default sorting jo hoti hai wo ascending order me hoti hai
# print(lst)


# lst = ["apple","banana","cherry","pineapple","melon"]
# lst.sort(reverse=True)                             
# print(lst)

# lst = ["apple","cherry","banana","pineapple","melon"]
# lst.reverse()
# print(lst)


## join list 

# lst1 = ["a",'b',"c"]
# lst2 = ["z","x","d"]
# lst3 = lst1 + lst2
# print(lst3)


# append , clear,count,extend,reverse,sort,pop,insert



### TUPLEEEE --> ordered,unchangeable,allow duplicate values and you can store any data type in it.

# tpl = ("black","green","red","black",22,22.67,True)
# print(len(tpl))
# print(type(tpl))

## one more way of creating tuple
# tuple constructor
# tpl = tuple(("red","black",'green'))
# print(type(tpl))

# tpl = ("red",)                ##single value ki tuple kaise create karte hai
# print(type(tpl))

# x = ('red',"black","green")
# y = list(x)
# y[1]= "brown"
# x = tuple(y)
# print(x)
# print(type(x))

# x = ('red',"black","green")
# y = list(x)
# y.append("blue")
# x = tuple(y)
# print(x)
# print(type(x))


## join tuples

# tpl1= ("red",1,"black")
# tpl2 = ("blue","greeen")
# tpl3 = tpl1 + tpl2
# print(tpl3)


### set --> unorderd, unchangeable and do not allow duplicate values 
 
# st = {"red","black","blue",True,"red",1}
# print(st)
# print(type(st))


# true 1 
#false 0 

## list constructor
##set # intersection

# set1 = {"python","code","class"}
# set1.add("c")
# print(set1)

# set1 = {"python","code","class"}
# set1.remove("class")
# print(set1)

# set1 = {"python","class"}
# set2 = {"code","jave"}
# set1.update(set2)
# print(set1)

# set1 = {"python","class"}
# set2 = {"code","jave"}
# output = set1.union(set2)
# print(output)

# set1 = {"python","class","code","java"}
# set1.pop()    # randomly removes any item 
# print(set1)

# set1 = {"python","class","code","java"}
# set1.remove("code")    
# print(set1)

