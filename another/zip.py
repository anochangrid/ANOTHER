import os, zipfile, wget

# 存放路徑 (將解壓縮的內容另存到這裡)
path_folder = './files'

if not os.path.exists(path_folder):
    os.makedirs(path_folder)

try:
    pass
except Exception as err:
    print("zip 無法開啟",err)
else:
    print('zip 解壓縮成功')

try:
    with zipfile.ZipFile("./ffmpeg")
    try:
        pass:
    except:
        pass
    