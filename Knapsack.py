import sys
from Config import Task,tasks  


def Fill_Knapsack(knapsack_size):

    max_capacity = knapsack_size
    n = len(tasks)

    
    # Create DP table
    dp = [[0 for _ in range(max_capacity+1)] for _ in range(n+1)]
    
    # Fill DP table
    for i in range(1, n+1):
        e = tasks[i-1]
        for w in range(max_capacity+1):
            if e.length <= w:
                dp[i][w] = max(e.importance + dp[i-1][int(w - e.length)], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Reconstruct chosen items
    chosen_items = []
    space_used = 0
    w = max_capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            e = tasks[i-1]
            chosen_items.append(e)
            tasks.remove(e)
            space_used += e.length
            w -= int(e.length)
    
    chosen_items.reverse()

    print("\nKnapsack filled with maximum value:", dp[n][max_capacity])
    print("Items chosen:")
    for item in chosen_items:
        print(item)
    print(f"Space used={space_used} Space remaining={max_capacity-space_used}")
    # print("Remaining Items")
    # for item in items:
    #     print(item)

    return chosen_items


def Generate_Schedule():
    schedule = {day: [] for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]}
    start_time = 8  #  8 = 8am
    end_time = 20   # 20 = 8pm
    day_length = end_time - start_time

    print(tasks)

    for day in schedule:
        print(day)
        Fill_Knapsack(day_length)





    