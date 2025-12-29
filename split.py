from config import OUTPUT_FILE, CHUNK_SIZE

def split_text(input_path=OUTPUT_FILE, chunk_size=CHUNK_SIZE):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    
    for i, start in enumerate(range(0, len(lines), chunk_size), 1):
        chunk = lines[start:start + chunk_size]
        part_file = f"{OUTPUT_FILE.rsplit('.', 1)[0]}_part_{i:03d}.txt"
        with open(part_file, "w", encoding="utf-8") as f:
            for line in chunk:
                f.write(line + "\n")