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




# def transcribe_video(api_key, audio_url):
#     endpoint = "https://api.assemblyai.com/v2/transcript"
#     json = {
#         "audio_url": audio_url
#     }
#     headers = {
#         "authorization": api_key,
#         "content-type": "application/json"
#     }
#     response = requests.post(endpoint, json=json, headers=headers)
#     return response.json()['id']

# # Example usage
# api_key = 'your_assemblyai_api_key'
# audio_url = 'url_of_your_uploaded_video'
# transcript_id = transcribe_video(api_key, audio_url)


# def get_transcription(api_key, transcript_id):
#     endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
#     headers = {
#         "authorization": api_key
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# # Get transcription result
# transcription = get_transcription(api_key, transcript_id)
# print(transcription['text'])
# # Here you can implement a method to allow the user to edit or confirm the transcription
if __name__ == "__main__":
    fp = "/home/ginger/code/gderiddershanghai/my_subtitle_generator/data/with_music.mp4"
    transcribe_video(fp)
