class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        graph = self.Grapher(edges)
        visited = set()
        length = len(graph)
        count = 0
        if length !=n:
            count += abs(n-length)
        for key,value in graph.items():
            if key not in visited:
                self.DFS(graph,key,visited)
                count+=1
        return count
    def DFS(self,graph,src,visited):
        if src in visited:
            return
        visited.add(src)
        for neighbor in graph[src]:
            self.DFS(graph,neighbor,visited)
    
    def Grapher(self,edges):
        graph = {}
        for key,value in edges:
            if key not in graph:
                graph[key] = []
            if value not in graph:
                graph[value] = []
                
            graph[key].append(value)
            graph[value].append(key)
            
            
        return graph
                    