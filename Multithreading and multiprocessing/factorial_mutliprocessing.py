#Multiporcessing for CPU bound tasks
#example:factorial calculations especially for large numbes
#It involves computational work which multiprocessing can be used to distribute the workload across multiple CPU Cores improving performance

import multiprocessing
import math
import sys
import time

#Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#FUNCTION TO COMPUTE FACTORIAL OF A GIVEN NUMBER

def compute_fact(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    return result
if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()

    #create a pool of worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_fact,numbers)
    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time takes: {end_time-start_time} seconds")
