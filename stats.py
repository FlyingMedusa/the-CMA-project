from nltk import FreqDist

def counter(need):

    with open("static/files/metaphors.csv") as fopen:
        a_file = fopen.read()

    a_file = a_file.replace("\n",",")
    a_file = a_file.split(",")

    metaphors = [el for el in a_file if a_file.index(el)%2==1]

    target_dom = []
    source_dom = []
    coll = []

    for metaphor in metaphors:
        upper = []
        for a_part in metaphor.split(' '):
            if a_part.isupper():
                upper.append(a_part)
        coll.append(upper)
        target_dom.append(upper[0])
        source_dom.append(upper[1])

    fdist1 = FreqDist(target_dom)
    fdist2 = FreqDist(source_dom)
    target_top5 = fdist1.most_common(5)
    source_top5 = fdist2.most_common(5)

    if need == "target":
        return target_top5
    elif need == "source":
        return source_top5
    elif need == "tlist":
        return target_dom
    elif need == "slist":
        return source_dom
