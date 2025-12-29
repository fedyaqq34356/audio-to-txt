from pocketsphinx import AudioFile
from config import TEMP_WAV, OUTPUT_FILE
from logger import setup_logger

logger = setup_logger()

def transcribe_audio(wav_path=TEMP_WAV, output_path=OUTPUT_FILE):
    logger.info("Starting transcription")
    
    text = []
    for phrase in AudioFile(audio_file=wav_path):
        text.append(phrase.hyp().hypstr)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(text))
    
    logger.info(f"Transcription saved to: {output_path}")