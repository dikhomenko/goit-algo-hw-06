
---

## Аналіз шляхів у графі за допомогою алгоритмів DFS, BFS та Дейкстри

### Опис алгоритмів DFS та BFS

DFS (Пошук у глибину) і BFS (Пошук у ширину) використовують різні підходи для пошуку шляхів у графах:

- **DFS (Пошук у глибину)**: Цей алгоритм проходить граф настільки глибоко, наскільки це можливо, перш ніж рухатися до інших вершин. Він використовує стек для управління процесом, що може призвести до знаходження довших і більш "глибоких" шляхів.

- **BFS (Пошук у ширину)**: Навпаки, BFS розповсюджується рівномірно від початкової вершини і використовує чергу для управління вершинами. Цей метод гарантує знаходження найкоротших шляхів в термінах кількості кроків.

### Застосування алгоритму Дейкстри

Алгоритм Дейкстри використовується для знаходження найкоротших шляхів від однієї вершини до всіх інших у важеному графі:

```python
import networkx as nx

G = nx.Graph()
edges_with_weights = [
    ("Alice", "Bob", 2), ("Alice", "Charlie", 3),
    ("Bob", "Charlie", 1), ("Bob", "David", 4),
    ("David", "Eve", 1), ("Eve", "Frank", 5),
    ("Charlie", "Eve", 2)
]
G.add_weighted_edges_from(edges_with_weights)

shortest_paths = nx.single_source_dijkstra_path(G, 'Alice')
shortest_paths_lengths = nx.single_source_dijkstra_path_length(G, 'Alice')

print("Найкоротші шляхи від Alice:")
for target, path in shortest_paths.items():
    print(f"{target}: {path}, Вага: {shortest_paths_lengths[target]}")
```

### Результати

Вивід алгоритму Дейкстри показує оптимальні шляхи з урахуванням ваг ребер, що ідеально підходить для задач, де ваги ребер мають велике значення, наприклад, у транспортних мережах або в маршрутизації мережевого трафіку.

### Висновок

Застосування різних алгоритмів пошуку дозволяє розуміти їх підходи та обирати найкращий залежно від контексту задачі. DFS і BFS ідеально підходять для ненавантажених графів, тоді як Дейкстра — незамінний інструмент для важених графів, де потрібно знайти найефективніший шлях.

---