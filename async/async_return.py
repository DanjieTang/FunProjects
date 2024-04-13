import asyncio

async def dummy(num: int) -> int:
    return num

async def main():
    output = await asyncio.gather(
        dummy(2),
        dummy(2),
        dummy(3),
        dummy(4)
    )
    print(type(output))

asyncio.run(main())