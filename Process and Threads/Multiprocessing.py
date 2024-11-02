#Processes that run in parallel
## CPU-Bound Tasks-Tasks that are heavy on CPU usage
## Parallel execution - Multiple cores of the CPU

import time
import multiprocessing

def square_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube:{i*i*i}")


if __name__ == "__main__":
#create two processes
        p1 = multiprocessing.Process(target=square_numbers)
        p2 = multiprocessing.Process(target=cube_numbers)
        t = time.time()
        ## start the process
        p1.start()
        p2.start()

        #wait for the threads to complete
        p1.join()
        p2.join()

        finished_time = time.time()-t
        print(finished_time)
