import asyncio

async def short_delay_long_processing(number):
    print(number)
    await asyncio.sleep(0.1)
    await asyncio.gather(
        long_delay_short_processing(10),
        long_delay_short_processing(20),
        long_delay_short_processing(30),
    )
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