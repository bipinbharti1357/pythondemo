# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

print("By leaving out the start index, the range will start at the first character:")
print("Get the characters from the start to position 5 (not included):")
print(b[:5])
print("=========")
print("Slice To the End")
print("By leaving out the end index, the range will go to the end:")
print("Get the characters from position 2, and all the way to the end:")
print(b[2:])
print("================================")
print("Negative Indexing")
print("Use negative indexes to start the slice from the end of the string:")
#Example
#Get the characters:

#From: "o" in "World!" (position -5)

#To, but not included: "d" in "World!" (position -2):
print(b[-5:-2])





