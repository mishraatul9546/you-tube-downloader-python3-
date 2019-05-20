import pytube

##for single video
link=input("please enter the link")
yt=pytube.YouTube(link)
videos= yt.streams.all()  #shows all available formats

#if this destination is ignored, saves into the directory where this code file is present.
destination= input("enter the path of destination folder")
videos.download(destination)
print("done")

####for full playlist
##pl= pytube.Playlist("https://www.youtube.com/playlist?list=PLVuQBUGB87-gomoG36CV4wMZCkGPGKw3p")
##pl.download_all()
