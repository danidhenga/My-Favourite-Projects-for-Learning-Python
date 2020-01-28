from Chef import Chef
from Italian_Chef import italian_Chef

#Use "CHEF.PY" as the main source for this lesson

#Instead of copy/pasting all commands, the Italian chef will simply inherit the info from the original chef.py file
'''Only need to add one special dish'''

myChef = Chef()
myChef.make_chicken()

myChef2 = italian_Chef()
myChef2.make_lasagna()