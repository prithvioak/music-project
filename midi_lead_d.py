from mido import Message, MidiFile, MidiTrack
import random
import os
import pygame
import math

# Create a new MIDI file with one track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
# Used in quantizing scale for notes in first loop
d_major = [26, 28, 30, 31, 33, 35, 37, 38, 40, 42, 43, 45, 47, 49, 50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 67, 69, 71, 73, 74, 76, 78, 79, 81, 83, 85, 86, 88, 90, 91, 93, 95, 97, 98, 100, 102, 103, 105, 107, 109, 110, 112, 114, 115, 117, 119]
low = 72
high = 74
duration = 960

for i in range(700):
    note = random.randint(low, high)
    note_to_add = min(d_major, key=lambda x:abs(x-note))
    if i % 20 == 0:
        low -= 1
        high += 1
    track.append(Message('note_on', note=note_to_add, velocity=64, time=0))
    track.append(Message('note_off', note=note_to_add, velocity=64, time=duration))
    if duration > 80:
        duration -= 7

for i in range(700):
    note = random.randint(low, high)
    note_to_add = min(d_major, key=lambda x:abs(x-note))
    if i % 20 == 0:
        low += 1
        high -= 1
    track.append(Message('note_on', note=note_to_add, velocity=64, time=0))
    track.append(Message('note_off', note=note_to_add, velocity=64, time=duration))
    if duration < 960 and i > 575:
        duration += 7

# Save the MIDI file
mid.save(os.path.join('out','random_midi_sequence_d.mid'))

print("MIDI file generated successfully.")

pygame.mixer.init()
pygame.init()

# Load the MIDI file
pygame.mixer.music.load(os.path.join('out','random_midi_sequence_d.mid'))

# Play the MIDI file
# pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)  # Wait for 1 second