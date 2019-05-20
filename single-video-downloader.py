import pytube

##for single video
link=input("please enter the link\n")
yt=pytube.YouTube(link)
videos= yt.streams.all()
count=0
for video in videos:
    print(str(count)+".",video)
    count+=1
number = int(input("enter the number of the video to download\n"))
print("downloading...\n")
videos[number].download()
print("done")

