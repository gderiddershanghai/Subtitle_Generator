import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')


def transcribe(fp):

    # Open the audio file for processing
    audio_file = open(fp, "rb")

    # Transcribe the audio using OpenAI's Whisper model in English
    transcript = openai.Audio.transcribe("whisper-1", audio_file, language="en", response_format="srt")
    print(transcript)
    audio_file.close()
    with open('transcript_whisper.srt', 'w') as file:
        file.write(transcript)
        print("Transcript saved as 'transcript_whisper.srt'.")

if __name__ == "__main__":
    fp = "/home/ginger/code/gderiddershanghai/my_subtitle_generator/data/with_music.mp4"
    transcribe(fp)
