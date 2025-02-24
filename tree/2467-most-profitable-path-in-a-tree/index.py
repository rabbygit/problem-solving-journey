import collections
from typing import List


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        bob_times = {}
        adj = collections.defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(src, prev, time):
            if src == 0:
                bob_times[src] = time
                return True

            for nei in adj[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True

            return False

        # track bob's time during traversal to root
        dfs(bob, -1, 0)

        q = collections.deque(
            [(0, 0, -1, amount[0])]
        )  # node, previous node, time, profit
        res = float("-inf")

        while q:
            node, time, parent, profit = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                nei_profit = amount[nei]
                nei_time = time + 1

                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]:
                        nei_profit = nei_profit // 2

                q.append((nei, nei_time, node, profit + nei_profit))
                
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)

        return res
