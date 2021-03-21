import pafy
import youtube_dl

while True :
    command = input("Apakah anda ingin memulai ?[y]/[n]: ")
    if command == "y" :
        url = input("Masukkan url: ")
        video = pafy.new(url)
        Download_Folder = "C:/Users/USER/Downloads/New folder (2)"

        audiostreams = video.audiostreams
        for i in audiostreams : 
            print ("bitrate: %s, ext: %s, size: %0.2fMb" % (i.bitrate, i.extension, i.get_filesize()/1024/1024))

        bestaudio = video.getbestaudio()

        bestaudio.download(filepath = Download_Folder)
    elif command == "n" :
        exit()
    else : 
        print("Masukkan dengan benar")