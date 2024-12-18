from collections import defaultdict, deque

def process_rules(data: list[str]) -> dict[int, list[int]]:
    graph = defaultdict(list)
    for line in data:
        if not line.strip():
            break
        x, y = map(int, line.strip().split('|'))
        graph[x].append(y)
    return graph

def order_pages(update: list[int], graph: dict[int, list[int]]) -> list[int]:
    subgraph = {page: set() for page in update}
    for page in update:
        if page in graph:
            for neighbor in graph[page]:
                if neighbor in subgraph:
                    subgraph[page].add(neighbor)

    in_degree = {page: 0 for page in subgraph}
    for page, neighbors in subgraph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    
    queue = deque([page for page in subgraph if in_degree[page] == 0])
    topological_order = []
    
    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor in subgraph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topological_order

def is_valid_order(update: list[int], graph: dict[int, list[int]]) -> bool:
    return order_pages(update, graph) == update

def main():
    with open('day05/input.txt', 'r') as f:
        data = f.readlines()
    
    split_index = data.index('\n')
    rules_data = data[:split_index]
    updates_data = data[split_index + 1:]
    
    graph = process_rules(rules_data)
    sum1 = 0
    sum2 = 0
    
    for update_line in updates_data:
        update = list(map(int, update_line.strip().split(',')))
        if not is_valid_order(update, graph):
            correct_order = order_pages(update, graph)
            middle = correct_order[len(correct_order) // 2]
            sum2 += middle
        else:
            middle = update[len(update) // 2]
            sum1 += middle
            
            
    print("Parte 1:", sum1)
    print("Parte 2:", sum2)

if __name__ == "__main__":
    main()
