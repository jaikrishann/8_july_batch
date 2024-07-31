
# var1 = 'Upflairs'
# var2 = "jaiii  ghjkkkkkkkkkkkkkkkkkkkkk,"
# var3= """upflairs .#@#$Y*(*()),sdksa
# ksda
# skadn"""  #-->paragrapghs ya multiline code 

# print(type(var3))

# rupees = 2000 
# print("i have",rupees,"rupees")

# print(rupees)

# company = "UpfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffLairs pvt"
# print(company.upper())
# print(company.lower())
# print(len(company))  #-->length
# print(company.count("f"))


# a = "hello-world"
# print(a.replace("hello","bye"))
# print(a.split("-"))

# college = " manipal "
# print(college.strip())
# print(college.rstrip())
# print(college.lstrip())


#indexing
#   m a n i p a l 
#   0 1 2 3 4 5 6 
# -7 -6 -5 -4 -3 -2 -1 

# slicing 
# college = "manipal"
# print(college[:])     #[start:end:skip/step]
# print(college[4:])
# print(college[-3:])
# print(college[0:5:2])

# quotes ke ander quotes me kuch likhna hai
# print('"My name is jai"')  #---> "" jsdj"" , ''sayfu''

# string concatentaion
# a = "hello"
# b = "world"
# # c = a + b 
# # print(c)

# c = a + " " + b 
# print(c)

# age = 20
# text = "my name is jai,I am of" + age 
# print(text)


# f-string / formatted string

# age = 20
# text = f"my name is jai,I am of {age}"
# print(text)


#Escape characters--> \n,\t
# text = "we are the students of \"datasci\""
# print(text)



### list --> ordered, changenable and allow duplicate values and you can  store and type of data 


# lst= ["apple","banana","cherry"]
# print(lst)
# print(type(lst))

# lst = ["python",True,22,22.34,"python"]
# print(lst)
# print(len(lst))

## accessing particular items 
# fruits = ["apple","banana","cherry","orange",'mango']
# print(fruits[1])
# print(fruits[0])
# print(fruits[-1])
# print(fruits[0:2])

##updating value using indexing
# print(fruits[1])
# fruits[1]="watermelon"
# print(fruits)

# fruits = ["apple","banana","cherry","orange",'mango']
# print(fruits[1:3])
# fruits[1:3]=["blackcurrent","watermelon"]
# print(fruits)


# fruits[1:2]=["blackcurrent","watermelon"]   
# print(fruits)

# fruits[1:3]=["blackcurrent"]   
# print(fruits)








# a = 10.34##

# # print(a,b,c)                        
# print(type(a))                    #type is used to  check data type 



# a = 'upflairs'
# b = "upflairssssssssjadjsa"
# c = """upflairsss
# my
#  name """
# print(type(a))
# print(type(b))
# print(c)

# rupees = 2000
# print("i have",rupees,"rupees")

# name = 'jai'
# print("my name is ",name)


# name = "upflairrrrrrrrrrs pvttt"
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.count("r"))

# name = "hello world"
# print(name.replace("h","b"))
# print(name.split(" "))
# college = "   manipal    "
# print(college.strip())
# print(college.rstrip())
# print(college.lstrip())




#indexing  --> numbering 0 - 9 

# m   a  n   i   p   a   l 
# 0   1   2   3   4   5   6 
# -7 -6   -5  -4  -2  -1


#slicing 
# college = "manipal"
# print(college[0:4])                                #[starting point:ending point:skip/step]
# print(college[::3])
# print(college[0:7])
# print(college[-7:-3])



#quotes ke ander quotes kaise dete hai 
# my name is "jai"
# print('my name is "jai"')      #--> surrondings ke quotes se ander ke quotes match nahi hone chaiye 

#escape characters \n ,\t        

# print("my name is \"jai\" ")         

# a = "hello"          
# b = " world"
# c = a + b 
# print(c)


# a = "hello"          
# b = " world"
# c = a +" ^^^ " + b 
# print(c)



