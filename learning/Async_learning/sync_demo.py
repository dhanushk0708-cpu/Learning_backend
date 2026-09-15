import time


def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


start = time.time()

task("Task A")
task("Task B")

end = time.time()

print(f"Total time: {end - start:.2f} seconds")