# Tutorial 1 - Working With Notes

# https://bspaans.github.io/python-mingus/index.html

from mingus.containers import Note
from mingus.core import notes

def main():
    #------------------------------------------------------------
    # Do some notes
    #------------------------------------------------------------

    print(f"{notes.is_valid_note("C")}")
    # True

    print(f"{notes.is_valid_note("D#")}")
    # True

    print(f"{notes.is_valid_note("Eb")}")
    # True

    print(f"{notes.is_valid_note("Fbb")}")
    # True

    print(f"{notes.is_valid_note("G##")}")
    # True

    #------------------------------------------------------------
    # Some examples of invalid notes
    #------------------------------------------------------------

    print(f"{notes.is_valid_note("c")}")
    # False

    print(f"{notes.is_valid_note("D #")}")
    # False

    print(f"{notes.is_valid_note("E-b")}")
    # False

    #------------------------------------------------------------
    # Some, perhaps surprisingly valid notes
    #------------------------------------------------------------

    print(f"{notes.is_valid_note("C######bb")}")
    # True

    print(f"{notes.is_valid_note("C#b#bb##b##bb")}")
    # True

    #------------------------------------------------------------
    # As you can see, mingus can handle any number of 
    # accidentals, whether it is the sensible thing to do or 
    # not. If you want to clean up messy accidentals, you can 
    # use "remove_redundant_accidentals(note)". Because it’s 
    # all fun and games until someone gets hurt.
    #------------------------------------------------------------

    print(f"{notes.remove_redundant_accidentals("C##b")}")
    # 'C#'

    print(f"{notes.remove_redundant_accidentals("C#b#bb##b##bb")}")
    # 'C'

    #------------------------------------------------------------
    # Notes as Integers
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Sometimes it is easier to work with notes as integers 
    # in range(0,12). This is possible with the functions 
    # notes.note_to_int(str) and notes.int_to_note(int).
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Note to integer
    #------------------------------------------------------------

    print(f"{notes.note_to_int("C")}")
    # 0

    print(f"{notes.note_to_int("B")}")
    # 11

    print(f"{notes.note_to_int("Cb")}")
    # 11

    print(f"{notes.note_to_int("C#")}")
    # 1

    print(f"{notes.note_to_int("Db")}")
    # 1

    #------------------------------------------------------------
    # As you can see in the examples some notes return the 
    # same values. These notes are called enharmonic, because 
    # they sound the same.
    #  
    # There is "notes.is_enharmonic(note1, note2)" to test if 
    # two notes are enharmonic.
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Integer to Note
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Because enharmonic notes exist, it is impossible to create 
    # a sound int-to-note converter based on an integer alone. 
    # For example, in the last piece of code we saw that B and 
    # Cb are both 11. They sound the same, but they aren’t
    # theoretically the same. This can be important when
    # building and recognizing intervals and thus scales and
    # chords, because intervals depend on the note name.
    # For instance: the interval between A and B is called a
    # major second, while the interval between A and Cb is a
    # diminished third. diatonic.int_to_note does a better job
    # at the conversion, bearing the key in mind as well. The
    # converter in [tutorialNoteModule Note] can also handles
    # octaves on top of that. Anyway, if you don’t care about
    # theoretically sound conversions or don’t need to
    # differentiate, this function is fine (it sounds the same,
    # after all):
    #------------------------------------------------------------

    print(f"{notes.int_to_note(0)}")
    # "C"
    
    print(f"{notes.int_to_note(1)}")
    # "C#"

    print(f"{notes.int_to_note(2)}")
    # "D"

    print(f"{notes.int_to_note(3)}")
    # "D#"

    print(f"{notes.int_to_note(4)}")
    # "E"

    #------------------------------------------------------------
    # Helper Functions
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Augment and Diminish
    #------------------------------------------------------------

    #------------------------------------------------------------
    # Augmenting and diminishing a note is a little bit harder 
    # than just slapping a ‘#’ or ‘b’ on at the end of the string. 
    # For instance: when you want to augment a ‘Cb’ note, a 
    # ‘C’ would be nicer than a ‘Cb#’ (although, again, they are 
    # the same, but it’s like using double negative). augment and 
    # diminish do a nice job at this:
    #------------------------------------------------------------

    print("Augmenting a note")

    print(f"{notes.augment('C')}")
    # "C#"

    print(f"{notes.augment('Cb')}")
    # "C"

    print(f"{notes.augment('C#')}")
    # "C##"

    print(f"{notes.augment("B")}")
    # "B#"

    print("Diminishing a note")

    print(f"{notes.diminish('C')}")
    # "Cb"

    print(f"{notes.diminish('C#')}")
    # "C"

    print(f"{notes.diminish('Cb')}")
    # "Cbb"

    print(f"{notes.diminish('B#')}")
    # "B"

    print("Minor and Major conversions")

    print("Minor:")

    #print(f"{notes.to_minor("C")}")
    # "A"

    #print(f"{notes.to_minor("F")}")
    # "D"

    #print(f"{notes.to_minor("D")}")
    # "B"

    #print(f"{notes.to_minor("B")}")
    # "G#"

    print("Major:")

    #print(f"{notes.to_major("A")}")
    # "C"

    #print(f"{notes.to_major("D")}")
    # "F"

    #print(f"{notes.to_major("B")}")
    # "D"

    #print(f"{notes.to_major("G#")}")
    # "B"

if __name__ == '__main__':
    main()
    