from faster_whisper import WhisperModel
from config import MODEL_SIZE, INPUT_FILE, OUTPUT_FILE, COMPUTE_TYPE, DEVICE
from logger import setup_logger

logger = setup_logger()

def transcribe_audio(input_path=INPUT_FILE, output_path=OUTPUT_FILE, model_size=MODEL_SIZE):
    logger.info("Starting transcription")
    logger.info(f"Loading model: {model_size}")
    
    model = WhisperModel(model_size, device=DEVICE, compute_type=COMPUTE_TYPE)
    
    logger.info(f"Processing file: {input_path}")
    segments, info = model.transcribe(
        input_path,
        beam_size=20,
        best_of=10,
        temperature=0.2,
        word_timestamps=False, 
        vad_filter=False,  
        condition_on_previous_text=True,
        language="en"
    )
    
    logger.info(f"Detected language: {info.language}, duration: {info.duration:.2f}s")
    
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment.text.strip() + "\n")
    
    logger.info(f"Transcription saved to: {output_path}")