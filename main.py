import sys
import os
from transcribe import transcribe_audio
from split import split_text
from config import INPUT_FILE, SUPPORTED_FORMATS

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else INPUT_FILE
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found")
        return
    
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext not in SUPPORTED_FORMATS:
        print(f"Error: Unsupported format '{file_ext}'")
        print(f"Supported formats: {', '.join(SUPPORTED_FORMATS)}")
        return
    
    transcribe_audio(input_path=input_file)
    split_text()

if __name__ == "__main__":
    main()