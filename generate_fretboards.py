import os

import fretboard
import pandas as pd

SVGS_FOLDER_PATH = 'svgs'


def main():
    chords = pd.read_csv('chords.csv', index_col='Chord', dtype='str')
    notes = []
    for chord, row in chords.iterrows():
        print(chord)
        positions, fingers = row
        svg = fretboard.UkuleleChord(positions=positions, fingers=fingers)
        os.makedirs(SVGS_FOLDER_PATH, exist_ok=True)
        filename = f'Uke_{chord}.svg'
        svg.save(os.path.join(SVGS_FOLDER_PATH, filename))
        chord_type = get_chord_type(chord)
        notes.append((f'''<img src="{filename}">''', chord, chord_type))
    notes_df = pd.DataFrame(notes)
    notes_df.to_csv('notes.csv', header=False, index=False)


def get_chord_type(chord):
    chord_type = 'Basic'
    if '7' in chord:
        chord_type = 'Seventh'
    return chord_type


if __name__ == '__main__':
    main()
