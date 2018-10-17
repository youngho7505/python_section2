import pytube
import os
import subprocess


yt = pytube.YouTube("https://youtu.be/K60dJKmoMMY?list=PLWPSsh-_scwSUsyYMNu0jxUFyxS0ghB5r") #다운 받을 동영상 url 지정

videos = yt.streams.all()

for i in range(len(videos)): #range(1,6) 1,2,3,4,5  # range(6) 0,1,2,3,4,5
    print(i, ',' , videos[i])

down_dir = "e:\youtube"

sNum = int(input("select num : "))
videos[sNum].download(down_dir)

newFileName = input("변환할 파일명은?")
oriFileName = videos[sNum].default_filename

subprocess.call(['ffmpeg','-i',
                os.path.join(down_dir, oriFileName),
                os.path.join(down_dir, newFileName)])

print('다운로드 및 mp3 변환완료!')
