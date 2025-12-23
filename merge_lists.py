import heapq


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    merged_lists = merge_two_lists(lists[0], lists[1])
    lists[:2] = [merged_lists]
    return merge_k_lists(lists)

       
def merge_two_lists(first: list[int], second: list[int]) -> list[int]:
    merged = []
    heapq.heapify(first)
    heapq.heapify(second)
    while first and second:
        if first[0] < second[0]:
            smallest = heapq.heappop(first)
        else:
            smallest = heapq.heappop(second)
        merged.append(smallest)
    
    while first:
        merged.append(heapq.heappop(first))
    while second:
        merged.append(heapq.heappop(second))

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
        

