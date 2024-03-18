# Russ Pedersen
# simple-synth-tunes
# Winter 2024
An interesting synthesizer written in Python

A simple keyboard that will generate various sound waves depending on a few settings
that you enter when you start the program. These settings are able to be changed while the 
program is running.

In a unix based system, from a terminal you can type:

`pip install -r requirements.txt`

then

`python3 synth.py` 

to run the program.

While testing on the student Linux servers, I realized that part of the code wasn't usable due
to root permissions and keyboard listeners. I modified all of the keyboard listening code to accept
one character entered at a time to demonstrate the code functionality, but this is less than ideal
for a synth experience.

I used the unittest module in Python to test each of the get and select functions with 
good and bad input.

The project1.wav, project2.wav and project3.wav files are output from various tests.

# Process notes

I first tried to write a simple function to play a sine wave when a key was pressed using 
the termion and rodio crates in Rust. I was never able to get the sine wave to play and save, 
so I switched to Python instead.

I started with a simple keyboard listener to generate a sine wave when a key was pressed.
Then expanded this to multiple keys, the frequencies of the keys start with the root of a chord
playable by pressing 'a' on the computer keyboard, the other keys in the home row are derived from
this root note.

I wanted to limit the number of keys played to make the code easier to debug. A future addition
might be the keys needed to be able to play the full 12 notes of each octave.

I added support for square wave, sawtooth wave and white noise and a function to select the
wave type when the keyboard listener is started.

Then added a way to change the frequencies of the chords as the keyboard is being played.
This has mixed results for being able to save the output to a .wav file, but works sometimes.
More work will need to be done for this section.

I changed the play function to take the wave type as a parameter, and was able to use one
function to play all of the types of waves. 

Then I added the ability to change the amplitude of the waves, this seems to work best (for the 
purposes of saving the .wav file) with amplitude sizes of 4096 or 8192. More testing is required
here as well.

One of the things I put in the proposal was the ability to change octaves, and this could have been 
done in multiple ways and could be expanded to include a full 88 key range (or more) but my 
first attempt was to simply use the 3rd through 5th octaves of a standard keyboard by multiplying
and dividing the basic frequencies passed into the play wave function.

Some of the challenges are to implement a realistic duration by timing the key press and release.
Even though it is fun to generatate musing by playing the keyboard, it feels clunky and jarring like
playing with weights tied to your fingers. Playing back the saved files from each session feels
smooth and clean, as expected from the wave generators.

The project outfiles are sometimes invalid or corrupt, more testing is needed to find a fix for this.

I saved several output files and want to add further effects using these files if I have time.


** Notes for the original keyboard command version. I had to change this from a listener to
a terrible get char command due to root permissions on Linux. If you want to try this version
(the only difference is that you won't have to hit <enter> after each keystroke.)

You will need to run this project with Python 3.9. Here are some instructions 
for setting up a virtual environment with a different python version.

https://cat.pdx.edu/platforms/linux/how-to/pip-python-virtual-env/

I was able to run this from VS Code without any issues by choosing the interpreter
from Command Palette

View > Command Palette > Python: Select Interpreter > Python 3.9.13

In VS Code, you can use Ctrl + F5 to run the project without debugging. This will open up 
a series of questions related to wave type, amplitude, etc. After you answer those questions
you can use the home row of your computer keyboard to play notes. This will automatically be saved
into a project.wav file that you can playback using any .wav reader.


MIT License

Copyright (c) 2024 ruspedpdx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.