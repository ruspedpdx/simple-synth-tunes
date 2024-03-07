import pyo
import keyboard
import threading

def play_sine(frequency):
    # Create Pyo server
    server = pyo.Server().boot()
    
    # Create sine wave oscillator
    sine = pyo.Sine(freq=frequency, mul=0.5)
    
    # Start the server
    server.start()
    
    # Start the sine wave oscillator
    sine.out()
    
    # Wait for one second
    pyo.time.sleep(1)
    
    # Stop the sine wave oscillator
    sine.stop()
    
    # Stop the server
    server.stop()

def key_listener():
    while True:
        if keyboard.is_pressed('a'):
            play_sine(261.63)

def main():
    # Start the keyboard listener in a separate thread
    threading.Thread(target=key_listener, daemon=True).start()
    
    # Main loop
    print("Press 'a' to play a sine wave of frequency 261.63 Hz.")
    print("Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
