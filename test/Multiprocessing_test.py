import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

do_something(1)




finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')