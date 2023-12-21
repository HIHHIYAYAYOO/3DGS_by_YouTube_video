import os
import argparse
from pytube import YouTube

def gaussian_splatting_by_youtube_video(video_URL, quality, fps):
    main_dir = os.getcwd()
    
    # 指定 YT 網址
    yt = YouTube(video_URL)
    # 篩選影片格式
    stream = yt.streams.filter(subtype='mp4', res=quality).first()

    video_download_folder = f"{main_dir}\\video"
    if not os.path.exists(video_download_folder):
        os.mkdir(video_download_folder)
    
    os.chdir(video_download_folder)

    # 取得影片下載路徑及下載影片
    video_path = stream.download(video_download_folder)
    # 影片標題的空格替換成底線
    safe_title = yt.title.replace(" ", "_")

    os.chdir(main_dir)

    data_input_folder = f"{main_dir}\\data\\{safe_title}\\input"
    if not os.path.exists(data_input_folder):
        os.makedirs(data_input_folder)

    os.chdir(data_input_folder)

    # 透過 ffmpeg 來分割影片
    os.system(f'ffmpeg -i {video_path} -qscale:v 1 -qmin 1 -vf fps={fps} %04d.jpg')
    
    os.chdir(main_dir)

    data_folder = f"{main_dir}\\data\\{safe_title}"
    # 設定環境變數,指定使用的GPU的序號
    os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'
    os.system(f'python convert.py -s {data_folder}')
    # os.system(f'python train.py -s {data_folder}')

# video_URL = "https://youtu.be/_2ntYhxo9OI?si=y0MmTyN1hN_e36Lz"
# quality = "1080p"
# fps = "2"
parser = argparse.ArgumentParser()
parser.add_argument("-url", required = True, help = "YouTube vido URL")
parser.add_argument("-res", default = "1080p", help = "YouTube vido quality")
parser.add_argument("-fps", default = "2", help = "video fps for ffmpeg")
args = parser.parse_args()
gaussian_splatting_by_youtube_video (args.url, args.res, args.fps)
