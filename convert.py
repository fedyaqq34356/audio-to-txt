import subprocess
from config import INPUT_FILE, TEMP_WAV

def convert_to_wav(input_path=INPUT_FILE, output_path=TEMP_WAV):
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-ar", "16000", "-ac", "1",
        "-y", output_path
    ], check=True)