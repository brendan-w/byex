#!/usr/bin/python3

import re

target = "<img href=\"/beam-beats\"></a>"

text = [
    "<a href=\"/beam-beats\">Beam Beats</a>",
    "<a href=\"/lasers\">Laser Projection</a>",
]


def tokenize(s):
    tokens = []
    delims = "[\s<>\[\]\{\}\(\);:'\"\\/\?|\-_=\+`~!@#\$%\^&\*]"

    # split a string without deleting splitting chars
    token = ""
    for c in s:
        if re.match(delims, c):
            if token:
                tokens.append(token)
                token = ""
            tokens.append(c)
        else:
            token += c

    # strip out whitespace
    return [t for t in tokens if not re.match("\s", t)]

for line in text:
    print(tokenize(line))

print("target:")
print(repr(tokenize(target)))
