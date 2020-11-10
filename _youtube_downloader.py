"""
Download youtube video
"""

import pytube

# url = 'https://youtu.be/fp0O7kp0uW8'

# Load url in function Youtube
# youtube = pytube.YouTube(url)

# Set Streams Resolution
# video = youtube.streams.first()
# or
# video = youtube.streams.get_highest_resolution()

# Download Video
# video.download() # In Same Folder
# or
# video.download('D://Downloads')  # In Other Folder

# Get Information of Video
# video.title  # Title
# video.video_id  # Id
# video.age_restricted  # Age

# Streams Format
# video.streams.all()
# stream = video.streams.all()
# for i in stream:
#     print(i)

url = input('Give URL: ')
pytube.YouTube(url).streams.get_highest_resolution().download('D://Downloads')
