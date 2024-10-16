#   Multithreading 
##  When to use Multithreading
### I/O bound tasks

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print("Number :",i)

def print_letter():
    for letter in "acbdefj":
        time.sleep(2)
        print(f"letters : {letter}")

# create Two threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()

# print_number()
# print_letter() #24sec

# start the thread
t1.start()
t2.start() # 14sec

### wait fro the threads to complete
t1.join()
t2.join()

finished_time = time.time()-t
print(finished_time)