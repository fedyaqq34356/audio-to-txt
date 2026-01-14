import subprocess
import os
from config import TEMP_WAV

def convert_to_wav(input_path, output_path=TEMP_WAV):
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-ar", "16000", "-ac", "1",
        "-vn",
        "-y", output_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path