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
    """Construct the moral graph from bayesian network

    :param bn: the adjacency matrix of bayesian network
    :return: moral graph of the bayesian network
    """
    moral_graph = copy.deepcopy(bn)
    parents=[]

    for item in bn:
        parents.add([idx for idx, i in enumerate(item) if i==1])
    for item in parents:
        for s in item:
            for e in item:
                if s != e:
                    moral_graph[s][e] = 1

    return moral_graph

