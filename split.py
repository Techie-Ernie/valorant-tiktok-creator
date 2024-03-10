import os
import glob 
import subprocess
from moviepy.editor import *
from edit import make_video
from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend

channel = input("Channel: ")

os.system('cd clips/')
os.system(f'TMP=clips/ twitch-dl clips {channel} --download --period last_month')
#output_json = subprocess.check_output(f'twitch-dl clips {channel} --period last_month --json', shell=True)

os.system('mv *.mp4 clips/')
files = glob.glob('clips/*')
mp4_files = [file for file in files if file.endswith('.mp4')]

for file in mp4_files:
    make_video(file) 
    try:
        # Removing temp files
        os.remove(f'{file}') 
        os.remove(f'{file.split('.')[0]}_bg.mp4')
        
        # Upload file to TikTok: NOT WORKING CURRENTLY, WILL FIX SOON
        videos = [{'path': f, 'description': '#valorant #vct #masters #champions'} for f in mp4_files]
        auth = AuthBackend(cookies='cookies.txt')
        upload_videos(videos=videos, auth=auth)

        
    except:
        pass # If the video is too short, _bg file will not be created, no need to delete

