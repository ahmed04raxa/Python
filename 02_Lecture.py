# STRING
# String is a data type that stores a sequence of characters.
# Escape Sequence Characters \n etc.

# BASIC OPERATIONS

# CONCATENATION
    # "Hello" + "World" => "Hello World"

# str1 = "Ahmed"
# str2 = " Raza"
# str3 = str1 + str2
# print(str3)
# LENGTH OF STRING
# print(len(str3))


# INDEXING
# str = "Ahmed Raza"
# ch = str[6]
# print(ch)


# SLICING | MOSTLY WE USE THIS IN ML => MACHINE LEARNING
    # Accessing parts of a string
# str[ starting_idx : ending_id] # ending idx is not included

# str = "Ahmed Raza"
# print(str[6:9])


# STRING FUNCTIONS

# str = "i am A Coder"
# print(str.endswith("der")) # TRUE, FALSE
# print(str.capitalize()) # capitilize First Character
# print(str.replace("e","1")) # replace all occurance of old
# print(str.find("a")) # return 1st index of 1st occurer
# print(str.count("am")) # counts the occurance of substr


# name = input("Enter Your Name : ")
# occurance = name.count("a")
# print(occurance)


# CONDITIONAL STATEMENTS
    # if-elif-else ( SYNTAX | RULES OF PROGRAMMING )

# light = ""

# if(light == "red") :
#     print("Stop")
    
# elif (light == "green") :
#     print("Go")
# elif (light == "yellow") :
#     print("Look")
# else:
    # print("Light Is Broken")


# age = 17

# if(age>=18):
#     print("Can Vote")
#     print("& Apply For Driving License") # INDENTATION
# else :
    # print("Your Under 18")

# marks = 50

# if(marks>= 90):
#     print("Grade A")
# elif(marks>= 80):
#     print("Grade B")
# elif(marks>=70) :
#     print("Grade C")
# else :
#     print("Grade D")