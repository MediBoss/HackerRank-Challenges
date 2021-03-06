

import heapq

def find_shortest_path(graph, source):
    
    # Set the initial distance to the source to 0 and all to infinity
    weight_to_get_to = { node : float('inf') for node in graph }
    weight_to_get_to[source] = 0

    # Keep track of nodes that's already dequeued - which means we've already found the shortest path to them
    dequeued_nodes = set()

    # Priority queue ordering nodes by the weight to get to them
    priority_queue = []
    for node in graph:
        # Putting all the nodes and their weights into the 
        heapq.heappush(priority_queue, (weight_to_get_to[node], node)) # heapq builds an array of tuples with a node and its weight
    
    while len(priority_queue) > 0:
        
        # deque the next node and its weight from the priority queue
        cheapest_cost, cheapest_node = heapq.heappop(priority_queue)
        # Add the dequeued node in the set of visited nodes
        dequeued_nodes.add(cheapest_node)

        # Visit the neighbors of the dequeued nodes
        for neighbor, weight in graph[cheapest_node]:

            # Skip the neighbor that's seen already
            if neighbor in dequeued_nodes:
                continue
            # Can we get there cheapely via the neighbor
            if weight_to_get_to[cheapest_node] + weight < weight_to_get_to[neighbor]:

                # Update the cost the cost to reach the node
                Updated_weight = weight_to_get_to[cheapest_node] + weight
                weight_to_get_to[neighbor] = Updated_weight
                # upadte the cost to reach this node in the priority queue
                heapq.heapreplace(priority_queue, (neighbor, weight_to_get_to[neighbor]))
            
    return weight_to_get_to

def main():
    
    graph = {}
    graph["A"] = [("B", 1), ("D", 3), ("C", 4)]
    graph["B"] = [("A", 1), ("C", 7)]
    graph["C"] = [("B", 7), ("D", 6), ("A", 4)]
    graph["D"] = [("A", 3), ("C", 6)]

    find_shortest_path(graph, "A")

if __name__ == "__main__":
    main()
