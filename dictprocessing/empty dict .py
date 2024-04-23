# empty dict().........

employee_data = dict()
employee_data["sushil"] = 2
employee_data["roshan"] = 3
employee_data["suraj"] = 4
print(employee_data)
#
# access value.............

my_dict = {"mango":1,"orange":2,"banana":3,"apple":4}
mango_value = my_dict.get("orange")
apple_value = my_dict.get("apple")
my_dict.keys()
print(my_dict.keys())
print(mango_value)
print(apple_value)
#
# update value and key.........

my_dict = {"deepak":1,"sushil":2,"abhishek":3}
d = {"deepika":4}
value = my_dict.update(d)
print(my_dict)

# dictionary iteration :..........

my_dict = {"maruti":1,"ford":2,"tata":3,"BMW":4}
for key,value in my_dict.items():
    print(key,value)

# deletion .........

my_dict = {"apple":1,"sumsung":2,"nokia":3,"sony":4}
del my_dict["sony"]
print(my_dict)
my_dict.pop("apple")
print(my_dict)




