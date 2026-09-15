import time
from threading import Thread


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


start = time.time()

t1 = Thread(target=task, args=("Task A",))
t2 = Thread(target=task, args=("Task B",))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time: {end - start:.2f} seconds")