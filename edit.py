import ffmpeg
import moviepy.editor as mp
import os
def make_video(input_file):
    input_stream = ffmpeg.input(input_file)
    # Box blur with radius 20
    background_stream = input_stream.filter("boxblur", 20)
    ffmpeg.output(background_stream, f"{input_file.split('.')[0]}_bg.mp4").run()
    small = mp.VideoFileClip(input_file)
    if small.duration >= 20:
        bg = mp.VideoFileClip(f'{input_file.split('.')[0]}_bg.mp4')
        small =  small.set_position((-400, 420)) # Set position on screen 
        bg = bg.resize((1080,1920))
        bg = bg.crop(x_center=540, y_center=960, width=1080, height=1920) # Potrait format
        final_video = mp.CompositeVideoClip([bg, small]) # Overlay the small screen over the blurred background
        final_video.write_videofile(f"{input_file.split('.')[0]}_out.mp4")
        final_video.close()
    else: # If video is too short, simply remove the video 
        os.remove(input_file) 

