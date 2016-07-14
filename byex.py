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

lines = [tokenize(line) for line in text]

for line in lines:
    print(line)

target = tokenize(target)
print("target:")
print(target)


def get_exemplar(lines, target):
    """ find the line with the most matching tokens """
    best = 0
    exemplar = ""

    for line in lines:
        n = sum([ int(token in target) for token in line ])
        if n > best:
            best = n
            exemplar = line

    return exemplar

print("exemplar:")
print(get_exemplar(lines, target))
