def topKFrequent(nums, k):
    # 1. Map each number to its frequency
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        
    # 2. Create buckets where index = frequency
    # We need len(nums) + 1 because a number could appear up to len(nums) times
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for n, freq in count.items():
        buckets[freq].append(n)
        
    # 3. Collect the top k elements
    res = []
    # Loop backwards from highest frequency to lowest
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res

    

nums = [1,2,2, 2,3,3,3, 3, 4]
k = 2
print(topKFrequent(nums, k))