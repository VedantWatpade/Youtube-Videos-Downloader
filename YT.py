#Follow me for more stuffs.
#link in GitHub profile.

#start 
#install pytube library - pip install pytube

from pytube import YouTube
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        video.download(output_path=save_path)
        print("Download completed!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    #Enter the path where you want to save video.
    save_location = input("Enter the path to save the video: ")

    download_video(video_url, save_location)


    
