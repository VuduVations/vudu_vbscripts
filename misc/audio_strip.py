# prompt: convert /content/frontline_mirror_v1.2 - HD 720p.mov to mp4
!ffmpeg -i /content/2min.mp4 - HD 720p.mov -c:v libx264 -c:a aac -movflags +faststart /content/2min.mp4- HD 720p.mp4

from moviepy.editor import *

# Load video
video = VideoFileClip('/content/2min.mp4')

# Extract audio
audio = video.audio

# Save audio
audio.write_audiofile('output_audio_v1.4.mp3')

# Close the audio object
audio.close()
