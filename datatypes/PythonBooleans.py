a = 200
b = 33

if a > b:
    print("A is Big")
else:
    print("B is Big")   


#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,    
print(bool("Hello"))
print(bool(15))    

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print("Some Values are False")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("Functions Demo")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))