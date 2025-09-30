
from mingus import core
from mingus.core import notes, scales, chords, intervals, keys

def main():
    print("Music rules!\n")
    
    # print(f"core: {dir(core)}\n")

    # core: [
    #   '__all__', 
    #   '__builtins__', 
    #   '__cached__', 
    #   '__doc__', 
    #   '__file__', 
    #   '__loader__', 
    #   '__name__', 
    #   '__package__', 
    #   '__path__', 
    #   '__spec__', 
    #   'chords', 
    #   'intervals', 
    #   'keys', 
    #   'mt_exceptions', 
    #   'notes', 
    #   'scales'
    # ]
 
    # print(f"scales: {dir(scales)}\n")

    # scales: [
    #   'Aeolian', 
    #   'Bachian', 
    #   'Chromatic', 
    #   'Diatonic', 
    #   'Dorian', 
    #   'FormatError', 
    #   'HarmonicMajor', 
    #   'HarmonicMinor', 
    #   'Ionian', 
    #   'Locrian', 
    #   'Lydian', 
    #   'Major', 
    #   'MelodicMinor', 
    #   'MinorNeapolitan', 
    #   'Mixolydian', 
    #   'NaturalMinor', 
    #   'NoteFormatError', 
    #   'Octatonic', 
    #   'Phrygian', 
    #   'RangeError', 
    #   'WholeTone', 
    #   '_Scale', 
    #   '__builtins__', 
    #   '__cached__', 
    #   '__doc__', 
    #   '__file__', 
    #   '__loader__', 
    #   '__name__', 
    #   '__package__', 
    #   '__spec__', 
    #   'absolute_import', 
    #   'augment', 
    #   'determine', 
    #   'diminish', 
    #   'get_notes', 
    #   'intervals', 
    #   'keys', 
    #   'range', 
    #   'reduce_accidentals'
    # ]

    my_scale = ["C", "D", "E", "F", "G", "A", "B", "C"]
    print(f"{scales.determine(my_scale)}")
    my_scale = ["D", "E", "F", "G", "A", "B", "C", "D"]
    print(f"{scales.determine(my_scale)}")


    print()
    print("Diatonic Scales")
    print("---------------")
    
    print()
    
    notes = scales.Diatonic("Ab", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("A" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("Bb", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("B" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("C" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("Db", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("D" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("Eb", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("E" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("F" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("Gb", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("G" , (3, 7)).ascending()
    print(notes)
    print()
    
    notes = scales.Diatonic("G#", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("A" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("A#", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("B" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("C" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("C#", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("D" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("D#", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("E" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("F" , (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("F#", (3, 7)).ascending()
    print(notes)
    print()

    notes = scales.Diatonic("G" , (3, 7)).ascending()
    print(notes)
    print()

    print("Ancient Scales")
    print("--------------")

    print("Aeolian")
    notes = scales.Aeolian("C").ascending()
    print(notes)
    print()

    print("Dorian")
    notes = scales.Dorian("C").ascending()
    print(notes)
    print()

    print("Ionian")
    notes = scales.Ionian("C").ascending()
    print(notes)
    print()

    print("Locrian")
    notes = scales.Locrian("C").ascending()
    print(notes)
    print()

    print("Lydian")
    notes = scales.Lydian("C").ascending()
    print(notes)
    print()

    print("Mixolydian")
    notes = scales.Mixolydian("C").ascending()
    print(notes)
    print()

    print("Phrygian")
    notes = scales.Phrygian("C").ascending()
    print(notes)
    print()

    print("Major Scales")
    print("------------")

    print("Major")
    notes = scales.Major("C").ascending()
    print(notes)
    print()

    print("HarmonicMajor")
    notes = scales.HarmonicMajor("C").ascending()
    print(notes)
    print()

    print("Minor Scales")
    print("------------")

    print("NaturalMinor")
    notes = scales.NaturalMinor("C").ascending()
    print(notes)
    print()

    print("HarmonicMinor")
    notes = scales.HarmonicMinor("C").ascending()
    print(notes)
    print()

    print("MelodicMinor")
    notes = scales.MelodicMinor("C").ascending()
    print(notes)
    print()

    print("Bachian")
    notes = scales.Bachian("C").ascending()
    print(notes)
    print()

    print("MinorNeapolitan")
    notes = scales.MinorNeapolitan("C").ascending()
    print(notes)
    print()

    print("Other Scales")
    print("------------")

    print("Chromatic")
    notes = scales.Chromatic("C").ascending()
    print(notes)
    print()

    print("WholeTone")
    notes = scales.WholeTone("C").ascending()
    print(notes)
    print()
    
    print("Octatonic")
    notes = scales.Octatonic("C").ascending()
    print(notes)
    print()
    
    # result = chords.from_shorthand("Cmaj7")
    # print(f"Cmaj7: {result}")



if __name__ == "__main__":
    main()
