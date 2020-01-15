#Tuples ******can't change once created******
#it would be a list if brackets are used

#use coordinates x,y
coordinates = [4, 5]
print(coordinates[1])

#end-clear work
coordinates.clear()
print(coordinates)

#Functions Lesson
#use keyword "def", give the function a name
#use indent to tell python what will be inside the function "say_hi"
def say_hi():
    print("Hello User")
#Call/execute function:
say_hi()

#Give parameters to a function, they go inside parentheses
def say_hi(name, age):
    print("Hello " + name + "you are " + str(age))
say_hi("Pandeni, ", 22)