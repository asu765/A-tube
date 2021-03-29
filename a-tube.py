from pytube import YouTube


yellow = '\033[93m'
green = '\033[92m'
red = '\033[91m'
b = '\033[1m'
print (red+b+"""


       
 
 █████╗    ████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗   ╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║█████╗██║   ██║   ██║██████╔╝█████╗  
██╔══██║╚════╝██║   ██║   ██║██╔══██╗██╔══╝  
██║  ██║      ██║   ╚██████╔╝██████╔╝███████╗
╚═╝  ╚═╝      ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                             
     
                                                          
"""+b+red)

print (green+b+" <===[ coed by Asif lone]===>"+b+green)
print (yellow+b+"<===( YOUTUBE==> Techno Lone )===>"+b+yellow)

YouTube(input("Please enter video link")).streams.first().download()
yt = YouTube(input("enter"))
yt.streams
....filter(progressive=True, file_extension='mp4')
... .order_by('resolution')
... .desc()
... .first()
... .download()