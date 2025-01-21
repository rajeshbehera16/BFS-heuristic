import heapq
graph = {
   0: [1, 2],
   1: [0, 3, 4],
   2: [0, 5],
   3: [1],
   4: [1],
   5: [2]
}
heuristic = {
   0: 10,
   1: 8,
   2: 5,
   3: 7,
   4: 3,
   5: 0  
}
start_node = 0
goal_node = 5
priority_queue = []
heapq.heappush(priority_queue, (heuristic[start_node], start_node))
visited = set()
path = []
 

while priority_queue:
  
   _, current = heapq.heappop(priority_queue)
   
   if current in visited:
       continue
   
  
   visited.add(current)
   path.append(current)

   if current == goal_node:
       break
   for neighbor in graph[current]:
       if neighbor not in visited:
           heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
print("Best-First Search Traversal:", path)
 