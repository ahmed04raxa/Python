# LIST IN PYTHON
    # A built-in data type that stores set of value
    # It can store elements of different types (integer, float, string, etc)

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(len(marks))

# STRING ARE IMMUTABLE | UNCHANGEABLE
# LIST ARE MUTUABLE | CHANGEABLE

# students = ["Ahmed", 80, "Karachi"]
# print(students)

# LIST SLICING
    # SIMILAR TO STRING SLICING

# num_list = ["87", "64", "33", "95", "76"]

# print(num_list[0:4])

# LIST METHODS

list = [2,1,3]


# # 1) list.append() # Adds one Element at the end
# list.append(4)
# print(list)

# 2 list.sort() sort in ascending order | 1,2,3,4
# list.sort()
# print(list)

# 3 list.sort(reverse = True) sort in descending order |  4,3,2,1
# list.sort(reverse=True)
# print(list)

# 4 list.reverse() reverse list |  3,1,2
# list.reverse()
# print(list)

# 4 list.insert(idx,el) insert element at index
# list.insert(1,5)
# print(list)

# 5 list.remove() removes first occcurance of element | Jo First Per Mily Ga Usy Remove Kr Dega

# list.remove(2)
# print(list)

# 6 list.pop(idx) removes element at idx

# list.pop(2)
# print(list) 



# TUPLES IN PYTHON
    # A built-in data type that lets us create immutable sequence of values.

# tup = (89,90,92,93,94,95)
# print(tup[0]) 

# TUPLE SLICING
# print(tup[1:3])

# TUPLE METHODS

tup = (1,2,3,4,3,4,5,6,4,3,3,)

# 1. tup.index( el ) return index of first occureance
# print(tup.index(3))

# 2. tup.coun( el ) counts total occurances

# print(tup.count(4))


print("Enter Your 3 Favorite Fruites Name")
first = input("First Name Of Fruit")
print(first)

second = input("Second Name Of Fruit")
print(second)
third = input("Third Name Of Fruit")
print(third)

print([first,second,third])