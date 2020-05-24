import random
import numpy as np
import DFS as dfs


# Dataset Generator
class Dataset:
    def __init__(self, bn, num_cases):
        self.bn = bn    # Bayesian Network
        self.num_cases = num_cases  # number of test
        self.dataset = np.zeros((self.num_cases, self.bn.n))

        # DFS orders the nodes from the root to the leaves
        self.ordered_array = dfs.order(self.bn.dag, self.bn.nodes)

        for i in range(self.num_cases):   # for each test (row)
            for j in range(self.bn.n):   # for each node (column)
                v = float(random.random())
                p = float(self.get_prob(self.ordered_array[j].value, i))
                if v <= p:
                    self.dataset[i][self.ordered_array[j].value] = 1

    # i = node index
    # index = test index
    def get_prob(self, i, index):
        p_i = self.bn.nodes[i].pi

        if len(p_i) == 0:  # no parents
            prob = self.bn.nodes[i].cpt[0]
        else:
            dim = len(p_i)
            s = sorted(p_i)
            k = 0
            for j in range(dim):
                k += 2 ** (dim - j - 1) * self.dataset[index][s[j]]
            prob = self.bn.nodes[i].cpt[int(k)]
        return prob
