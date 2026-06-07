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

    # función para conectar dos conjuntos distintos en uno solo
    def union(self, padres, i, j):
        raiz_i = self.buscar_padre(padres, i)
        raiz_j = self.buscar_padre(padres, j)
        padres[raiz_i] = raiz_j

    # algoritmo de kruskal para calcular coste mínimo o máximo
    def ejecutar_kruskal(self, modo="minimo"):
        print(f"\nEjecutando Kruskal en modo: {modo}")

        # ordena las aristas según el modo elegido
        if modo == "minimo":
            aristas_ordenadas = sorted(self.aristas, key=lambda x: x[2])
        else:
            aristas_ordenadas = sorted(self.aristas, key=lambda x: x[2], reverse=True)

        # muestra el orden en el que se van a evaluar las aristas
        print("Aristas ordenadas para la simulación:")
        for u, v, p in aristas_ordenadas:
            print(f"   {u} - {v} (peso: {p})")

        # inicializa cada nodo como su propio padre (conjuntos disjuntos)
        padres = {nodo: nodo for nodo in self.nodos}
        
        arbol_final = []
        costo_total = 0
        paso = 1

        # ciclo principal para evaluar cada arista una por una
        for u, v, peso in aristas_ordenadas:
            print(f"[Paso {paso}] Evaluando {u} - {v} con peso {peso}:")
            
            raiz_u = self.buscar_padre(padres, u)
            raiz_v = self.buscar_padre(padres, v)

            # si las raíces son diferentes, los nodos no están conectados y no hay ciclo
            if raiz_u != raiz_v:
                self.union(padres, raiz_u, raiz_v)
                arbol_final.append((u, v, peso))
                costo_total += peso
                print("       Aceptada: No forma ciclo.")
            else:
                print("       Rechazada: Formaría un ciclo.")
            
            paso += 1

            # detiene el algoritmo si ya se tienen las aristas necesarias (nodos - 1)
            if len(arbol_final) == len(self.nodos) - 1:
                break

        # muestra los resultados finales en la consola
        print(f"\nResultado final ({modo}):")
        print("Aristas elegidas:")
        for u, v, peso in arbol_final:
            print(f"   * {u} -- {v} (peso: {peso})")
        print(f"Costo total del árbol: {costo_total}\n")


if __name__ == "__main__":
    simulador = KruskalConsola()
    
    # ejecuta el simulador para ambos casos de estudio
    simulador.ejecutar_kruskal(modo="minimo")
    simulador.ejecutar_kruskal(modo="maximo")