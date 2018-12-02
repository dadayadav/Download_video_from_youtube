#Scap the site link
import random
import requests
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.request import urlopen


youtube = "https://www.youtube.com/playlist?list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D"
url = requests.get(youtube)
page = url.text
siraj=BeautifulSoup(page,'html.parser')
print(siraj.prettify())


video_link = []
video_name = []
res=soup.find_all('a',{'class':'pl-video-title-link'})
for l in res:
    a = "https://www.youtube.com" + l.get("href")
    video_link.append(a)
    video_name.append(l.text)



for i in video_link:
    print(i)


# Download the video


import os
from pytube import YouTube
def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


path = r'F:\Winter pack\Introduction to Game Development\machinelearningin3\Siraj Raval\Introduction to mathematics'
for i in range(11,len(video_link)):
    try:
        downloadYouTube(video_link[i],path)
        print("complete video: " + video_name[i])
    except RegexMatchError:
        print("video cannot be downloaded due to RegexMatchError: " + video_name[i])
        pass
