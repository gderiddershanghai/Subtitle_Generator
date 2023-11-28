# from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
# from moviepy.video.tools.subtitles import SubtitlesClip
import subprocess

def add_subtitles(video_path, subtitles_path, output_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f"subtitles={subtitles_path}:force_style='Fontsize=32,Alignment=2,MarginV=10'",
        '-c:v', 'libx264',
        '-c:a', 'copy',
        '-crf', '22',
        '-preset', 'veryfast',
        output_path
    ]
    subprocess.run(command)

# def add_subtitles(video_path, subtitles_path, output_path):

#     video = VideoFileClip(video_path)
#     generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
#     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>',generator)
#     subtitles = SubtitlesClip(subtitles_path, generator)

#     subtitles = subtitles.set_position(('center','bottom')).set_duration(video.duration)

#     video_with_subtitles = CompositeVideoClip([video, subtitles])

#     video_with_subtitles.write_videofile(output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    add_subtitles('data/original.mp4', 'transcript_whisper.srt', 'new_video.mp4')
