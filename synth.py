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
            play_sine(174.61)
        if keyboard.is_pressed('s'):
            play_sine(196.00)
        if keyboard.is_pressed('d'):
            play_sine(220.00)
        if keyboard.is_pressed('f'):
            play_sine(246.94)
        if keyboard.is_pressed('h'):
            play_sine(261.63)
        if keyboard.is_pressed('j'):
            play_sine(293.66)
        if keyboard.is_pressed('k'):
            play_sine(329.63)
        if keyboard.is_pressed('l'):
            play_sine(349.23)


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
