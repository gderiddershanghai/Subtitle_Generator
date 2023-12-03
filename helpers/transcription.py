import requests
import assemblyai as aai
import os

from dotenv import load_dotenv, find_dotenv
import requests

_ = load_dotenv(find_dotenv())
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

def transcribe_video(fp):
    transcriber = aai.Transcriber()
    print('----------')
    print(transcriber)
    transcript = transcriber.transcribe(fp)
    subtitles_srt = transcript.export_subtitles_srt()
    print(subtitles_srt)
    with open('transcript.srt', 'w') as file:
        file.write(subtitles_srt)
        print("Transcript saved as 'transcript.srt'.")

if __name__ == "__main__":
    fp = "/home/ginger/code/gderiddershanghai/my_subtitle_generator/data/with_music.mp4"
    transcribe_video(fp)
