class KruskalConsola:
    def __init__(self):
        # lista de aristas con formato (nodo1, nodo2, peso)
        self.aristas = [
            ('A', 'B', 4), ('A', 'C', 2),
            ('B', 'C', 1), ('B', 'D', 5),
            ('C', 'D', 8), ('C', 'E', 10),
            ('D', 'E', 2)
        ]
        # lista de los nodos del grafo
        self.nodos = ['A', 'B', 'C', 'D', 'E']

    # función para encontrar la raíz del conjunto al que pertenece un nodo
    def buscar_padre(self, padres, i):
        if padres[i] == i:
            return i
        return self.buscar_padre(padres, padres[i])

