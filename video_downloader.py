import yt_dlp
import argparse
import os

def download_video(url, download_path):
    abs_path = os.path.abspath(download_path)
    
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)

    ffmpeg_path = r"C:\\DEV\\videos\\ffmpeg-2026-03-15-git-6ba0b59d8b-essentials_build\\bin" 

    ydl_opts = {
        # Requests best video and best audio
        'format': 'bestvideo+bestaudio/best',
        # Ensures the final container is mp4
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(abs_path, '%(title)s.%(ext)s'),
        'restrictfilenames': True,
        'ffmpeg_location': ffmpeg_path,
        
        # This tells ffmpeg to re-encode the audio stream to aac during the merge
        'postprocessor_args': {
            'ffmpeg': [
                '-c:v', 'copy', # Copy the video stream (no re-encoding, fast!)
                '-c:a', 'aac',  # Convert audio stream to AAC
                '-b:a', '192k'  # Set audio bitrate
            ],
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading and converting audio to AAC...")
            ydl.download([url])
            print(f"\nSuccess! Video saved to: {abs_path}")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos with AAC audio.")
    parser.add_argument("url", help="The YouTube URL")
    parser.add_argument("path", nargs='?', default=".", help="Optional: Download folder")
    
    args = parser.parse_args()
    download_video(args.url, args.path)

# Example Usage: 
# python3.12 video_downloader.py https://www.youtube.com/watch?v=c7y2LRcf4kc
# 
