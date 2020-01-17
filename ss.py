import copy

def buildct(G, order,i,link):

    '''
    generate the clique tree from BN

    :param G:
    :param order:
    :return:
    '''

    ct=[]
    z = order[0]
    order = order[1:]
    S = get_neighbours(z)
    chord_moral(G)
    C = copy.deepcopy(S)
    C.add(z)

    if C.contain(G):
        return (i,C)
    else:
        G = elim_node(G,z)
        ct.add(buildct(G,order,i+1,link))


    for item in ct:
        if item[1].contain(S):
            link.add((C,item))

    return ct

def moralize(bn):
    link=[]
    for item in bn:
        link.add([idx for idx, i in enumerate(item) if i==1])
    for item in link:
        