from replit import clear
from morse_art import title_header, bye

morse_alphabet = {'A': '· —', 'B': '— · · ·', 'C': '— · — ·', 'D': '— · ·', 'E': '·', 'F': '· · — ·', 'G': '— — ·',
                  'H': '· · · ·', 'I': '· ·', 'J': '· — — —', 'K': '— · —', 'L':	'· — · ·', 'M':	'— —', 'N': '— ·',
                  'O': '— — —', 'P': '· — — ·', 'Q': '— — · —', 'R': '· — ·', 'S': '· · ·', 'T': '—', 'U': '· · —',
                  'V': '· · · —', 'W': '· — —', 'X': '— · · —', 'Y': '— · — —', 'Z': '— — · ·'}


def convert_string():
    """This function will take a string and convert it to morse code, printing the string in the console"""
    converted_string = ""
    uncoded_chars = ""
    string_to_convert = input('Please enter the string you want to convert:\t').upper()
    for char in string_to_convert:
        match = False
        if char == " ":
            converted_string += "/ "
            match = True
        for key, value in morse_alphabet.items():
            if char == key:
                converted_string += value + "   "
                match = True
        if not match:
            uncoded_chars += char + ', '
    if uncoded_chars:
        print(f"\nThe following characters were not converted: {uncoded_chars[:len(uncoded_chars)-2]}")
    if converted_string:
        print(f"\nThis is your coded text:\n{converted_string}")
    new_request = input("\n\nDo you want to try it again?(Y/N)\t").upper()
    if new_request == 'Y':
        clear()
        convert_string()
    else:
        clear()
        print("\nThanks for using the TEXT TO MORSE CONVERTER. Hope to see u soon!")
        print(bye)


print(title_header)
print("Welcome to the TEXT TO MORSE CODE CONVERTER\n")
convert_string()
