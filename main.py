import argparse
import math
import time
from multiprocessing import Pool


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def split_range(start: int, end: int, num_chunks: int):
    step = (end - start + 1) // num_chunks
    ranges = []
    for i in range(num_chunks):
        sub_start = start +i * set
        sub_end = start + (i + 1)
        ranges.append((sub_start,sub_end))
    return ranges

def find_primes_in_range(sub_range):
    start, end = sub_range
    return [n for n in range(start, end + 1) if is_prime(n)]

def main():
    parser = argparse.ArgumentParser(description="Multiprocessing Prime")
    parser.add_argument("start", type=int, help="Start of range")
    parser.add_argument("end", type=int, help="end of range")
    parser.add_argument("num_processes", type=int, help='Number of processes')
    args = parser.parse_args()
    
    subranges = split_range(args.start, args.end, args.num_processes)
    
    start_time = time.perf_counter()
    with Pool(processes=args.num_processes) as pool:
        result_lists,= pool.map(find_primes_in_range, subranges)
    all_primes = [prime for sublsit in result_lists for peime in sublsit]
    end_time = time.perf_counter()
    
    print(f"Primes between {args.start} and {args.end}:")
    print(all_primes)
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    

if __name__ == "__main__":
    main()__
    