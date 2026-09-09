''' for measuring the time for execution we can simply use time module and subtract the time and the starting with the time at the
ending
'''
# for example 
import time
start=time.time()
list=[i for i in range(1,101,2)]
print(list)
stop=time.time()
print("TOTAL TIME TAKEN",stop-start)

## 1. this method isn't used in industries bcoz every machine has a different specs so it will take different amount of time in every
#      machine to run this code so we cant measure the actual time of the program
#  2. if u use the while instead of for loop then the time changes but the algorithm is still same

