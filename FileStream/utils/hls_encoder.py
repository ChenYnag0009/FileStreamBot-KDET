import os
import subprocess

def encode_hls(input_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cmd = f"""ffmpeg -i "{input_path}" \
    -map 0 -c:v libx264 -crf 23 -preset veryfast \
    -g 48 -sc_threshold 0 \
    -map 0 -c:a aac -b:a 128k \
    -vf "scale=w=1280:h=720:force_original_aspect_ratio=decrease" -b:v 2800k -maxrate 2996k -bufsize 4200k \
    -f hls -hls_time 6 -hls_playlist_type vod \
    -hls_segment_filename "{output_folder}/stream_%03d.ts" \
    "{output_folder}/master.m3u8"
    """
    subprocess.run(cmd, shell=True)
