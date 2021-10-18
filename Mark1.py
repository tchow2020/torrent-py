from pytube import YouTube
from pytube.cli import on_progress


YouTube('https://youtu.be/7aBtZUSBwoQ').streams.get_highest_resolution().download()
yt = YouTube('https://youtu.be/7aBtZUSBwoQ')
yt.streams
