import heapq

def mergeKLists(lists):
    heap = []

    for linked_list in lists:
        for val in linked_list:
            heapq.heappush(heap, val)
    
    merged_list = []
    
    while heap:
        merged_list.append(heapq.heappop(heap))
    
    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(mergeKLists(lists))  
    