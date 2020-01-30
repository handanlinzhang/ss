import copy
from illustration import generate_uag


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
    neighbours = get_neighbours(z, G)
    chord_moral(G,neighbours)
    C = copy.deepcopy(neighbours)
    C.add(z)

    if C.contain(G):
        return (i,C)
    else:
        G = elim_node(G,z)
        ct.add(buildct(G,order,i+1,link))


    for item in ct:
        if item[1].contain(neighbours):
            link.add((C,item))

    return ct


def elim_node(G,z):
    copy_G = copy.deepcopy(G)
    for index, ele in enumerate(G):
        if index == z:
            copy_G.pop(z)
        else:
            copy_G[index].pop(z)


def chord_moral(G,neighbours):

    for node in neighbours:
        for item in neighbours:
            if node != item:
                if G[node][item] == 0:
                    G[node][item] = 1

def get_neighbours(node_id, G):

    neighbours=G[node_id]
    return [idx for idx, i in enumerate(neighbours) if i == 1]

def moralize(bn):
    """Construct the moral graph from bayesian network

    :param bn: the adjacency matrix of bayesian network
    :return: moral graph of the bayesian network
    """
    moral_graph = copy.deepcopy(bn)
    parents=[]

    for item in bn:
        parents.append([idx for idx, i in enumerate(item) if i==1])
    for item in parents:
        for s in item:
            for e in item:
                if s != e:
                    moral_graph[s][e] = 1

    return moral_graph

if __name__ == '__main__':
    t = [[0,1,1],[1,0,0],[1,0,0]]
    chord_moral(t,[1,2])
    print(t)
    generate_uag(t)

    #print(get_neighbours(0,t))
