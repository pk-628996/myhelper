"""FFMPEG HELPER"""

__all__ = [
    
]
__author__ = "Prince Kumar"
__version__ = "0.1.0-alpha"

import shutil

if not shutil.which('ffmpeg'):
    raise Exception("FFmpeg is not installed. First Make sure that it is installed and is on path")
    
 

