import simpleaudio as sa
from numpy import random
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.signal import sawtooth
import keyboard
import threading
import numpy as np
import time

# Start menu
def menu():
    # Default menu options, menu is redisplayed after a choice has been made
    print("Press any key in ASDF or HJKL on the home row to play a note.")
    print("Press 't' to randomly change wave type.")
    print("Press 'r' to randomly change tuning.")
    print("Press 'v' to randomly change amplitude.")
    print("Press 'o' to randomly change octave.")
    print("Press 'q' to quit.")


# Get wav type
def get_type():
    # Four main wave types, leaving room for other effects
    wave = ["Sine", "Square", "Sawtooth", "Noise"]
    # For the get wav type function a random choice is made
    type = random.choice(wave)
    print(f"Wave type of {type} chosen")
    return type


# Select wave type
def select_type():
    # Four main wave types, leaving room for other effects
    wave = ["Sine", "Square", "Sawtooth", "Noise"]
    # Ask for user input to select type
    while True:
        try:
            wave_type = int(
                input("Select the wave type: 0:Sine 1:Square 2:Sawtooth 3:Noise")
            )
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if wave_type < 0:
            print("please choose between 0 and 3.")
            continue
        if wave_type > 3:
            print("please choose between 0 and 3.")
            continue
        else:
            break
    type = wave[wave_type]
    print(f"Wave of {type} type chosen")
    return type


# Get amplitude
def get_ampl():
    # small selection of amplitudes, needs to be expanded
    # and handled differently
    amplitude = [4096, 8192, 16384]
    # get ampl will return random choice
    amp = random.choice(amplitude)
    print(f"Amplitude of {amp} chosen")
    return amp


