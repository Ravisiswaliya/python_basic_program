import time
import threading


def squre(numbers):
    print('Calculate Squre Number')
    for n in numbers:
        time.sleep(0.2)
        print('Squre', n*n)

def cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('Cube', n*n*n)

arr = [2,3,8,9]

t = time.time()
#squre(arr)
#cube(arr)

t1 = threading.Thread(target=squre, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()
print("Done")
print(time.time()-t)