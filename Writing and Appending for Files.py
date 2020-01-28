

#append to "Random File.txt"
#use "w" to overrwrite or create new files
 
employee_file = open("Random File.txt", "a")

employee_file.write("\nKelly - Customer Service")
#*********to add new line of data use "\n"

employee_file.close()

#be careful to not re-run too much when appending