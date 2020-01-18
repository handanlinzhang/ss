import networkx as nx
import matplotlib.pyplot as plt


def generate_uag(adj_matrix):
    """

    :return:
    """
    G = nx.Graph()
    node_num = len(adj_matrix)
    for index in range(node_num):
        G.add_node(index)

    for ch_index, out_nodes in enumerate(adj_matrix):
        [G.add_edge(pa_index, ch_index) for pa_index, link in enumerate(out_nodes) if link == 1]
    plt.subplot()
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


def generate_dag(adj_matrix):

    G = nx.DiGraph()
    node_num = len(adj_matrix)
    for index in range(node_num):
        G.add_node(index)

    for ch_index,out_nodes in enumerate(adj_matrix):
        [G.add_edge(pa_index,ch_index) for pa_index,link in enumerate(out_nodes) if link == 1]

    plt.subplot()
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == '__main__':
    adj = [[0,1,1],[1,0,0],[1,0,0]]
    generate_dag(adj)