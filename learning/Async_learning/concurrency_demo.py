import asyncio
import time


async def fetch_data(name, seconds):
    print(f"{name} started")

    await asyncio.sleep(seconds)

    print(f"{name} finished")
    return f"{name} result"


async def main():
    start = time.time()

    results = await asyncio.gather(
        fetch_data("Weather API", 3),
        fetch_data("Payment API", 2),
        fetch_data("User API", 4)
    )

    end = time.time()

    print("Results:", results)
    print(f"Total time: {end - start:.2f} seconds")


asyncio.run(main())