import subprocess

def webm2wav(input_file, output_file):
    # Command to convert WebM to WAV using ffmpeg
    command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", output_file]

    try:
        # Execute the ffmpeg command
        subprocess.run(command, check=True)
        print("Conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Conversion failed:", e)
