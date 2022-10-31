from importlib.resources import path
import os
from pathlib import Path
from pytube import Playlist
from pytube import YouTube
#from moviepy.editor import *
# yt.py -s -v
# yt.py -s -a
# yt.py -s -t
# yt.py -s -c


def folderCreate(outputFolder):
    home = str(f"{Path.home()}\Downloads\{outputFolder}")
    if os.path.isdir(home) == False:
        os.system(f"mkdir {home}")


class SingleVid:
    def __init__(self,url):
        self.url =url
        self.yt = YouTube(self.url)
        self.home = str(f"{Path.home()}\Downloads\ytdownloads")

    def vid(self):
        title = self.yt.title
        if os.path.isdir(str(f"{Path.home()}\Downloads\ytdownloads")) == False:
            folderCreate("ytdownloads")
        self.yt.streams.get_highest_resolution().download(output_path = self.home)
     
    def audio(self):
        t=self.yt.streams.filter(only_audio =True).first().download()
        thisFile = self.yt.title+".mp4"
        base = os.path.splitext(thisFile)[0]
        os.rename(thisFile, base + ".mp3")
        print(thisFile)
      
       
       


def playList():
    outputFolder = input("Playlist folder name : ")
    playlist = Playlist(input("Playlist link: "))
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    i =1
    home=str(f"{Path.home()}\Downloads\ytdownloads\{outputFolder}")
    for video in playlist.videos:
        video.streams.first().download(output_path=home)
        print(f"vid {i} complete")
        i = i+1
        print(f"All videos are in {home} ")



playList()