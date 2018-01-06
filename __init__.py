import string as st


def circular_add(start, amount, rng=(32, 126)):
    output = start + amount
    if output > rng[1]:
        output -= rng[1]
        output += rng[0] - 1
        if output > rng[1]:
            output = circular_add(rng[1], output - rng[1], rng=rng)

    return output


def circular_subtract(start, amount, rng=(32, 126)):
    output = start - amount

    if output < rng[0]:
        output += rng[1] + 1
        output -= rng[0]
        if output < rng[0]:
            output = circular_subtract(rng[0], rng[0] - output, rng=rng)

    return output


class Scrambler(object):
    characters = [c for c in st.ascii_letters + "1234567890-=`~!@#$%^&*()_+\\][|{}';/.,\":?>< "]
    rev_ord = {ord(c): c for c in characters}
    ord = {c: ord(c) for c in characters}

    def scramble(self, string):
        salt = Scrambler.ord[string[0]]
        output = ""

        for i, c in enumerate(string):
            c_ord = Scrambler.ord[c]
            if i == 0:
                out = c
            else:
                out = Scrambler.rev_ord[circular_add(salt, c_ord)]

            output += out
            salt = Scrambler.ord[c]

        return output

    def unscramble(self, string):
        salt = Scrambler.ord[string[0]]
        if not salt:
            raise ValueError("Your message is invalid.")

        output = ""

        for i, c in enumerate(string):
            c_ord = Scrambler.ord[c]
            if i == 0:
                out = c
            else:
                last_c_ord = Scrambler.ord[output[-1]]
                out_ord = circular_subtract(c_ord, last_c_ord)
                out = Scrambler.rev_ord[out_ord]

            output += out
            salt = Scrambler.ord[out]

        return output

print(''.join(Scrambler.characters))
d = """Paul awoke to feel himself in the warmth of his bed - thinking... thinking. This world of Castle Caladan, without play or companions his own age, perhaps did not deserve sadness in farewell. Dr. Yueh, his teacher, had hinted that the faufreluches class system was not rigidly guarded on Arrakis. The planet sheltered people who lived at the desert edge without caid or bashar to command them: will-o'-the-sand people called Fremen, marked down on no census of the Imperial Regate.s"""
d2 = """ASCII stands for American Standard Code for Information Interchange. Computers can only understand numbers, so an ASCII code is the numerical representation of a character such as 'a' or '@' or an action of some sort. ASCII was developed a long time ago and now the non-printing characters are rarely used for their original purpose. Below is the ASCII character table and this includes descriptions of the first 32 non-printing characters. ASCII was actually designed for use with teletypes and so the descriptions are somewhat obscure. If someone says they want your CV however in ASCII format, all this means is they want 'plain' text with no formatting such as tabs, bold or underscoring - the raw format that any computer can understand. This is usually so they can easily import the file into their own applications without issues. Notepad.exe creates ASCII text, or in MS Word you can save a file as 'text only'"""
d3 = """They've been pumping basements around the clock in neighborhoods like Pico Avenue where Sean Driscoll's basement flooded and three cars were damaged. He managed to get his family to a hotel but now has no heat, electricity or water. "I was a kid during the blizzard of 78 and this was definitely close to that," he said. "If I didn't get out of the basement when I did, when water passed the electrical panel, I could have been electrocuted," Esposito said. "I'm lucky I got out before that." He says the bucket rescue was a hair-raising experience, but he was grateful for the lift. "The only bad thing was the metal blade was so slippery with and snow it was hard to keep yourself steady," he said. Lt. Governor Karyn Polito met with Winthrop town officials to tour the hard hit area and assess the damage. She is hoping for some federal disaster relief. "We will evaluate all the estimates and then determine what next steps can be taken," Polito said."""
d4 = "Scrambled eggs are yummy."

s = Scrambler()
o = s.scramble(d4)
print(o)
m = s.unscramble(o)
print(m)

