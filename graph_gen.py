from matplotlib import pyplot as plt

def generate_g1(tlist, slist):

    def text_size(total: int) -> float:
        return 12 + total / 80 * 100

    masterset = set(tlist + slist)

    metaphors = {}
    for el in sorted(masterset):
        metaphors[el] = [0, 0]
        if el in tlist:
            metaphors[el][0] = tlist.count(el)
        else:
            metaphors[el][0] = 0
        if el in slist:   
            metaphors[el][1] = slist.count(el)
        else:
            metaphors[el][1] = 0
    
    for key in metaphors:
        plt.text(metaphors[key][0], metaphors[key][1],key, ha='center', va='center', size=text_size(metaphors[key][0] + metaphors[key][1]), color ='darkcyan')

    plt.xlabel("Popularity in target domains")
    plt.ylabel("Popularity in source domains")
    plt.axis([0,13,0,13])
    plt.xticks([])
    plt.yticks([])


    plt.savefig('static/images/graph1.png')
