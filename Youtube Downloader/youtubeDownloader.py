import pytube
from pytube import YouTube

path=r"C:\Users\Abhranil\Desktop\youtube"

link = r"https://www.youtube.com/watch?v=SCRbCZ_p_C8&list=RDyIdKbSeAueY&index=3"

try:
    youtube = YouTube(link)
except:
    print("Connection error....")

print(youtube.description)
print()
print(youtube.captions)
print()
print(youtube.length)
print()
print(youtube.title)
print()
print(youtube.streams.all())

stream = youtube.streams.first()
#stream.download()

print(stream.filesize)

