class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Classic topological order graph problem.

        vII of the detects cycle in the graph.

        """
        # Build the adjacency list and in-degree count
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with nodes having zero in-degree
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if topological sort includes all nodes
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []
