import pytube
link= input("enter the link of the playlist\n")
pl= pytube.Playlist(link)
print("downloading...")
pl.download_all()
print("done")
##the downloads are stored in the directory of this code file
