# DICTIONARY AND SET

# DICTIONARY IN PYTHON
    # Dictionary are you to store data values in key:value pair
    # They are unordered, mutable(changeable) & don't allow duplicate keys

# info = {
#     "name" : "ahmed",
#     "age" : 23,
# } 
# print(info)

# # info["key"]="value" # To Assign or Add New
# info["age"] = 21
# print(info)

myDict = {
    "name" : "Ahmed",
    "score":{
        "chem" : 98,
        "phy" : 97,
        "math" : 90
    }
}

# print(list(myDict)) to convert dictionary in list []

# DICTIONARY METHODS

#  myDict.keys() TO GET ALL KEYS
# print(myDict.keys())

#  myDict.values() TO GET ALL VALUES
# print(myDict.values())

#  myDict.items() return all (key,val) pairs as tuples
# print(myDict.items())

#  myDict.get() return the key according to valu
# print(myDict.get("name"))

# SET IN PYTHON
    # Set is a collection of unordered items.
    # Each element in the set must be unique and immutable

# collection = {1,2,2,23,3,4,"hello","Hello"}
# print(collection)

# TO CREATE EMPTY SET
    # set()

# collection = {1,2,3,4,5,6}
# print(type(collection))

# SET METHODS

# set.add() add an element
# collection.add(3)
# print(collection)

# set.remove() remove an element
# collection.remove(1)
# print(collection)

# set.clear() empty the set
# collection.clear()
# print(collection)


# set.pop() removes a random value
# collection.pop()
# print(collection)


# set.union() combines both set values & return new

# set1 = {1,2,2,3}
# set2 = {1,2,3,4}

# print(set1.union(set2))


# set.intersection() combines comman values & return new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2))
