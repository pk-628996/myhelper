"""functions commonly used in other snips"""

__all__ = [
    "generate_random_string",
    "hbs",
    "make_filename_safe",
    "do_it_async"
    ]
__author__ = "Prince Kumar"
__version__ = "0.1.0-alpha"

import re 
import random
import string
import asyncio
import time
import math
import os 

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def hhmmss(secs):
    hh, secs = divmod(secs, 3600)
    mm, ss = divmod(secs, 60)
    return f'{hh}:{mm:02}:{ss:02}'



def hbs(bytes_num):
    """
    Convert bytes to a human-readable format with dynamic precision.
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    index = 0
    while bytes_num >= 1024 and index < len(suffixes) - 1:
        bytes_num /= 1024.0
        index += 1
    # Format the number with 2 decimal places if it's not an integer,
    # otherwise format it without decimal places
    formatted_num = "{:.2f}".format(bytes_num) if bytes_num % 1 != 0 else "{:.0f}".format(bytes_num)
    return f"{formatted_num} {suffixes[index]}"
    

def make_filename_safe(filename):
    # Replace characters that are not acceptable with an underscore
    safe_filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
    return safe_filename

async def do_it_async(func,*args,**kwargs):
    if not asyncio.get_event_loop().is_running():
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
    else:
      loop = asyncio.get_event_loop()
    # Run the synchronous function in a separate thread
    return await loop.run_in_executor(None,func,*args,**kwargs)


def progress(current,total,start,**kwargs):
    now=time.time()
    diff=now-start
    percent = current / total * 100 
    if diff > 0:
        speed = current / diff 
        time_to_completion = (total - current) / speed
        bead_downloaded = "⬢"
        bead_not_downloaded = "⬡"
        cols=22
        ond=100/(cols-2)
        progress_bar="[{}{}]".format(
            "".join([bead_downloaded for i in range(math.floor(percent/ond))]),
            "".join([bead_not_downloaded for i in range((cols-2) - math.floor(percent/ond))])
            )
        print(f"Downloaded {hbs(current)} of {hbs(total)} at {hbs(speed)}/s\nElapsed: {diff:.2f}s {percent:.2f}% {progress_bar}\nTime remaining: {time_to_completion:.2f}s")
