import numpy as np
from BayesianNet import BayesianNet
from Dataset import Dataset
import StructureLearning as sl


def main():
    num_cases = 150
    num_learn = 1000

    bn = BayesianNet()
    print('Adjacency matrix: \n' + str(bn.dag))

    dag = np.zeros((5, 5))
    for i in range(num_learn):
        data = Dataset(bn, num_cases)
        dag += sl.k2(data.dataset, data.ordered_array, 2)

    for i in range(len(dag)):
        for j in range(len(dag)):
            if dag[i][j] < (num_learn/2):
                dag[i][j] = 0
            else:
                dag[i][j] = 1

    print('Learned structure: \n' + str(dag))


if __name__ == "__main__":
    main()
