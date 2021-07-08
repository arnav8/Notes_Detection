#! /usr/bin/env python

import sys
from aubio import source, notes, midi2note
import numpy

if len(sys.argv) < 2:
    print("Usage: %s <filename> [samplerate]" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]

downsample = 1
samplerate = 44100 // downsample
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

win_s = 512 // downsample # fft size
hop_s = 256 // downsample # hop size

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

notes_o = notes("default", win_s, hop_s, samplerate)

print("%8s" % "time","[ start","vel","last ]")

# total number of frames read
total_frames = 0
note_string_notation = 0
while True:
    samples, read = s()
    new_note = notes_o(samples)
    
    if (new_note[0] != 0):
        note_str = ' '.join(["%.2f" % i for i in new_note])
        if(new_note[2] != -1):
            note_string_notation = midi2note(int(new_note[0]))
            

        print("%.6f" % (total_frames/float(samplerate)),' ------> ', note_string_notation)
    total_frames += read
    if read < hop_s: break

