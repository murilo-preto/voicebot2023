import librosa
import soundfile as sf
import ffmpeg

def webm_to_wav_ffmpeg(input_file, output_file):
    try:
        # Cria um objeto ffmpeg para a entrada
        input_stream = ffmpeg.input(input_file)

        # Define as opções de saída para o arquivo WAV
        output_options = {
            'acodec': 'pcm_s16le',
            'ar': 44100,
            'ac': 2
        }

        # Define o caminho de saída
        output_stream = ffmpeg.output(input_stream, output_file, **output_options)

        # Executa o comando ffmpeg
        ffmpeg.run(output_stream)

        print("Conversão concluída com sucesso.")
    except ffmpeg.Error as e:
        print("Falha na conversão:", e.stderr)

def webm_to_wav_librosa(input_file, output_file):
    try:
        # Carrega o arquivo de áudio usando Librosa
        y, sr = librosa.load(input_file, sr=None, mono=True)

        # Salva o arquivo de áudio como WAV usando SoundFile
        sf.write(output_file, y, sr)

        print("Conversão concluída com sucesso.")
    except Exception as e:
        print("Falha na conversão:", e)