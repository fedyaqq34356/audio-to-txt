import sys
import os
from convert import convert_to_wav
from transcribe import transcribe_audio
from split import split_text
from config import INPUT_FILE, TEMP_WAV

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else INPUT_FILE
    convert_to_wav(input_path=input_file)
    transcribe_audio()
    split_text()
    os.remove(TEMP_WAV)

if __name__ == "__main__":
    main()