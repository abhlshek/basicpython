# my_dict = {"apple": 5, "banana": 6, "mango": 8}
# print(my_dict["apple"])
# print(my_dict.get("mangob","Not Found"))
# print(my_dict["banana"])

# my_dict = {"one": 1, "two": 2, "mango": 10, "apple": 11}
# print(my_dict ["one"])
# print(my_dict ["apple"])
# print(my_dict.get("apples","not found"))


# my_dict ={"apple":6,"banana":7,"mango":8}
# apple_value =  my_dict["apple"]
# print(apple_value)
# banana_value = my_dict["banana"]
# print(banana_value)
# mango_value = my_dict["mango"]
# print(mango_value)

# get method ........# (search function)

# my_dict = {"apple": 6, "banana": 7, "mango": 8}
# apple_value = my_dict.get("apple")
# print(apple_value)

# banana_value = my_dict.get("bananas")  # output none
# print(banana_value)
#
# print(my_dict.get("mango"))
# print(my_dict.get("pair"))  #output = none
# print(my_dict.get("pair", 0))

# mango_value = my_dict.get("mangos", "not found")
# print(mango_value)

#adding method ........

# my_dict = {"mango": 1, "orange": 2, "banana": 3}
# my_dict["banana"] = 10
# print(my_dict)
# my_dict["mango"] = 11
# print(my_dict)
# my_dict["orange"] = 12
# print(my_dict)
# my_dict["pair"] = 3
# print(my_dict)
# my_dict["tony"] = 1
# print(my_dict)
# my_dict["mohan"] = 14
# print(my_dict)

# item() method......(iterating)

# my_dict = {"apple":1,"mango":2,"banana":3,"orange":4}
# for key,value in my_dict.items():
#     print(key,value)

# my_dict ={"sushil":11,"abhishek":12,"deepika":13,"sunita":14}
# for key,value in my_dict.items():
#     print(key,value)

# my_dict = {"tree":1,"tony":2,"sony":3,"anita":4}
# for key in my_dict.items():
#     print(key)

# my_dict ={"apple":1,"banana":2,"mango":3}
# print(my_dict.items())


# key,value pair........

# dict() method .......................

# my_dict = dict({"apple":1,"banana":2,"orange":3})
# print(my_dict)

# my_dict = dict({"abhishek": 1, "tony": 2})
# print(my_dict)

# creating dict with keyword argument

# my_dict = dict(apple = 5,banana = 6,orange = 7)
# print(my_dict)

# my_dict = dict(soham = 12, mohan = 13,gopal = 14)
# print(my_dict)

# len() function ............


# my_dict = {"sushama":6,"sunita":7,"gita":8}
# print(len(my_dict))

# my_dict = {"neeraj":5,"deepak":7,"sunil":8,"mamta":9}
# print(len(my_dict))

# keys(),values()  function  ..............

# my_list={"komal":3,"nikhil":4,"priya":5}
# print(my_list.keys())
# print(my_list.values())

# my_dict={"yes":1,"raunak":2,"anil":1}
# print(my_dict.keys())
# print(my_dict.values())

# pop() function .............

# my_dict = {"apple": 1, "banana": 2, "cherry": 3, "orange": 4}
# value = my_dict.pop("apple")/
# print(value)
# print(my_dict)
# value = my_dict.pop("pair",0)
# print(value)

# value = my_dict.pop("orange")
# print(value)
# print(my_dict)
# value = my_dict.pop("cherry")
# print(value)
# print(my_dict)


# update() function ............................

# d={"ram":4}
# my_dict = {"apple": 1, "banana": 2, "cherry": 3}
# value = my_dict.update(d)
# print(my_dict)


result = {1: ["neeraj", 33, 5, 66], 2: ["saurabh", 55, 66, 67], 3: ["sunil", 44, 55, 66]}
print(result)

i = 1
n = 5
while i < n:
    rolln = int(input("enter the roll"))
    search = result.get(rolln)
    print(i)
    i += 1
    print("i=",i)

    if search is None:
        print("not found")
    else:
        total = search[1] + search[2] + search[3]
        print("total", total)
        per = total / 3
        print("per", per)
