MODEL_SIZE = "large"
COMPUTE_TYPE = "int8"
DEVICE = "cpu"
INPUT_FILE = "audio.mp3"
OUTPUT_FILE = "audio.txt"
LOG_FILE = "transcription.log"
CHUNK_SIZE = 500
TEMP_WAV = "temp_audio.wav"
LANGUAGE = None
SUPPORTED_FORMATS = [
    '.mp3', '.wav', '.m4a', '.aac', '.ogg', '.flac', '.wma', '.opus', '.alac', '.ape', '.aiff', '.amr', '.oga', '.spx', '.tta', '.wv', '.mka',
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v', '.3gp', '.3g2', '.f4v', '.vob', '.ogv', '.ts', '.mts', '.m2ts'
]