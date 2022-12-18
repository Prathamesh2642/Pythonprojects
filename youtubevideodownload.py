from pytube import YouTube
url=input("Enter the link of the video ")
myvideo=YouTube(url)
print(myvideo.title)
# print(myvideo.thumbnail_url)
# for streams in myvideo.streams:
    # print(streams)
downloadvid=myvideo.streams.get_highest_resolution()
downloadvid.download()
