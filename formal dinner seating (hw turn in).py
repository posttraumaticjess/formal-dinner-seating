#formal dinner.py
#1/19/2020
#Jess Yang CompSci
#done with kenzie, kenzie's mom, and will d.

#must "import random" to be able to use random.sample to assign random values for seating assignments
import random

# from stackoverflow...
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#declaring list names
student = []
waiter = []
left_over = []
kitchen = []
at_table = []


"""open("Dinner Seating - Student List 2018-19 4.csv") as input_file:
    for each in input_file:
        student.append(each)

"""

try:
    #calling 'file-in'
    with open("Dinner Seating - Student List 2018-19 4.csv") as student_file:
        for line in student_file:
            #find second ',' and store the first and last names only in student list
            npos = find_nth(line,',',2)
            if npos > 0:
                name = line[:npos]
                #print(name)—can convert this from a comment to functioning code to check that the appended list of student names is working properly
                student.append(name)

except IOError as err:
    print("Error =" + str(err))

#num_student = length of the list "student"
num_student = len(student)
#printing num_student and converting to a string
print(str(num_student))

waiter = random.sample(student,31)
print('number of waiters = ' + str(len(waiter)))

#defining left_over as a list made up of the leftover students after subtracting the students from the waiter list
#converting list to set class
#sets are collections of items in no particular order, which is useful for random assignment
left_over = list(set(student).difference(set(waiter)))
num_left = len(left_over)
print(str(num_left))

#using random.sample method from stackoverflow to randomize names assigned to kitchen crew
kitchen = random.sample(left_over, 7)
num_kitchen = len(kitchen)
print(str(num_kitchen))

#defining at_table as a list made up of the leftover students after subtracting the students from the kitchen list
at_table = list(set(left_over).difference(set(kitchen)))
print(str(len(at_table)))

#seating assignments using counter increments
try:
    with open("seating_assignments.csv","w") as output_file:
        for each_student in kitchen:
            print(each_student + ", Kitchen", file=output_file)
        counter = 1
        #table assignments for waiters
        for each_student in waiter:
            scounter = str(counter)
            #must add another , to denote an additional list
            print(each_student + "," + "W" + scounter.zfill(2), file=output_file)
            counter = counter + 1
            #incrementing a counter so that the assignment values change
            if counter > 31:
                counter = 1
        for each_student in at_table:
            print(each_student + "," + str(counter), file=output_file)
            counter = counter + 1
            if counter > 31:
                counter = 1
            
except IOError as err:
    print("IO Error writing student file:" + str(err))
