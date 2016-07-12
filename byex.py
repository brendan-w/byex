#!/usr/bin/python3

#a = "<a href=\"foo\"></a>"
a = "<a href=\"/beam-beats\">Beam Beats</a>"
b = "<a href=\"/lasers\">Laser Projection</a>"


rep = "<a href=\"bar\"></a>"

#text = "<header><a href=\"foo\"></a><a href=\"bar\"></a><a href=\"baaaaar\"></a></header>"
text = """
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="author" content="Brendan Whitfield">
		<meta name="description" content="Brendan Whitfield&#39;s Portfolio">
		<meta name="keywords" content="portfolio, developer, programmer, programming, creative, interactive">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width,initial-scale=1">
		<title>Brendan Whitfield | Interactive Developer</title>
		<link rel="shortcut icon" type="image/png" href="/assets/favicon-32.png">
		<link rel="apple-touch-icon" type="image/png" href="/assets/favicon-120.png">
	</head>
	<body class="mode-home fadeout">
		<div class="graphics" id="bg"></div>
		<div class="graphics" id="grid"></div>
		<div id="content">
			<header class="border-top">
				<nav id="main">
					<a href="/about">About</a>
					<a href="https://github.com/brendan-w">GitHub</a>
					<a href="/assets/brendan_whitfield_resume.pdf" rel="external">Résumé</a>
					<a href="mailto:me@brendan-w.com">me@brendan-w.com</a>
				</nav>
				<div id="tower">
					<hr class="top">
					<h1><a href="/" id="name">
						<span class="fl">Brendan</span>
						<span class="fr">Whitfield</span>
					</a></h1>
					<nav id="projects">
						<a href="/beam-beats">Beam Beats</a>
						<a href="/lasers">Laser Projection</a>
						<a href="/python-obd">Python OBD-II Module</a>
						<a href="/rng">Nuclear Hardware RNG</a>
						<a href="/cgraph">C-Graph</a>
						<a href="/collector">Collector</a>
						<a href="/lumber">Lumber Segmenter</a>
						<a href="/executejs">Execute JS</a>


						<a href="/ir">Universal IR Remote</a>
						<a href="/archive">Archive</a>
					</nav>
					<div class="opener">
						<a href="#">projects</a>
					</div>
					<hr class="bottom">
				</div>
			</header>
			<article></article>
		</div>
		<footer>© Brendan Whitfield 2015</footer>
	</body>
</html>
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

    # sort in this order:
    #    ascending starting index in the larger
    #    ascending starting index in the smaller
    substrs = sorted(substrs, key=lambda substr: (substr[1], substr[2]))
    return substrs


substrs = cdiff(b, a)

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
"""
