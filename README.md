# Audio Transcription Tool

Audio Transcription Tool is a simple utility for converting speech to text using faster-whisper.

## Features

* Transcribe audio files to text
* Split output into chunks
* Support for multiple audio formats
* Detailed logging

## Requirements

```
Python 3.8+
faster-whisper >= 0.9.0
ffmpeg
```

## Installation

```bash
git clone https://github.com/fedyaqq34356/audio-to-txt.git
cd audio-to-txt
pip install faster-whisper
```

FFmpeg must be installed separately for audio conversion.

## Usage

```bash
python main.py [audio_file]
```

If no file is specified, the tool uses `audio.mp3` from config.

### Steps:
1. Place your audio file in the directory or specify path
2. Run `python main.py your_audio.mp3`
3. Get transcription in `audio.txt`
4. Find split chunks as `audio_part_001.txt`, `audio_part_002.txt`, etc.

## Configuration

Edit `config.py` to customize:

```python
MODEL_SIZE = "large"      # tiny, base, small, medium, large
COMPUTE_TYPE = "float32"  # float32, float16, int8
DEVICE = "cpu"            # cpu or cuda
CHUNK_SIZE = 500          # lines per chunk
```

## Project Structure

```
audio-to-txt/
├── main.py              # Entry point
├── transcribe.py        # Core transcription
├── split.py             # Text splitting
├── convert.py           # Format conversion
├── config.py            # Configuration
├── logger.py            # Logging setup
├── example/
│   ├── example_audio.mp3
│   ├── original_text.txt
│   └── example_output_audio.txt
└── README.md
```

## Example

The `example/` directory contains sample files showing transcription quality. Compare `original_text.txt` with `example_output_audio.txt` to see accuracy.

## Output

* `audio.txt` - Full transcription
* `audio_part_XXX.txt` - Split chunks
* `transcription.log` - Process log

## Notes

Transcription quality depends on audio clarity, model size, and proper language settings. Larger models provide better accuracy but require more processing time.

## License

GNU General Public License v3.0

This project is free software. You can redistribute it and/or modify it under the terms of the GPL v3 or any later version.

This software is provided without any warranty.

## Contributing

Pull requests are welcome. Keep changes minimal and focused.

## Author

Built with Python and faster-whisper.