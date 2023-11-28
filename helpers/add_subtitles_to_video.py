from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

def add_subtitles(video_path, subtitles_path, output_path):
    # Load the video clip
    video = VideoFileClip(video_path)

    # Create a subtitle clip
    subtitles = SubtitlesClip(subtitles_path, lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white'))

    # Set the subtitles to appear at the bottom of the video
    subtitles = subtitles.set_position(('center','bottom')).set_duration(video.duration)

    # Overlay the subtitles on the video
    video_with_subtitles = CompositeVideoClip([video, subtitles])

    # Write the result to a file
    video_with_subtitles.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Usage
add_subtitles('data/with_music.mp4', 'transcript_whisper.srt', 'new_video.mp4')
