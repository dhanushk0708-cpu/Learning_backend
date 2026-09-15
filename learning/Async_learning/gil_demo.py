import time
from threading import Thread


def heavy_task(name):
    print(f"{name} started")

    total = 0

    for i in range(50_000_000):
        total += i

    print(f"{name} finished")


if __name__ == "__main__":
    start = time.time()

    t1 = Thread(target=heavy_task, args=("Task A",))
    t2 = Thread(target=heavy_task, args=("Task B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")