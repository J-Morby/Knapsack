import sys

class Item:
    def __init__(self, name, value, size):
        self.name = name
        self.value = value
        self.size = size

    def __repr__(self):
        return (f"Item (name={self.name}, "f"value={self.value}, size={self.size})")
    


def Solve(knapsack_size, data):

    items = []
    for row in data:
        name = row[0]
        value = int(row[1])
        size  = int(row[2])
        items.append(Item(name, value, size))

    max_capacity = knapsack_size
    n = len(data)

    
    # Create DP table
    dp = [[0 for _ in range(max_capacity+1)] for _ in range(n+1)]
    
    # Fill DP table
    for i in range(1, n+1):
        e = items[i-1]
        for w in range(max_capacity+1):
            if e.size <= w:
                dp[i][w] = max(e.value + dp[i-1][int(w - e.size)], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Reconstruct chosen items
    chosen = []
    space_used = 0
    w = max_capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            e = items[i-1]
            chosen.append(e)
            space_used += e.size
            w -= int(e.size)
    
    chosen.reverse()
    
    print("\nKnapsack filled with maximum value:", dp[n][max_capacity])
    print("Items chosen:")
    for item in chosen:
        print(item)
    print(f"Space used={space_used} Space remaining={max_capacity-space_used}")
    
