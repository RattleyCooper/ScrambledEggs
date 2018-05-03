ScrambledEggs is a text encoding / obfuscation tool that was created
for fun. 

It turns text into something like this:

    gGj}z(*:8~g0Dr'#Q_a3.8`~.!05FEYf i98)#?bdVi%*Ab'*5Dc*&}*a#|zM_Ti^o'~=`Vr6LGe-o	gE1S\p|+Tunx?_tk$:Y}	(,;SQan*ODMUq?=;P5

^ that is the first 4 lines of this README.md encoded.


Example:

    s = Scrambler()
    encoded = s.scramble('Hello world')
    decoded = s.unscramble(encoded)

