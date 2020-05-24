import numpy as np
import Earthquake


class BayesianNet:

    def __init__(self):
        self.nodes = Earthquake.earthquake_gen()  # nodes array from earthquake model
        self.n = len(self.nodes)  # number of nodes
        self.dag = np.zeros((self.n, self.n))  # Adjacency matrix
        self.dag_generator()

    def dag_generator(self):
        for i in range(self.n):  # nodes index
            for j in self.nodes[i].pi:  # parents index
                self.dag[j][i] = 1

    def print_graph(self):
        print(self.dag)
