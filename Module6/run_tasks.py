# run_tasks.py

from multiprocessing import Pool, freeze_support
from my_task_module import task

def run():
    names = ["Process 1", "Process 2", "Process 3"]
    with Pool(3) as pool:
        results = pool.map(task, names)

    for result in results:
        print(result)

if __name__ == '__main__':
    freeze_support()  # Required for Windows + multiprocessing
    run()