## formatted string ////f- string

# age = 22
# name = "jai"
# # text = "my age is" + age 
# text = f"my age is {age},my name is {name}"       
# print(text)

# list --> ordered, changenable(mutable) and allow duplicate values and you can  store and type of data 


# lst = ["apple","banana","cherry","apple",10,10.34,True]
# print(lst)
# # print(type(lst))
# print(len(lst))

# print(lst[3])
# # print(lst[-3:])
# lst[3] = "red"
# print(lst)

# lst[0:3] = ["black",'blue',"green"]
# print(lst)
# lst[0:3] = ["code",'class']
# print(lst)

# lst[0:3]=["black","blue","red",'green']
# print(lst)

# lst = ["apple","banana","cherry","apple",10,10.34,True]
# lst.insert(5,"code")
# print(lst)

# lst = ["apple","banana","cherry","apple",10,10.34,True]
# lst.append("class")
# print(lst)



## quotes ke ander quotes 
# print("my name is 'JAI'")  #--> surrondings ke quotes se inner wale quotes match nahi hone chaiye 


#escape characters \n \t

# print("my name is \"jai\"")


##string concatenation

# a = "heelo"
# b = " world"
# c = a + b 
# print(c)



# a = "heelo"
# b = "world"
# c = a +" "+ b 
# print(c)



## formatted string //f-string
                                               
# age = 22
# name = "jai"
# # text = "my age is " + age    # 
# text  = f"my age is {age}"
# print(text)


# list --> ordered, changenable(mutable) and allow duplicate values and you can store any type of data 


# lst = [10,"red","black",'zero',10.34,True,"red"]
# print(lst)

# print(type(lst))
# print(len(lst))

# print(lst[2])
# lst[2] = "codde"
# print(lst)

# print(lst[0:4])
# lst[0:2] = ['apple',"banana"]
# lst[0:2] = ['apple',"banana","cherry"]
# lst[0:2] = ['apple']
# print(lst)



# lst = ["red","black",'zero',"green"]
# # lst1 = ["heey","hello"]
# # lst.insert(2,"jai")
# # lst.append("bhai")
# # lst.remove(10)
# # lst.pop(3)
# # lst.pop()
# # lst.clear()
# # lst.reverse()
# # lst.extend(lst1)
# # lst2 = lst.copy()
# lst.sort(reverse=True)
# print(lst)

# TUPLEEEE --> ordered,unchangeable,allow duplicate values and you can store any data type in it.
# tpl = ("hello",10,True,"red","red")
# print(tpl)
# print(type(tpl))
# print(len(tpl))

###tuple constructor
# tpl = tuple(("hello",10,True,"red","red"))
# print(type(tpl))


# ##type casting


# a = "10"
# print(type(a))

# b = float(a)
# print(type(b))





# tpl = ("hello",10,10.367,True,"hello",[1,2,3])
# print(tpl)
# print(type(tpl))
# print(len(tpl))


# tpl = ("hello",)
# print(type(tpl))


#tuple constructor 
# tpl = tuple(("hello",10,10.367,True,"hello",[1,2,3]))
# print(type(tpl))

# type casting
# a = "10"
# b = int(a)
# print(type(b))


# x  = ("heelo","black","red","black")
# # y = list(x)
# # y[2] = "green"
# z = x.count("black")
# # x = tuple(y)
# print(z)
# print(type(x))


# x  = ("heelo","black","red")
# y = list(x)
# y.append("blue")
# x = tuple(y)
# print(x)
# print(type(x))

# join


# set --> unorderd, unchangeable and do not allow duplicate values 

# st = {"hello",10,10.34,True,1,"hello"}
# st1 ={"red","black"}
# st.add("code")
# st.clear()
# st.pop()
# st.remove("hello")
# st.update(st1)
# st.intersection()
# result = st.union(st1)
# print(result)
# print(st)
# print(type(st))
# print(len(st))


# true = 1
# false = 0
