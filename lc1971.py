from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        succeeding_nodes = self.get_succeeding_nodes(edges)
        nodes_to_traverse = set(succeeding_nodes[source])
        traversed_nodes = {source}
        while nodes_to_traverse:
            node = nodes_to_traverse.pop()
            if node in traversed_nodes:
                continue
            elif node == destination:
                return True
            else:
                traversed_nodes.add(node)
                nodes_to_traverse |= succeeding_nodes[node]
        return False

    def get_succeeding_nodes(self, edges: List[List[int]]) -> Dict[int, Set[int]]:
        succeeding_nodes = defaultdict(set)
        for start, end in edges:
            succeeding_nodes[start].add(end)
            succeeding_nodes[end].add(start)
        return succeeding_nodes

if __name__ == "__main__":
    assert Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
    assert Solution().validPath(1, [], 0, 0)
    assert Solution().validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9)
    print("success")
