import subprocess, os, wget, zipfile

if not os.path.exists("./ffmpeg.zip"):
    print("[下載 ffmpeg]")
    wget.download(
        "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip",
        "./ffmpeg.zip",
    )


with zipfile.ZipFile('./ffmpeg.zip', 'r') as zf:
        # 解壓縮
    print('[解壓縮 zip]')
    zf.extractall(path='./')

        # 更改資料夾名稱
    os.rename(zf.namelist()[0], './ffmpeg')
