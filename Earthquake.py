from Node import Node


# Setup Earthquake Model
def earthquake_gen():
    b = Node("Burglary", set(), [0.01], [0, 1], 0)
    e = Node("Earthquake", set(), [0.02], [0, 1], 1)
    a = Node("Alarm", set([1, 0]), [0.001, 0.29, 0.94, 0.95], [0, 1], 2)
    j = Node("JohnCalls", set([2]), [0.05, 0.9], [0, 1], 3)
    m = Node("MaryCalls", set([2]), [0.01, 0.7], [0, 1], 4)

    return [b, e, a, j, m]
