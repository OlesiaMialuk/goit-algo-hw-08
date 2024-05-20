
import heapq
def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        merged_cable = cable1 + cable2
        total_cost += merged_cable
    heapq.heappush(cables, merged_cable)
    return total_cost
cables = [8, 4, 6, 12, 2, 9]
print("Minimum total cost:", min_cost_to_connect_cables(cables))
