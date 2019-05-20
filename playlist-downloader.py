import pytube
link= input("enter the link of the playlist")
pl= pytube.Playlist(link)
pl.download_all()
##the downloads are stored in the directory of this code file
