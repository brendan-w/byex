#!/usr/bin/python3

a = "<a href=\"bar\" class=\"foo\"></a>"
b = "<a class=\"foo\" href=\"bar\"></a>"

text = """
<html>
<head></head>
<body>
<header>
<a href=\"bar\" class=\"foo\"></a>
<a href=\"bar\" class=\"bazz\"></a>
<a href=\"bar\" class=\"asdfasdfasdf\"></a>
</header>
<footer></footer>
</body>
</html>
"""

segments = {} # len : [(a_pos, b_pos)]

def add_segment(rl, ai, bi):
    segments[rl] = segments.get(rl, []) + [(ai-rl, bi-rl)]

def cdiff(a, b, shift):
    output = []
    rl = 0
    for i in range(len(a)):
        ac = a[i]
        bi = (i + shift) % len(a)
        bc = b[bi]

        if ac == bc:
            output += [1]
            rl += 1
        else:
            output += [0]
            if rl > 0:
                add_segment(rl, i, bi)
                rl = 0

    if rl > 0:
        add_segment(rl, i, bi)

    return output


lines = []

for shift in range(len(a)):
    lines.append(cdiff(a, b, shift))


for line in lines:
    readout = "".join(["#" if i else "_" for i in line])
    chars = "".join([c if line[i] else " " for i, c in enumerate(a)])
    print("|" + readout + "|" + chars + "|")


for rl in segments:
    print(str(rl) + ": " + str(segments[rl]))
