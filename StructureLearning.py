import numpy as np
import math
import itertools
import copy


def cartesian_product(n, f_i):
    # n  = number of parents
    x = [0, 1]
    y = []
    count = 0
    for j in range(n):
        y.append(x)

    for itr in itertools.product(*y):
        f_i[count] = itr
        count += 1

    return f_i


def count_case(dataset, f_i, p_i, i, j, k):
    # i = variable index
    # j = parents configuration
    # k  = value that can take the variable i
    # f_i set of configurations of the parents of i

    a_ijk = 0
    t = f_i[j]
    if len(p_i) == 0:
        for m in range(len(dataset)):
            if dataset[m][i] == k:
                a_ijk = a_ijk + 1
    else:
        for m in range(len(dataset)):
            if dataset[m][i] == k:
                count = True
                s = list(p_i)
                s = sorted(s)
                a = - 1
                for index in range(len(s)):
                    a = a + 1
                    x = s[index]
                    if dataset[m][x] != t[a]:
                        count = False
                if count:
                    a_ijk = a_ijk + 1
    return a_ijk


def score(dataset, node_i, p_i):
    # node_i = node on focus
    # p_i = parents array of node_i

    r_i = len(node_i.domain_values)
    i = node_i.value
    q_i = 2 ** (len(p_i))
    f_i = np.zeros((q_i, (len(p_i))))
    f_i = cartesian_product(len(p_i), f_i)
    score = 1
    j = 0

    while j < q_i:
        n_ij = 0
        p2 = 1
        for k in range(r_i):
            a_ijk = count_case(dataset, f_i, p_i, i, j, node_i.domain_values[k])
            n_ij = n_ij + a_ijk
            p2 = p2 * math.factorial(a_ijk)

        num_p1 = math.factorial(r_i - 1)
        dem_p1 = math.factorial(n_ij + r_i - 1)
        p1 = num_p1 / dem_p1
        product = p1 * p2

        score = score * product
        j = j + 1

    return score


def maximize_score(dataset, nodes, i, pred):
    p_max = -1
    z = -1
    node_i = nodes[i]
    p_i = nodes[i].parents
    # set difference
    diff = pred - p_i
    for x in diff:
        tmp = copy.deepcopy(p_i)
        tmp.add(nodes[x].value)
        local_score = score(dataset, node_i, tmp)
        if local_score >= p_max:
            z = x
            p_max = local_score

    return z, p_max


def k2(dataset, nodes, upper_bound):
    n = len(nodes)
    for i in range(n):
        nodes[i].parents = set()

    for i in range(n):
        pred = set()
        for x in range(i):
            pred.add(x)
        p_old = score(dataset, nodes[i], nodes[i].parents)
        ok = True
        while ok == True and len(nodes[i].parents) < upper_bound:
            (z, p_new) = maximize_score(dataset, nodes, i, pred)

            if p_new >= p_old:
                p_old = p_new
                nodes[i].parents.add(nodes[z].value)
                pred.remove(z)
            else:
                ok = False

    dag = np.zeros((n, n))
    for r in range(len(nodes)):
        s = list(nodes[r].parents)
        for c in range(len(s)):
            i = nodes[r].value
            j = s[c]
            dag[j][i] = 1

    return dag
