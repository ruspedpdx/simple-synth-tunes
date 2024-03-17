import sounddevice as sd
from numpy import random
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.signal import sawtooth
import keyboard
import threading
import numpy as np

# Get wav type
def get_type():
    wave = ["Sine", "Square", "Sawtooth", "Noise"]
    type = random.choice(wave)
    print(f"Wave type of {type} chosen")
    return type

# Get key signature
def get_key():
    keys = ["C", "G", "D", "A", "E", "B", "F", "F#", "Db", "Ab" "Eb", "Bb"]
    key = random.choice(keys)
    print(f"Key of {key} chosen")
    return key

# return frequencies of given key
def get_frequencies(key):
    frequencies = []
    if key == "c" or key == "C":
            frequencies = [261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16, 523.25]
    elif key == "g" or key == "G":
            frequencies = [392.00, 440.00, 466.16, 523.25, 587.33, 622.25, 698.46, 783.99]
    elif key == "d" or key == "D":
            frequencies = [293.66, 392.63, 349.23, 392.00, 440.00, 466.16, 523.25, 587.33]
    elif key == "a" or key == "A":
            frequencies = [440.00, 493.88, 523.25, 587.33, 659.26, 698.46, 783.99, 880.00]
    elif key == "e" or key == "E":
            frequencies = [392.63, 369.99, 392.00, 440.00, 493.88, 523.25, 587.33, 659.26]
    elif key == "b" or key == "B":
            frequencies = [493.88, 554.37, 587.33, 659.26, 739.99, 783.99, 880.00, 987.77]
    elif key == "f" or key == "F":
            frequencies = [349.23, 392.00, 415.30, 466.16, 523.25, 554.37, 622.25, 698.46]
    elif key == "f#" or key == "F#":
            frequencies = [369.99, 415.30, 440.00, 493.88, 554.37, 587.33, 659.26, 739.99]
    elif key == "db" or key == "Db":
            frequencies = [277.18, 311.13, 329.63, 369.99, 415.30, 440.00, 493.88, 554.37]
    elif key == "ab" or key == "Ab":
            frequencies = [415.30, 466.16, 493.88, 554.37, 622.25, 659.26, 739.99, 830.61]
    elif key == "eb" or key == "Eb":
            frequencies = [311.13, 349.23, 369.99, 415.30, 466.16, 493.88, 554.37, 622.25]
    elif key == "bb" or key == "Bb":
            frequencies = [466.16, 523.25, 554.37, 622.25, 698.46, 739.99, 830.61, 932.33]
    else:
            print("Invalid key signature!")
    return frequencies


# Play and return sine wave of given frequency
def play_sine(frequency):
    sine_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    # Play the sine wave
    sd.play(sine_wave, sample_rate)
    sd.wait()

    # append samples to output
    sine_output_samples = np.append(sine_output_samples, sine_wave)
    return sine_output_samples

# Play and return square wave of given frequency
def play_square(frequency):
    square_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))

    # Play the square wave
    sd.play(square_wave, sample_rate)
    sd.wait()

    # append samples to output
    square_output_samples  = np.append(square_output_samples , square_wave)
    return square_output_samples 

# Play and return sawtooth wave of given frequency
def play_sawtooth(frequency):
    sawtooth_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    sawtooth_wave = amplitude * sawtooth(2 * np.pi * frequency * time)

    # Play the sawtooth wave
    sd.play(sawtooth_wave, sample_rate)
    sd.wait()

    # append samples to output
    sawtooth_output_samples  = np.append(sawtooth_output_samples , sawtooth_wave)
    return sawtooth_output_samples 


# Play and return noise
def play_noise():
    noise_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    white_noise = np.random.uniform(-amplitude, amplitude, num_samples)

    # Play the white noise
    sd.play(white_noise, sample_rate)
    sd.wait()

    # append samples to output
    noise_output_samples  = np.append(noise_output_samples , white_noise)
    return noise_output_samples 

# Write array to wav file
def write_wav_file(filename, sample_rate, samples):
    write(filename, sample_rate, samples)

def key_listener():
    wav_type = get_type()
    tuning = get_key()
    sine = []
    freq = get_frequencies(tuning)
    while True:
        if keyboard.is_pressed('a'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[0])
            elif wav_type == "Square": 
                new_wav = play_square(freq[0])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[0])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('s'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[1])
            elif wav_type == "Square": 
                new_wav = play_square(freq[1])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[1])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('d'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[2])
            elif wav_type == "Square": 
                new_wav = play_square(freq[2])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[2])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('f'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[3])
            elif wav_type == "Square": 
                new_wav = play_square(freq[3])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[3])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('h'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[4])
            elif wav_type == "Square": 
                new_wav = play_square(freq[4])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[4])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('j'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[5])
            elif wav_type == "Square": 
                new_wav = play_square(freq[5])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[5])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('k'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[6])
            elif wav_type == "Square": 
                new_wav = play_square(freq[6])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[6])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        if keyboard.is_pressed('l'):
            if wav_type == "Sine":
                new_wav = play_sine(freq[7])
            elif wav_type == "Square": 
                new_wav = play_square(freq[7])
            elif wav_type == "Sawtooth":
                new_wav = play_sawtooth(freq[7])
            else:
                new_wav = play_noise()
            sine = np.append(sine, new_wav)
        sine = np.asarray(sine, dtype=np.int16)
        write_wav_file("project.wav", 48000, sine)

def main():
    # Start the keyboard listener in a separate thread
    threading.Thread(target=key_listener, daemon=True).start()
    
    # Main loop
    print("Press any key on the home row to play a note.")
    print("Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()