import random
import asyncio


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that takes an arg,
    waits for a random delay between 0 and arg,
    and eventually returns it.

    args: max_delay(int) - maximum random delay value

    return: (int) - randomly generated value
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
