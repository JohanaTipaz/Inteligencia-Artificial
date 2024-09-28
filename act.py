from collections import deque

# Clase para representar el sistema de transporte
class SistemaTransporte:
    def __init__(self):
        self.grafo = {}

    def agregar_ruta(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)  # Si es bidireccional

    def encontrar_mejor_ruta(self, inicio, fin):
        # Usar BFS para encontrar la ruta más corta
        cola = deque([[inicio]])
        visitados = set()

        while cola:
            ruta_actual = cola.popleft()
            nodo_actual = ruta_actual[-1]

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            if nodo_actual == fin:
                return ruta_actual

            for vecino in self.grafo.get(nodo_actual, []):
                nueva_ruta = list(ruta_actual)  # Copiar la ruta actual
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)

        return None  # Si no se encuentra una ruta

# Ejemplo de uso
sistema = SistemaTransporte()

sistema.agregar_ruta("Estacion1", "Estacion2")
sistema.agregar_ruta("Estacion2", "Estacion3")
sistema.agregar_ruta("Estacion3", "Estacion4")
sistema.agregar_ruta("Estacion1", "Estacion3")
# Buscar la mejor ruta
punto_A = "Estacion1"
punto_B = "Estacion4"

ruta = sistema.encontrar_mejor_ruta(punto_A, punto_B)

if ruta:
    print(f"La mejor ruta desde {punto_A} hasta {punto_B} es: {' -> '.join(ruta)}")
else:
    print(f"No se encontró una ruta desde {punto_A} hasta {punto_B}.")