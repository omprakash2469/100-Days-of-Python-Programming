"""
Multithreading
----
Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python. 
"""

import threading, time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()

    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2 - time1)



def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 1)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        args = [i for i in range(10)]
        results = executor.map(func, args)
        for result in results:
            print(result)


poolingDemo()