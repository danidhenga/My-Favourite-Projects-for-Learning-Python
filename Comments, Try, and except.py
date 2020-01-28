#Comments
# Are lines that aren't rendered
#Use hashtag or tripple quotes
'''an example'''

'''Try / Except Lesson'''

#instead of the whole program crashing, use try and except
try:
    number = int(input("Enter a Number: "))
    print(number)
#You can specify error type below:
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Invalid input")