
from mingus import core
from mingus.core import notes, scales, chords, intervals, keys

def main():
    print("Music rules!")
    result = chords.from_shorthand("Cmaj7")
    print(f"Cmaj7: {result}")
    
    print (f"Aeolian\n{scales.Aeolian("C")}")
    print (f"Bachian\n{scales.Bachian("C")}")

    print(f"core: {dir(core)}\n")

#    core: [
#        '__all__', 
#        '__builtins__', 
#        '__cached__', 
#        '__doc__', 
#        '__file__', 
#        '__loader__', 
#        '__name__', 
#        '__package__', 
#        '__path__', 
#        '__spec__', 
#        'chords', 
#        'intervals', 
#        'keys', 
#        'mt_exceptions', 
#        'notes', 
#        'scales'
#    ]

    print(f"scales: {dir(scales)}\n")

#    scales: [
#        'Aeolian', 
#        'Bachian', 
#        'Chromatic', 
#        'Diatonic', 
#        'Dorian', 
#        'FormatError', 
#        'HarmonicMajor', 
#        'HarmonicMinor', 
#        'Ionian', 
#        'Locrian', 
#        'Lydian', 
#        'Major', 
#        'MelodicMinor', 
#        'MinorNeapolitan', 
#        'Mixolydian', 
#        'NaturalMinor', 
#        'NoteFormatError', 
#        'Octatonic', 
#        'Phrygian', 
#        'RangeError', 
#        'WholeTone', 
#        '_Scale', 
#        '__builtins__', 
#        '__cached__', 
#        '__doc__', 
#        '__file__', 
#        '__loader__', 
#        '__name__', 
#        '__package__', 
#        '__spec__', 
#        'absolute_import', 
#        'augment', 
#        'determine', 
#        'diminish', 
#        'get_notes', 
#        'intervals', 
#        'keys', 
#        'range', 
#        'reduce_accidentals'
#    ]

    print("Diatonic Scales")
    #print(f"Diatonic\n{scales.Diatonic("C")}\n")

    print("Ancient Scales")
    print(f"Aeolian\n{scales.Aeolian("C")}\n")
    print(f"Dorian\n{scales.Dorian("C")}\n")
    print(f"Ionian\n{scales.Ionian("C")}\n")
    print(f"Locrian\n{scales.Locrian("C")}\n")
    print(f"Lydian\n{scales.Lydian("C")}\n")
    print(f"Mixolydian\n{scales.Mixolydian("C")}\n")
    print(f"Phrygian\n{scales.Phrygian("C")}\n")

    print("Major Scales")
    print(f"Major\n{scales.Major("C")}\n")
    print(f"HarmonicMajor\n{scales.HarmonicMajor("C")}\n")

    print("Minor Scales")
    print(f"NaturalMinor\n{scales.NaturalMinor("C")}\n")
    print(f"HarmonicMinor\n{scales.HarmonicMinor("C")}\n")
    print(f"MelodicMinor\n{scales.MelodicMinor("C")}\n")
    print(f"Bachian\n{scales.Bachian("C")}\n")
    print(f"MinorNeapolitan\n{scales.MinorNeapolitan("C")}\n")

    print("Other Scales")
    print(f"Chromatic\n{scales.Chromatic("C")}\n")
    print(f"WholeTone\n{scales.WholeTone("C")}\n")
    print(f"Octatonic\n{scales.Octatonic("C")}\n")

    

if __name__ == "__main__":
    main()
