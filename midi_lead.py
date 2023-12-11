from mido import Message, MidiFile, MidiTrack
import random
import os
import pygame
import math

# Create a new MIDI file with one track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# lowest possible value for random note
low = 72
# hightest posible value for random note
high = 74
# duration of note (in ticks, 480 ticks per beat is standard)
duration = 960

# First loop; increasing speed
for i in range(700):
    note = random.randint(low, high)
    if i % 20 == 0:
        # increasing width of the envelope
        low -= 1
        high += 1
    # Adding the note on and off events to the track
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration))
    # increasing speed
    if duration > 80:
        duration -= 7

# Second loop; decreasing speed
for i in range(700):
    note = random.randint(low, high)
    if i % 20 == 0:
        # decreasing width of the envelope
        low += 1
        high -= 1
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration))
    # decreasing speed
    if duration < 960 and i > 575:
        duration += 7

# Save the MIDI file
mid.save(os.path.join('out','random_midi_sequence.mid'))

print("MIDI file generated successfully.")

pygame.mixer.init()
pygame.init()

# Load the MIDI file
pygame.mixer.music.load(os.path.join('out','random_midi_sequence.mid'))

# Play the MIDI file
# pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)  # Wait for 1 second