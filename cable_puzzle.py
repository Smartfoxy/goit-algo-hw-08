import heapq


def min_cost_to_connect_cables(cables):
    if not cables:
        return 0
    if len(cables) == 1:
        return 0
    
    heapq.heapify(cables)
    total_costs = 0
    while len(cables) > 1:
        min_1 = heapq.heappop(cables)
        min_2 = heapq.heappop(cables)
        union_cost = min_1 + min_2
        heapq.heappush(cables, union_cost)
        total_costs += union_cost

    return total_costs

print(min_cost_to_connect_cables([10, 20, 30]))  # 90
print(min_cost_to_connect_cables([1, 2, 3, 4]))  # 19



