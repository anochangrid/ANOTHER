import subprocess, os, wget, zipfile

if not os.path.exists("./ffmpeg.zip"):
    print("[下載 ffmpeg]")
    wget.download(
        "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip",
        "./ffmpeg.zip",
    )

if not os.path.exists("./ffmpeg"):
    with zipfile.ZipFile('./ffmpeg.zip', 'r') as zf:
        print('[解壓縮 zip]')
        zf.extractall(path='./')

        os.rename(zf.namelist()[0], './ffmpeg')

import subprocess, os, wget, zipfile



'''
下載工具
'''
# 下載 ffmpeg
if not os.path.exists('./ffmpeg.zip'):
    print('[下載 ffmpeg]')
    wget.download(
        'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip', 
        './ffmpeg.zip'
    )

    # 對 ffmpeg 解壓縮 至 指定路徑
    with zipfile.ZipFile('./ffmpeg.zip', 'r') as zf:
        # 解壓縮
        print('[解壓縮 zip]')
        zf.extractall(path='./')

        # 更改資料夾名稱
        os.rename(zf.namelist()[0], './ffmpeg')

# 下載 yt-dlp
if not os.path.exists('./ffmpeg/bin/yt-dlp.exe'):
    print('[下載 yt-dlp]')
    wget.download(
        'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', 
        './ffmpeg/bin/yt-dlp.exe'
    )



'''
下載影片
'''
# 設定 YouTube 影片 id 和 video 連結
video_id = 't0igPuDjYUE'
video_url = f'https://www.youtube.com/watch?v={video_id}'

# 判斷影片是否已經下載
if not os.path.exists(f'./{video_id}.mp4'):
    # 設定下載影片指令
    cmd = [
        './ffmpeg/bin/yt-dlp.exe',
        video_url,
        '-f', 'w[ext=mp4]', 
        '-o', './%(id)s.%(ext)s'
    ]

    # 執行指令，並取得輸出訊息
    print("[下載影片]")
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'成功')
    else:
        print(f'失敗')

choice = 1

if choice == 1:
    cmd = [
        '/ffmpeg/bin/ffmpeg.exe',
        '-ss',' 00:02:43.000',
        '-i', f'-/{video_id}.mp4',
        '-t', "00:00:24.000",
        "-y",
        "-c",
        'copy',
        "-/output.mp4",
    ]

elif choice == 2:
     cmd = [
        '/ffmpeg/bin/ffmpeg.exe',
        '-i', f'-/{video_id}.mp4',
        '-ss',' 00:02:39.000',
        '-to', "00:03:06.000",
        "-y",
        "-c",
        'copy',
        "-/output.mp4",
    ]
print("[切割影片]")
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'成功')
else:
    print(f'失敗')