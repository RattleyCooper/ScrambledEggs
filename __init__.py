import string as st
from common import Dial


class Scrambler(object):
    # characters = [c for c in st.ascii_letters + "1234567890-=`~!@#$%^&*()_+\\][|{}';/.,\":?>< "]
    characters = [c for c in st.printable]
    rev_ord = {ord(c): c for c in characters}
    ord = {c: ord(c) for c in characters}

    def __init__(self):
        Scrambler.rev_ord[31] = '\n'
        Scrambler.ord['\n'] = 31

        Scrambler.rev_ord[30] = '\t'
        Scrambler.ord['\t'] = 30

    def scramble(self, string):
        if not string:
            raise ValueError("String cannot be empty.")

        first_letter_ord = Scrambler.ord[string[0]]
        output = ""

        for i, c in enumerate(string):
            d1 = Dial(Scrambler.ord[c])
            c_ord = d1.add(sum([Scrambler.ord[x] for x in string[:i]]))
            if i == 0:
                out = c
            else:
                d1.set_pointer(first_letter_ord)
                _ = d1.add(c_ord)
                out = Scrambler.rev_ord[_]

            output += out
            first_letter_ord = Scrambler.ord[c]

        d1.set_pointer(Scrambler.ord[string[0]])
        first_letter_number = d1.add(sum([Scrambler.ord[x] for x in output[1:]]))
        output = Scrambler.rev_ord[first_letter_number] + output[1:]
        return output

    def unscramble(self, string):
        if not string:
            raise ValueError("String cannot be empty.")

        first_letter_ord = Scrambler.ord[string[0]]
        if not first_letter_ord:
            raise ValueError("Your message is invalid.")

        output = ""

        # Set string's first letter to the correct un-encoded letter.
        d1 = Dial(first_letter_ord)
        first_letter_number = d1.sub(sum([Scrambler.ord[x] for x in string[1:]]))
        first_letter = Scrambler.rev_ord[first_letter_number]
        string = first_letter + string[1:]

        for i, c in enumerate(string):
            d1.set_pointer(Scrambler.ord[c])
            c_ord = d1.sub(sum([Scrambler.ord[x] for x in output[:i]]))
            if i == 0:
                out = c
            else:
                last_c_ord = Scrambler.ord[output[-1]]
                d1.set_pointer(c_ord)
                out_ord = d1.sub(last_c_ord)
                out = Scrambler.rev_ord[out_ord]

            output += out
            first_letter_ord = Scrambler.ord[out]

        return output


print(''.join(Scrambler.characters))
d = """Paul awoke to feel himself in the warmth of his bed - thinking... thinking. This world of Castle Caladan, without play or companions his own age, perhaps did not deserve sadness in farewell. Dr. Yueh, his teacher, had hinted that the faufreluches class system was not rigidly guarded on Arrakis. The planet sheltered people who lived at the desert edge without caid or bashar to command them: will-o'-the-sand people called Fremen, marked down on no census of the Imperial Regate.s"""
d2 = """ASCII stands for American Standard Code for Information Interchange. Computers can only understand numbers, so an ASCII code is the numerical representation of a character such as 'a' or '@' or an action of some sort. ASCII was developed a long time ago and now the non-printing characters are rarely used for their original purpose. Below is the ASCII character table and this includes descriptions of the first 32 non-printing characters. ASCII was actually designed for use with teletypes and so the descriptions are somewhat obscure. If someone says they want your CV however in ASCII format, all this means is they want 'plain' text with no formatting such as tabs, bold or underscoring - the raw format that any computer can understand. This is usually so they can easily import the file into their own applications without issues. Notepad.exe creates ASCII text, or in MS Word you can save a file as 'text only'"""
d3 = """They've been pumping basements around the clock in neighborhoods like Pico Avenue where Sean Driscoll's basement flooded and three cars were damaged. He managed to get his family to a hotel but now has no heat, electricity or water. "I was a kid during the blizzard of 78 and this was definitely close to that," he said. "If I didn't get out of the basement when I did, when water passed the electrical panel, I could have been electrocuted," Esposito said. "I'm lucky I got out before that." He says the bucket rescue was a hair-raising experience, but he was grateful for the lift. "The only bad thing was the metal blade was so slippery with and snow it was hard to keep yourself steady," he said. Lt. Governor Karyn Polito met with Winthrop town officials to tour the hard hit area and assess the damage. She is hoping for some federal disaster relief. "We will evaluate all the estimates and then determine what next steps can be taken," Polito said."""
d4 = "Scrambled eggs are yummy."

s = Scrambler()

print()
o = "Going down to south park\ngonna have myself a time."
print('string:', o)
o = s.scramble(o)
print('\nencoded:', o)
m = s.unscramble(o)
print('\ndecoded:', m)

o = """import string as st
from common import circular_add, circular_subtract


class Scrambler(object):
    # characters = [c for c in st.ascii_letters + "1234567890-=`~!@#$%^&*()_+\\][|{}';/.,\":?>< "]
    characters = [c for c in st.printable]
    rev_ord = {ord(c): c for c in characters}
    ord = {c: ord(c) for c in characters}

    def __init__(self):
        Scrambler.rev_ord[31] = '\n'
        Scrambler.ord['\n'] = 31

        Scrambler.rev_ord[30] = '\t'
        Scrambler.ord['\t'] = 30

    def scramble(self, string):
        first_letter_ord = Scrambler.ord[string[0]]
        output = ""

        for i, c in enumerate(string):
            c_ord = circular_add(Scrambler.ord[c], sum([Scrambler.ord[x] for x in string[:i]]))
            if i == 0:
                out = c
            else:
                _ = circular_add(first_letter_ord, c_ord)
                out = Scrambler.rev_ord[_]

            output += out
            first_letter_ord = Scrambler.ord[c]

        # Set first character to an encoded character based on the sum of all characters after the first character.
        first_letter_number = circular_add(Scrambler.ord[string[0]], sum([Scrambler.ord[x] for x in output[1:]]))
        output = Scrambler.rev_ord[first_letter_number] + output[1:]
        return output

    def unscramble(self, string):
        first_letter_ord = Scrambler.ord[string[0]]
        if not first_letter_ord:
            raise ValueError("Your message is invalid.")

        output = ""

        # Set string's first letter to the correct un-encoded letter.
        first_letter_number = circular_subtract(first_letter_ord, sum([Scrambler.ord[x] for x in string[1:]]))
        first_letter = Scrambler.rev_ord[first_letter_number]
        string = first_letter + string[1:]

        for i, c in enumerate(string):
            c_ord = circular_subtract(Scrambler.ord[c], sum([Scrambler.ord[x] for x in output[:i]]))
            # c_ord = Scrambler.ord[c]
            if i == 0:
                out = c
            else:
                last_c_ord = Scrambler.ord[output[-1]]
                out_ord = circular_subtract(c_ord, last_c_ord)
                out = Scrambler.rev_ord[out_ord]

            output += out
            first_letter_ord = Scrambler.ord[out]

        return output
"""

print('\nstring:', o)
o = s.scramble(o)
print('\nencoded:', o)
o = s.unscramble(o)
print('\ndecoded:', o)
