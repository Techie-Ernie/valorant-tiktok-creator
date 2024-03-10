
import os
import glob 
import subprocess
from moviepy.editor import *
from edit import make_video
from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend
files = glob.glob('clips/*')

mp4_files = [file for file in files if file.endswith('.mp4')]

videos = [{'path': f, 'description': '#valorant #vct #masters #champions'} for f in mp4_files]
auth = AuthBackend(cookies='cookies.txt')
upload_videos(videos=videos, auth=auth, headless=True)