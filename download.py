from pytube import YouTube, Search
import cv2
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
import os

karaoke_name= input("What karoake song is it? \n") + " karaoke"
yt = Search(karaoke_name).results[0]
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="./output", filename="karaoke_song.mp4")

video_path="./output/karaoke_song.mp4"

def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()

PlayVideo(video_path)
os.remove(video_path)
