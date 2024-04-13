from multiprocessing import Pool
import time

def square_number(n):
    for i in range(1000000000):
        number = i

if __name__ == '__main__':
    # Sequential
    start_time = time.time()
    for i in range(4):
        square_number(i)
    
    end_time = time.time()
    print(end_time-start_time)
    
    # Create a pool of workers
    start_time = time.time()
    with Pool(processes=4) as pool:
        end_time = time.time()
        print(end_time-start_time)
        numbers = [1, 2, 3, 4]
        # Map 'square_number' to the inputs and collect the output
        results = pool.map(square_number, numbers)
    end_time = time.time()
    print(end_time-start_time)