## Multiprocessing  with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time
def square_number(number):
    time.sleep(0.2)
    return f"square: {number*number}"
numbers = [1,2,3,4,5,5,7,7,9,9,3,12,3,14]

if __name__ =="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)
    
    for result in results:
        print(result)