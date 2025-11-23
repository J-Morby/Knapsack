
events = []

class Event:
    def __init__(self, name, length, value):
        self.name = name
        self.length = length
        self.value = value
    
    def __repr__(self):
        return (f"Event(name={self.name}, length={self.length}, "
                f"value={self.value})")


def EventGanerator():
    count = int(input("How many objects? "))
    for i in range(count):
        name = input("Enter name? ")
        length = float(input("Enter length? "))
        value = float(input("Enter value? "))
        events.append(Event(name, length, value))


def PrintEvents():
    print("\nGenerated Items:")
    for item in events:
        print(item)


class Knapsack:
    def __init__(self, size):
        self.size = size

    def FillKnapsack(self):
        self.size = int(input("How big is your knapsack? "))
        n = len(events)
        capacity = int(self.size)
        
        # Create DP table
        dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
        
        # Fill DP table
        for i in range(1, n+1):
            e = events[i-1]
            for w in range(capacity+1):
                if e.length <= w:
                    dp[i][w] = max(e.value + dp[i-1][int(w - e.length)], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # Reconstruct chosen items
        chosen = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                e = events[i-1]
                chosen.append(e)
                w -= int(e.length)
        
        chosen.reverse()
        
        print("\nKnapsack filled with maximum value:", dp[n][capacity])
        print("Items chosen:")
        for item in chosen:
            print(item)


EventGanerator()
PrintEvents()
Knapsack.FillKnapsack(Knapsack)
