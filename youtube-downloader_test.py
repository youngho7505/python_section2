import pytube
import os
import subprocess

movieUrl = input('동영상 주소를 입력하세요!')
yt = pytube.YouTube(movieUrl)
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, '-',videos[i])

sNum = int(input('다운받을 비디오 번호는'))

down_dir = 'e:\youtube'
videos[sNum].download(down_dir)

orgFileName = videos[sNum].default_filename

qs = input('파일을 mp3로 추출하시겠습니까?(y/n)')
if qs.lower() == 'y':
    newFileName = input('변환하실 파일명은?')
    subprocess.call(['ffmpeg',
                 '-i',
                 os.path.join(down_dir, orgFileName),
                 os.path.join(down_dir, newFileName)
                 ])

print('동영상 다운로드 및 mp3 번환완료!')
