# formal-dinner-seating
This is code written in Python to produce a csv list of randomized formal dinner assignments, including 31 waiters, 7 kitchen crew, and 252 students seated at tables.  
This code references a given csv file that includes a list of 290 student names from the 2018-2019 Cate School Academic year.
The kitchen, waiting, and seating assignments are completely random every time — the code does not take grade or previous assignments into account as of yet.
One of the main components of the code, random.sample, was found on stackoverflow and randomly selects a certain number of values from a specified list.  In this case, random.sample was used to randomly sample firstly from the entire list to select 31 waiters, then from the list of remaining names after waiter selection to assign kitchen crew, then from the list of remaining names after waiting and kitchen selection to assign table seating.
I worked with Kenzie, Kenzie's mom, and Will on this assignment.
