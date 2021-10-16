from pytube import YouTube

yt = YouTube("https://www.youtube.com")
yt = yt('mp4', '144p', '250p', '360p', '480p', '720p', '1080p')
