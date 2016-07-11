#!/usr/bin/python3

a = "<a href=\"bar\" class=\"foo\"></a>"
b = "<a class=\"foo\" href=\"bar\"></a>"

text = "<header><a href=\"bar\" class=\"foo\"></a><a href=\"bar\" class=\"asdfasdfasdf\"></a></header>"

T="#"
F=" "

def cdiff(bigger, smaller):
    substrs = []

    # loop through starting indeicies in the larger string
    for i in range(len(bigger)):
        line = ""
        run = 0
        for k in range(len(smaller)):

            # when the smaller string falls off the end of the bigger string
            if i + k > (len(bigger) - 1):
                break;

            s_char = smaller[k]
            b_char = bigger[i + k]

            if s_char == b_char:
                line += T
                run += 1
            else:
                line += F
                if run > 0:
                    substrs.append((run, i, k))
                    run = 0

        if run > 0:
            substrs.append((run, i, k))


        print((F*i) + line + (F*(len(bigger)-len(smaller)-i)))

    # sort by run length
    print(sorted(substrs, key=lambda substr: substr[0]))

print(text)
cdiff(text, a)
