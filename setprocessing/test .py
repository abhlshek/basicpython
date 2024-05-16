# a ={1,2,3,4,6,5,4,3,2,1}   # duplicates not allow
# print(a)

# basic operaters:

# add() element.........

# my_set ={1,2,3,4,5,6}
# my_set. add(7)
# print(my_set)
# my_set.add("number")
# print(my_set)
# my_set.add("element")
# print(my_set)
# my_set.add(7)
# print(my_set)

# my_set = {"sushil","sunil","saurabh","sachin"}
# my_set.add("sohan")
# print(my_set)


# remove() and discard()  element.........

# my_set = {1,2,3,4,5,6,7}
# my_set.remove(7)
# my_set.discard(6)
# print(my_set)

# my_set ={"anita","deepika","abhishek","sushil"}
# my_set.remove("anita")
# my_set.discard("sushil")
# print(my_set)


# set operators (union('|'),intersection('&'),difference('-'),and symmetric('^'):

# union('|')......
# set1 = {1,2,3,4,5,6}
# set2 = {3,4,9,8,2,7}
# union_set = set1|set2
# print(union_set)

# set1 = {"ram","sita","gita"}
# set2 = {"sohan","mohan","monu"}
# union_set = set1|set2
# print(union_set)

# intersection('&').....

# set1= {1,2,3,4}
# set2= {5,7,9,2,3,4}
# intersection_set = set1 & set2
# print(intersection_set)

# set1 = {"sohan","mohan","gita","ram"}
# set2 = {"hanuman","ankit","sohan","gita","ram"}
# intersection_set = set1 & set2
# print(intersection_set)

# difference('-') .........

# set1 = {1,2,3,4,5,6,7}
# set2 = {7,8,9,2,3,4,5,6}
# difference_set = set1 - set2
# print(difference_set)
# difference_set = set2-set1
# print(difference_set)


# symmetric('^')...........
# set1 = {1,2,3,4,5,6,7}
# set2 = {5,6,7,8,9,}
# symmetric_set = set1 ^set2
# print(symmetric_set)


# set method ......................
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {5, 6, 7, 8, 9}
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1.difference(set2)
# symmetric_set = set1.symmetric_difference(set2)
# print(union_set)
# print(intersection_set)
# print(difference_set)
# print(symmetric_set)

# is_subset and is_superset.........

# set1 = {1,2,3,4,5}
# set2 = {2,3,5}
# is_subset = set2.issubset(set1)
# print(is_subset)

# set1 = {1,2,3,4,5}
# set2 ={3,4,5}
# is_superset = set1.issuperset(set2)
# print(is_superset)


# frozen_set .....................
frozen_set = frozenset([1,2,3,4])
frozen_set.add(5)
print(frozen_set)