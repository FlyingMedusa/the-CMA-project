from matplotlib import pyplot as plt

def generate_g1(fdist_abst):

    labels = []
    sizes = []
    for mark in fdist_abst:
        labels.append(mark[0])
        sizes.append(mark[1])

    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.05, 0.05, 0.05, 0.05)
    if len(fdist_abst) == 3:
        colors = colors[:3]
        explode = (0.05, 0.05, 0.05)
    elif len(fdist_abst) == 2:
        colors = colors[:2]
        explode = (0.05, 0.05)

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, wedgeprops={"edgecolor":"k",'linewidth': 1, 'antialiased': True})

    plt.axis('equal')

    plt.savefig('static/images/graph1.png')
    plt.close('all')

def generate_g2(fdist_abst_target):

    labels2 = []
    sizes2 = []
    for mrk in fdist_abst_target:
        labels2.append(mrk[0])
        sizes2.append(mrk[1])

    if len(fdist_abst_target) == 2:
        colors = ['gold', 'yellowgreen']
        explode = (0.05, 0.05)
    elif len(fdist_abst_target) == 1:
        colors = ['gold']
        explode = (0.05)

    plt.pie(sizes2, explode=explode, labels=labels2, colors=colors,
    autopct='%1.1f%%', shadow=True, wedgeprops={"edgecolor":"k",'linewidth': 1, 'antialiased': True})

    plt.axis('equal')

    plt.savefig('static/images/graph2.png')
    plt.close('all')

def generate_g3(fdist_abst_source):

    labels3 = []
    sizes3 = []
    for mrk in fdist_abst_source:
        labels3.append(mrk[0])
        sizes3.append(mrk[1])

    if len(fdist_abst_source) == 2:
        colors = ['gold', 'yellowgreen']
        explode = (0.05, 0.05)
    elif len(fdist_abst_source) == 1:
        plt.pie(sizes3, labels=labels3, colors=['gold'],
        autopct='%1.1f%%', shadow=True, wedgeprops={"edgecolor":"k",'linewidth': 1, 'antialiased': True})

    plt.axis('equal')

    plt.savefig('static/images/graph3.png')
    plt.close('all')
