# simple-synth-tunes
# Russ Pedersen
# Winter 2024
An interesting synthesizer written in Python

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
