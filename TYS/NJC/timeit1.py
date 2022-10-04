# import the built-in library timeit 
import timeit 
# use the function from Task 1.1 to read in 1000 integers from the file THOUSAND.txt 
t1000 = task2_1('THOUSAND.txt')
# use the timeit function to call the task2_2(li) function with the 1000 integer list, run this just once 
time1000 = timeit.timeit(lambda: task2_2(t1000), number=1)
# print out the time, in seconds
print(time1000)
