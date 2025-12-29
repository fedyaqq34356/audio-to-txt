import sys
from transcribe import transcribe_audio
from split import split_text
from config import INPUT_FILE

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else INPUT_FILE
    transcribe_audio(input_path=input_file)
    split_text()

if __name__ == "__main__":
    main()