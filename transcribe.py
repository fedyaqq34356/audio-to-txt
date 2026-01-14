import os
from faster_whisper import WhisperModel
from config import MODEL_SIZE, OUTPUT_FILE, COMPUTE_TYPE, DEVICE, TEMP_WAV, SUPPORTED_FORMATS, LANGUAGE
from logger import setup_logger
from convert import convert_to_wav

logger = setup_logger()

def transcribe_audio(input_path, output_path=OUTPUT_FILE, model_size=MODEL_SIZE):
    logger.info("Starting transcription")
    logger.info(f"Loading model: {model_size}")
    
    model = WhisperModel(model_size, device=DEVICE, compute_type=COMPUTE_TYPE)
    
    logger.info(f"Processing file: {input_path}")
    
    file_ext = os.path.splitext(input_path)[1].lower()
    
    if file_ext in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'] or file_ext not in ['.wav']:
        logger.info(f"Converting {file_ext} to WAV format")
        audio_path = convert_to_wav(input_path)
    else:
        audio_path = input_path
    
    segments, info = model.transcribe(
        audio_path,
        beam_size=20,
        best_of=10,
        temperature=0.2,
        word_timestamps=False, 
        vad_filter=False,  
        condition_on_previous_text=True,
        language=LANGUAGE
    )
    
    logger.info(f"Detected language: {info.language}, duration: {info.duration:.2f}s")
    
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment.text.strip() + "\n")
    
    if audio_path == TEMP_WAV and os.path.exists(TEMP_WAV):
        os.remove(TEMP_WAV)
        logger.info("Temporary WAV file removed")
    
    logger.info(f"Transcription saved to: {output_path}")