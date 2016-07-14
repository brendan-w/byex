#!/usr/bin/python3

from itertools import groupby

example = "<img href=\"/beam-beats\">Beam Beats</img>"

text = """
<!doctype html>
<nav id="projects">
	<a href="/beam-beats">Beam Beats</a>
	<a href="/lasers">Laser Projection</a>
	<a href="/python-obd">Python OBD-II Module</a>
	<a href="/rng">Nuclear Hardware RNG</a>
</nav>
"""

"""
	<a href="/cgraph">C-Graph</a>
	<a href="/collector">Collector</a>
	<a href="/lumber">Lumber Segmenter</a>
	<a href="/executejs">Execute JS</a>
	<a href="/ir">Universal IR Remote</a>
	<a href="/archive">Archive</a>
"""

T="#"
F="_"

def cdiff(bigger, smaller):
    substrs = []

    # loop through starting indicies in the larger string
    for i in range(len(bigger)):
        # line = ""
        run = 0
        for k in range(len(smaller)):

            # when the smaller string falls off the end of the bigger string
            if i + k > (len(bigger) - 1):
                break;

            s_char = smaller[k]
            b_char = bigger[i + k]

            if s_char == b_char:
                # line += T
                run += 1
            else:
                # line += F
                if run > 0:
                    substrs.append((run, (i+k)-run, k-run))
                    run = 0

        # catch matches at the tail end
        if run > 0:
            substrs.append((run, (i+k)-run, k-run))


        #print((F*i) + line + (F*(len(bigger)-len(smaller)-i)))
        #print(line)

    return substrs


def filter_largest_spanning_substrs(substrs):
    # sort groups by descending length
    substrs = sorted(substrs, key=lambda substr: -substr[0])

    indices = set()
    output = []

    for substr in substrs:
        substr_completed = True
        for i in range(substr[1], substr[1] + substr[0]):
            if i in indices:
                substr_completed = False
                break
            else:
                indices.add(i)

        if substr_completed:
            output.append(substr)

    return output


substrs = cdiff(text, example)
substrs = filter_largest_spanning_substrs(substrs)

# sort in this order:
#    ascending starting index in the larger
#    ascending starting index in the smaller
substrs = sorted(substrs, key=lambda substr: (substr[1], substr[2]))



"""
for substr in substrs:
    comment = ""
    if substr[2] == 0:
        comment = " <--- start"
    elif substr[0] + substr[2] == (len(a) - 1):
        comment = " <--- end"
    print(repr(substr) + comment)
"""

matches = []
match = []
i = 0
for substr in substrs:
    if substr[2] < i:
        matches.append(match)
        match = [substr]
    else:
        match.append(substr)
    i = substr[2]

for m in matches:
    print(m)