# Select amplitude
def select_ampl():
    # small selection of amplitudes, needs to be expanded
    # and handled differently
    amplitude = [4096, 8192, 16384]
    # ask for user input to choose amplitude
    while True:
        try:
            amp_size = int(input("Select the amplitude: 0:Half, 1:Normal, 2:Double"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if amp_size < 0:
            print("please choose between 0 and 2.")
            continue
        if amp_size > 2:
            print("please choose between 0 and 2.")
            continue
        else:
            break
    amp = amplitude[amp_size]
    print(f"Amplitude of {amp} chosen")
    return amp


# Get octave
def get_oct():
    # small selection of octaves, needs to be expanded
    # and handled differently
    octave = [0.5, 1.0, 2.0]
    # get ampl will return random choice
    oct = random.choice(octave)
    print(f"octave multipiler of {oct} chosen")
    return oct


# Select octave
def select_oct():
    # small selection of octaves, needs to be expanded
    # and handled differently
    octave = [0.5, 1.0, 2.0]
    # ask for user input to choose octave
    while True:
        try:
            oct_mult = int(
                input(
                    "Select the octave: 0:3 Below Middle, 1:4 Middle, 2:5 Above Middle"
                )
            )
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if oct_mult < 0:
            print("please choose between 0 and 2.")
            continue
        if oct_mult > 2:
            print("please choose between 0 and 2.")
            continue
        else:
            break
    oct = octave[oct_mult]
    print(f"octave multipiler of {oct} chosen")
    return oct


# Get key signature
def get_key():
    # selection of minor keys
    keys = ["C", "G", "D", "A", "E", "B", "F", "F#", "Db", "Ab", "Eb", "Bb"]
    # get key will return a random choice
    key = random.choice(keys)
    print(f"Key of {key} chosen")
    return key


# Get key signature
def select_key():
    # selection of minor keys
    keys = ["C", "G", "D", "A", "E", "B", "F", "F#", "Db", "Ab", "Eb", "Bb"]
    while True:
        # ask for user input to select key
        try:
            key = int(
                input(
                    "Select the key: 0:C 1:G 2:D 3:A 4:E 5:B 6:F 7:F# 8:Db 9:Ab 10:Eb 11:Bb"
                )
            )
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if key < 0:
            print("please choose between 0 and 11.")
            continue
        if key > 11:
            print("please choose between 0 and 11.")
            continue
        else:
            break
    sign = keys[key]
    print(f"Key of {sign} chosen")
    return sign


# return frequencies of given key
# hard coded, should be done with frequency generator
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


# Play and return wave of given frequency
# Generic wave player, may be able to replace other play_ functions, still needs more testing
def play_wave(type, frequency, amplitude, duration, octave):
    output_samples = []
    sample_rate = 48000
    frequency = frequency * octave
    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    if type == "Sine":
        wave = amplitude * np.sin(2 * np.pi * frequency * time)
    elif type == "Square":
        wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    elif type == "Sawtooth":
        wave = amplitude * sawtooth(2 * np.pi * frequency * time)
    else:
        wave = np.random.uniform(-amplitude, amplitude, num_samples)
    # Play the wave
        
    # Ensure that highest value is in 16-bit range
    audio = wave * (2**15 - 1) / np.max(np.abs(wave))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()

    # append samples to output
    output_samples = np.append(output_samples, wave)
    return output_samples


# Play and return sine wave of given frequency
def play_sine(frequency):
    sine_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    time = np.arange(num_samples) / sample_rate
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    # Ensure that highest value is in 16-bit range
    audio = sine_wave * (2**15 - 1) / np.max(np.abs(sine_wave))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()

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

    # Ensure that highest value is in 16-bit range
    audio = square_wave * (2**15 - 1) / np.max(np.abs(square_wave))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()

    # append samples to output
    square_output_samples = np.append(square_output_samples, square_wave)
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

    # Ensure that highest value is in 16-bit range
    audio = sawtooth_wave * (2**15 - 1) / np.max(np.abs(sawtooth_wave))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()

    # append samples to output
    sawtooth_output_samples = np.append(sawtooth_output_samples, sawtooth_wave)
    return sawtooth_output_samples


# Play and return noise
def play_noise():
    noise_output_samples = []
    amplitude = 8192
    sample_rate = 48000
    duration = 0.2727  # Duration in seconds

    num_samples = int(sample_rate * duration)
    white_noise = np.random.uniform(-amplitude, amplitude, num_samples)

    # Ensure that highest value is in 16-bit range
    audio = white_noise * (2**15 - 1) / np.max(np.abs(white_noise))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()

    # append samples to output
    noise_output_samples = np.append(noise_output_samples, white_noise)
    return noise_output_samples


# Write array to wav file
def write_wav_file(filename, sample_rate, samples):
    write(filename, sample_rate, samples)


def key_listener():
    # Start up settings
    wav_type = select_type()
    tuning = select_key()
    amplitude = select_ampl()
    octave = select_oct()
    out_wav = []
    freq = get_frequencies(tuning)
    menu()
    while True:
        if keyboard.is_pressed("t"):
            wav_type == ""
            wav_type = get_type()
            menu()
        if keyboard.is_pressed("v"):
            amplitude == ""
            amplitude = get_ampl()
            menu()
        if keyboard.is_pressed("o"):
            octave == ""
            octave = get_oct()
            menu()
        if keyboard.is_pressed("r"):
            freq == []
            tuning = get_key()
            freq = get_frequencies(tuning)
            menu()
        if keyboard.is_pressed("a"):
            new_wav = play_wave(wav_type, freq[0], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("s"):
            new_wav = play_wave(wav_type, freq[1], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("d"):
            new_wav = play_wave(wav_type, freq[2], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("f"):
            new_wav = play_wave(wav_type, freq[3], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("h"):
            new_wav = play_wave(wav_type, freq[4], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("j"):
            new_wav = play_wave(wav_type, freq[5], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("k"):
            new_wav = play_wave(wav_type, freq[6], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        if keyboard.is_pressed("l"):
            new_wav = play_wave(wav_type, freq[7], amplitude, 0.2727, octave)
            out_wav = np.append(out_wav, new_wav)
        out_wav = np.asarray(out_wav, dtype=np.int16)
        write_wav_file("project.wav", 48000, out_wav)


def main():
    # Start the keyboard listener in a separate thread
    threading.Thread(target=key_listener, daemon=True).start()

    # Main loop
    while True:
        if keyboard.is_pressed("q"):
            time.sleep(2)
            break


if __name__ == "__main__":
    main()
