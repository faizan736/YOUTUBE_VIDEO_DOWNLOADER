from pytube import YouTube

def download_video(url):
    try:
        youtube=YouTube(url)
        video=youtube.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully"
        )
    except Exception as e:
        print("Error",str(e))

if __name__=="__main__" :
    video_url=input("Enter the Youtube video URL:")
    download_video(video_url)
