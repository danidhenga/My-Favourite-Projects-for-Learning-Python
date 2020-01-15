#Return statments

def cube(num):
    return num*num*num

print(cube(3))

#Pull the result of the equation
result = cube(4)
print(result)

#If Statements

#boolean variables
is_male = False
is_tall = False
#or operator
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male nor tall")
is_male = True
is_tall = True
#and operator
if is_male and is_tall:
    print("you are a tall male")
else:
    print("you are either not male or tall or both")


#elif situation
print("-------Elif section-------")
is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are tall and female")
else:
    print("you are a short female")

#COMPARISSON LESSON
#pull largest number from a function
#(!= not equal to); (== - equal to)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(1, 2, 3))
