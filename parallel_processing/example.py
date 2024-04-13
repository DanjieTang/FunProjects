from multiprocessing import Pool

def square_number(n):
    return n * n

if __name__ == '__main__':
    # Create a pool of workers
    with Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5]
        # Map 'square_number' to the inputs and collect the output
        results = pool.map(square_number, numbers)
        print(results)