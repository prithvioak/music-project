from mido import Message, MidiFile, MidiTrack
import random
import os
import pygame
import math

# Create a new MIDI file with one track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

low = 72
high = 74
duration = 960
# Generate a random sequence of MIDI notes
for i in range(1000):  # 1000 iterations
    # Random number of notes between 1 and 5 for each iteration
    # Generating a random note (MIDI note numbers are in the range 21-108)
    note = random.randint(low, high)
    # Generating a random duration for the note (in ticks, 480 ticks per beat is standard)
    # duration = random.randint(120, 480)
    if i % 20 == 0:
        low -= 1
        high += 1
    # Adding the note on and off events to the track
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration))
    if duration > 80:
        duration -= 10
    # duration -= math.ceil((960 - 60)/1000)

print(duration)

# Save the MIDI file
mid.save(os.path.join('out','random_midi_sequence.mid'))

print("MIDI file generated successfully.")

pygame.mixer.init()
pygame.init()

# Load the MIDI file
pygame.mixer.music.load(os.path.join('out','random_midi_sequence.mid'))

# Play the MIDI file
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)  # Wait for 1 second