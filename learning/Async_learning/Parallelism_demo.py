import time
from multiprocessing import Process


def heavy_task(name):
    print(f"{name} started")

    total = 0

    for i in range(50_000_000):
        total += i

    print(f"{name} finished")


if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=heavy_task, args=("Task A",))
    p2 = Process(target=heavy_task, args=("Task B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")