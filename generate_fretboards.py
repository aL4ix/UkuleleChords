import fretboard
import pandas as pd


def main():
    chords = pd.read_csv('chords.csv', index_col='Chord', dtype='str')

    for chord, row in chords.iterrows():
        positions, fingers = row
        svg = fretboard.UkuleleChord(positions=positions, fingers=fingers)
        svg.save(f'{chord}.svg')


if __name__ == '__main__':
    main()