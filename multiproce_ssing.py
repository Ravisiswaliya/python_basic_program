import multiprocessing

def squre(numbers):
    print('Calculate Squre Number')
    for n in numbers:
        #time.sleep(0.2)
        print('Squre', n*n)

if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=squre, args=(arr))
    p1.start()
    p1.join()
