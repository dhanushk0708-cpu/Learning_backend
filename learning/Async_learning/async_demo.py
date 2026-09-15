import asyncio
import time


async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished")


async def main():
    start = time.time()

    await task("Task A")
    await task("Task B")

    end = time.time()

    print(f"Total time: {end - start:.2f} seconds")


asyncio.run(main())

# without gather, the tasks are executed sequentially, resulting in a total time of approximately 4 seconds.