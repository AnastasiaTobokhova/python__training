import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()
    return all_data

if __name__ == '__main__':
    filenames = ['./file 1.txt', './file 2.txt', './file 3.txt', './file 4.txt']


    # Линейный подход
    start_time = time.time()
    for filename in filenames:
        read_info(filename)  # Линейный вызов
    linear_time = time.time() - start_time
    print(f"Линейный: {linear_time}")

    # Многопроцессный подход
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multi_time = time.time() - start_time
    print(f"Многопроцессный: {multi_time}")
