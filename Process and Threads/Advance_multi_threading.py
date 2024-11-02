## Multithreading with thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number : {number}"

numbers = [1,2,3,4,5,6,7,8,9,3,44,4,3,3,3,4,4,5,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)
    
for result in results:
    print(result)