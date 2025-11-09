import heapq

def dijkstrafordcarb(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}

    heap = [(0, start)]
    count_relax = {node: 0 for node in graph}  # contatore di rilassamenti

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

                count_relax[v] += 1
                if count_relax[v] > len(graph):
                    raise ValueError("Il grafo contiene un ciclo negativo")

    return dist, prev

# Esempio di grafo
graph = {
    's': [('a', 1), ('b', 5), ('d',2)],
    'a': [('c', 2)],
    'b': [('c', 1)],
    'c': [('d',3)],
    'd': [('a', -2)],  # arco negativo, ma ciclo totale positivo
}

distances, previous = dijkstrafordca(graph, 's')
print("Distanze minime:", distances)
print("Precedenti:", previous)
