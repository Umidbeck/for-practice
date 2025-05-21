def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(100)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

squares_gen = (x ** 2 for x in range(5))
for square in squares_gen:
    print(square)

import asyncio

async def say_hello():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Goodbye, world!")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())

import multiprocessing

def square(n):
    return n * n
def main():
    nums = range(5+1)
    with multiprocessing.Pool() as pool:
        results = pool.map(square, nums)
    print(results)


if __name__ == '__main__':
    main()


import multiprocessing
import time
import os

def square(n):
    print(f" Process {os.getpid()}: is calculating square of {n}")
    time.sleep(2)
    return n * n

def main():
    start = time.time()

    nums = range(5+1)
    with multiprocessing.Pool() as pool:
        results = pool.map(square, nums)

    end = time.time()
    print("Natija:", results)
    print(f"Umumiy vaqt: {end - start:2f} soniya")

if __name__ == "__main__":
    main()


def daraja(n):
    print(f" Process {os.getpid()}: is calculating square of {n}")
    return n * n

def main():
    start = time.time()
    raqamlar = [1,2,3,4,5]
    result = map(daraja, raqamlar)

    end = time.time()
    print("Natija:", list(result))
    print(f"Umumiy vaqt: {end - start:2f} soniya")

if __name__ == "__main__":
    main()

def tugadi():
    print('Vazifa tugadi')

def bajar(callback):
    print("Nima ishlar qilayaidi...")
    callback()

bajar(tugadi)

import sys
# lst = [i for i in range(1000000)]
# gen = (i for i in range(1000000))

# print(sys.getsizeof(lst))
# print(sys.getsizeof(gen))


def  cheksiz():
    n = 0
    while True:
        yield n
        n += 1

# g = cheksiz()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

