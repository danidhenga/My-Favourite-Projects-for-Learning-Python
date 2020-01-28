#Read from Random File.txt

#use comma and r = read; w = write; a = append (add); r+ = read & write
#store open into variable

employee_file = open("Random File.txt", "r")

#print employeefile.readable to test file
#print employeefile.readline to read first line
#print employeefile.readlines to read specific lines
print(employee_file.readable())

employee_file.close()

'''could create a for loop 
eg. for employee in employee_file.readlines
            print employee:
'''