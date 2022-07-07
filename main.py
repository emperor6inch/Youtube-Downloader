print("Welcome to Emperor6inch YouTube Downloader and Converter v0.1")
print("This program is designed to download and convert YouTube videos to MP3")

import pytube
import youtube_downloader
import file_converter

print("""
What do you want to do?
(1) Download Youtube Videos Manually
(2) Download Youtube Videos from a Playlist
(3) Download and Convert MP3 to MP4 and vice-versa

Downloading copyrighted YouTube videos is illegal and not allowed.
By using this app, you agree to the terms of use of this app.
You are responsible for your own actions. Go at your own risk!.

Copyright © 2022 Emperor6inch. All rights reserved.
""")

choice = input("Enter your choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist:")
        print("Downloading playlist ...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished.")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Downloading video ...")
        filename = youtube_downloader.download_video(link, "low")
        print("Converting video to MP3 ...")
        file_converter.convert_to_mp3(filename)
else:
    print("Invalid input Terminating ...")
