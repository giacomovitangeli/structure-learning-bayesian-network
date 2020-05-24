class Node:
    def __init__(self, name, pi, cpt, domain_values, value):
        self.name = name
        self.value = value
        self.pi = pi
        self.cpt = cpt
        self.domain_values = domain_values
        self.color = 'White'
        self.f = 0
