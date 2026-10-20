class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points: 
            if len(heap) < k:
                heapq.heappush(heap, (-(point[0]*point[0] + point[1]*point[1]), point))
            elif len(heap) == k and -(point[0]*point[0] + point[1]*point[1]) > heap[0][0]:
                heapq.heapreplace(heap, (-(point[0]*point[0] + point[1]*point[1]), point))
        
        ans = []
        for entry in heap:
            ans.append(entry[1])

        return ans
