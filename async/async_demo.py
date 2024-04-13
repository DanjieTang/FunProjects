import asyncio

async def short_delay_long_processing(number):
    print(number)
    await asyncio.sleep(0.1)
    for i in range(1000000000):
        number = i
    print(number)
        
async def long_delay_short_processing(number):
    print(number)
    await asyncio.sleep(0.2)
    print(number)

async def main():
    print("Started")

    # Run two 'say_after' coroutines concurrently:
    await asyncio.gather(
        short_delay_long_processing(1),
        long_delay_short_processing(2),
        long_delay_short_processing(3),
        long_delay_short_processing(4)
    )

    print("Finished")

# Run the main coroutine
asyncio.run(main())