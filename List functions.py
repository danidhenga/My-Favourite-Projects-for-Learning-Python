#LIST FUNCTIONS
lucky_numbers = [4, 8, 15, 16, 23, 23, 42]
family = ["Tangeni", "Linda", "Bonny", "Pandeni", "Pandeni", "Jeanne"]

#create a copy of a list
family2 = family.copy()
print(family.insert(0, "1"))
#connect two lists together with ".Extend"; could also add another word or number instead
family.extend(lucky_numbers)
print(family)
#add item to end of list with ".append"
family.append("Helvi")
print(family)
#Add to specific part of list with ".insert"
family.insert(3, "GYM")
print(family)
#remove something from the list:
family.remove("GYM")
family.remove("1")
family.remove("Helvi")
print(family)
#clear EVERYTHING from list:
family.clear()
print(family)
#.pop removes last element from a list
lucky_numbers.pop()
print(lucky_numbers)
#.index allows you to find out if something is actually in the list
print(lucky_numbers.index(16))
#.count number of times a word appears in a list
print(lucky_numbers.count(23))
#.sort for alphabetical order or numerical order in ascending order, (.reverse to reverse order)
#print a copy
print(family2)