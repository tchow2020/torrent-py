from pytube import YouTube
yt = YouTube('https://youtu.be/jC0kHsTtzCA')
yt.streams.first().download()
yt = yt('mp4', '480p')