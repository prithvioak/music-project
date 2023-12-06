from mido import Message, MidiFile, MidiTrack
import random
import os
import pygame
import math

# Create a new MIDI file with one track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

center = 73
current = 74
duration = 960
prob_to_center = 1
# Generate a random sequence of MIDI notes
for i in range(1000):  # 1000 iterations
    # Random number of notes between 1 and 5 for each iteration
    # Generating a random note (MIDI note numbers are in the range 21-108)
    # note = random.randint(low, high)
    # Generating a random duration for the note (in ticks, 480 ticks per beat is standard)
    # duration = random.randint(120, 480)
    # if i % 20 == 0:
    #     low -= 1
    #     high += 1
    # Adding the note on and off events to the track
    track.append(Message('note_on', note=current, velocity=64, time=0))
    track.append(Message('note_off', note=current, velocity=64, time=duration))
    if current > center:
        current += random.choices([-1, 0, 1], [prob_to_center, 0.1, 0.9-prob_to_center])[0]
    elif current < center:
        current += random.choices([-1, 0, 1], [4*(1-prob_to_center)/5, (1-prob_to_center)/5, prob_to_center])[0]
    else:
        current += random.choice([-1,1])
    if current < 21:
        current = 21
    if current > 108:
        current = 108
    
    if prob_to_center > 0.45:
        prob_to_center -= 0.05
    if duration > 80:
        duration -= 10
    # duration -= math.ceil((960 - 60)/1000)

print(duration)

# Save the MIDI file
mid.save(os.path.join('out','markov_midi_sequence.mid'))

print("MIDI file generated successfully.")

pygame.mixer.init()
pygame.init()

# Load the MIDI file
pygame.mixer.music.load(os.path.join('out','markov_midi_sequence.mid'))

# Play the MIDI file
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)  # Wait for 1 second