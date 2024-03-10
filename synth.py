import sounddevice as sd
from numpy import random
from scipy.io import wavfile
from scipy.io.wavfile import write
import keyboard
import threading
import numpy as np

# Play and return sine wave of given frequency
def play_sine(frequency):
    sine_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    # Play the square wave
    sd.play(sine_wave, sample_rate)
    sd.wait()

    # append samples to output
    sine_output_samples = np.append(sine_output_samples, sine_wave)
    return sine_output_samples

# Write array to wav file
def write_wav_file(filename, sample_rate, samples):
    write(filename, sample_rate, samples)

def key_listener():
    sine = []
    while True:
        if keyboard.is_pressed('a'):
            new_sine = play_sine(174.61)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('s'):
            new_sine = play_sine(196.00)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('d'):
            new_sine = play_sine(220.00)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('f'):
            new_sine = play_sine(246.94)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('h'):
            new_sine = play_sine(261.63)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('j'):
            new_sine = play_sine(293.66)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('k'):
            new_sine = play_sine(329.63)
            sine = np.append(sine, new_sine)
        if keyboard.is_pressed('l'):
            new_sine = play_sine(349.23)
            sine = np.append(sine, new_sine)
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