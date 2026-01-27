class Solution:
    def bfs(self, adjenceList: dict, valuesMap: dict, src: str, dest: str) -> int:
        if src not in adjenceList or dest not in adjenceList:
            return -1

        fifo = deque()
        fifo.append(src)
        score = defaultdict(int)
        score[src] = 1
        visited = set()
        found = False 

        while len(fifo) != 0:
            node = fifo.popleft()
            if node == dest:
                    found = True
                    return score[node]

            for neighbour in adjenceList[node]:
                if neighbour not in visited:
                    fifo.append(neighbour)
                    score[neighbour] = score[node] * valuesMap[node + '-' + neighbour]
            visited.add(node)

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """

        - BFS (map adj, values) O(Q*E) time O(E) space
        """
        adjenceList = defaultdict(list)
        valuesMap = defaultdict(int)

        for i in range(len(equations)):
            source = equations[i][0]
            destination = equations[i][1]
            value = values[i]

            adjenceList[source].append(destination)
            adjenceList[destination].append(source)

            valuesMap[source + '-' + destination] = value
            valuesMap[destination + '-'+ source] = 1/value

        results = []

        for query in queries:
            querySrc = query[0]
            queryDest = query[1]

            results.append(self.bfs(adjenceList, valuesMap, querySrc, queryDest))

        return results