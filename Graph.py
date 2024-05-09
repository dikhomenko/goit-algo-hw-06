import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин та ребер
nodes = ["Home", "School", "Work", "Tennis", "Cafe", "Football"]
edges = [("Home", "School"), ("Home", "Work"), ("School", "Work"), ("School", "Tennis"), ("Tennis", "Cafe"), ("Cafe", "Football"), ("Work", "Cafe")]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 5))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_color='black')
plt.title("Social Network Graph")
plt.show()

# Основні характеристики графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Ступені вершин
degrees = dict(G.degree())
print("Ступені вершин:", degrees)

# Обчислення кластерного коефіцієнта
clustering_coef = nx.clustering(G)
print("Кластерний коефіцієнт для кожної вершини:", clustering_coef)

# Обчислення середнього кластерного коефіцієнта
average_clustering = nx.average_clustering(G)
print("Середній кластерний коефіцієнт:", average_clustering)



# Task 2

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Створення графа з попереднього прикладу
G = nx.Graph()
nodes = ["Home", "School", "Work", "Tennis", "Cafe", "Football"]
edges = [("Home", "School"), ("Home", "Work"), ("School", "Work"), ("School", "Tennis"), ("Tennis", "Cafe"), ("Cafe", "Football"), ("Work", "Cafe")]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Знайти всі шляхи від 'Home' до 'Football' за допомогою DFS і BFS
print("DFS paths:")
dfs_result = list(dfs_paths(G, 'Home', 'Football'))
for path in dfs_result:
    print(path)

print("\nBFS paths:")
bfs_result = list(bfs_paths(G, 'Home', 'Football'))
for path in bfs_result:
    print(path)



# Task 3

# Створення графа з вагами
G = nx.Graph()
edges_with_weights = [("Home", "School", 2), ("Home", "Work", 3), ("School", "Work", 1), 
                      ("School", "Tennis", 4), ("Tennis", "Cafe", 1), ("Cafe", "Football", 5), ("Work", "Cafe", 2)]
G.add_weighted_edges_from(edges_with_weights)

# Візуалізація графа з вагами
pos = nx.spring_layout(G, seed=42)  # для стабільності розташування
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Social Network Graph with Weights")
plt.show()


# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від 'Home'
shortest_paths = nx.single_source_dijkstra_path(G, 'Home')
shortest_paths_lengths = nx.single_source_dijkstra_path_length(G, 'Home')

print("Найкоротші шляхи від Home:")
for target, path in shortest_paths.items():
    print(f"{target}: {path}, Вага: {shortest_paths_lengths[target]}")
    