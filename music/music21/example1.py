#from music21 import *

import music21
import music21.corpus as corpus
import music21.note as note

def main():
    print("List of properties and functions in module \"music21\":")
    print(f"  {"\n  ".join(dir(music21))}")
    print()

    # Load score of bach/bwv65.2
    s = corpus.parse('bach/bwv65.2.xml')

    # Analyze the score to determine the key
    print(f"The score for \"bach/bwv65.2\" is in the key of {s.analyze('key')}.\n")

    # Open MuseScore with score of bach/bwv65.2
    #s.show()

    print("Hello", end=" ")
    print("World!", end="\n\n")

    print("List of properties and functions in module note:")
    print(f"  {"\n  ".join(dir(note))}")
    print()

    f = note.Note("F5")
    print(f"Note: {f.name}, Octave: {f.octave}, Pitch: {f.pitch}, Frequency: {f.pitch.frequency}")

    b_flat = note.Note("B-2")


'''
################################################################################
####                                                                        ####   
####            ██████   ██████   █████████   █████ ██████   █████          ####
####           ▒▒██████ ██████   ███▒▒▒▒▒███ ▒▒███ ▒▒██████ ▒▒███           ####
####            ▒███▒█████▒███  ▒███    ▒███  ▒███  ▒███▒███ ▒███           ####
####            ▒███▒▒███ ▒███  ▒███████████  ▒███  ▒███▒▒███▒███           ####
####            ▒███ ▒▒▒  ▒███  ▒███▒▒▒▒▒███  ▒███  ▒███ ▒▒██████           ####
####            ▒███      ▒███  ▒███    ▒███  ▒███  ▒███  ▒▒█████           ####
####            █████     █████ █████   █████ █████ █████  ▒▒█████          ####
####           ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒           ####
####                                                                        ####
################################################################################
'''

if __name__ == '__main__':
    main()
    print(f"\n{' Done '.center(80, '~')}\n")
