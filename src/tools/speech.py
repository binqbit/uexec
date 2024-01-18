import pyaudio
import numpy as np
import wave

from tools.console import clear_line, get_columns



def is_fast_mode():
    return True

FORMAT = pyaudio.paInt16
CHANNELS = 1

# RATE = 44100
RATE = 22050
CHUNK_SIZE = 256

SILENCE_THRESHOLD = 1000
SILENCE_DURATION = 1 * (RATE // CHUNK_SIZE)



def listen_and_save(filename, wait_conversation = False, event = None):
    if is_fast_mode():
        speed = 0.75
    else:
        speed = 1.0

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK_SIZE)

    audio_frames = []
    silence_counter = 0
    start_conversation = False

    try:
        while True:
            audio_data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)
            mean = np.mean(np.abs(audio_data))
            
            if mean < SILENCE_THRESHOLD:
                if start_conversation or not wait_conversation:
                    silence_counter += 1
                    columns = get_columns()
                    counter = columns - silence_counter * columns / (SILENCE_DURATION * speed)
                    clear_line()
                    print("#" * int(counter), end="\r")
            else:
                silence_counter = 0
                if not start_conversation:
                    start_conversation = True

            if silence_counter >= SILENCE_DURATION * speed:
                if not start_conversation:
                    return False
                break

            audio_frames.append(audio_data)

            if event and event.is_set():
                if not start_conversation:
                    return False

    except KeyboardInterrupt:
        return False

    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_frames))

    return True
