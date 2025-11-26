# FILE I/O In PYTHON |  I/O => Inout & Output
    # Python can be used to perofrm operation on a file. (read & write data)

# TYPES OF ALL FILES
# 1. Text File : .txt, docx, .log, etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc

# Open, read and close File
    # We have to open a file nefore reading or writing

# f = open("file_name","mode")

# f = open("demo.txt",'r')
# data = f.read() # reads entire file
# # data = f.readline() # reads one line at a time
# print(data)
# f.close()

# WRITING TO A FILE

# f = open("demo.txt","w")
# data = f.write("This Is A New Line") # overwrites the entire File
# print(data) 
 
# f = open("demo.txt","a")
# data = f.write("\n This Is A New Line 2") # Adds to the file
# print(data)


import os
