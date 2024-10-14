#!/usr/bin/env python3
""" Basic asynchronous function that demonstrates waiting for a random delay.  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay and returns the delay value.
        
        Args:
            max_delay (int): The maximum possible delay in seconds (default is 10).
                             The function will generate a random delay between 0 and max_delay.
                             
        Returns:
            float: The actual delay time in seconds.
            
        Description:
            - Generates a random float between 0 and the specified max_delay using the random.uniform() function.
            - Uses asyncio.sleep() to asynchronously wait for the random delay.
            - Once the wait is over, the random delay value is returned.
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
