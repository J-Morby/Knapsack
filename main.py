events = []

def main():
    pass


class Calener:
    def __init__(self):
        pass
        

class Knapsack:
    def __init__(self, name, length, value, denominations):
        self.name = name
        self.length = length
        self.value = value
        self.denomination = denominations
    
    def __repr__(self):
        return (f"Item(name={self.name}, length={self.length}, "
                f"value={self.value}, denominations={self.denomination})")
    

def KnapsackGenerator():
    count = int(input("How many objects? "))
    for i in range(count):
        name = input("enter name? ")
        length = float(input("enter length? "))
        value = float(input("enter value? "))
        denomination = float(input("enter denominations? "))
        
        # FIXED — create a Knapsack object, not calling the string 'name'
        events.append(Knapsack(name, length, value, denomination))


def PrintKnapsack():
    print("\nGenerated Items:")
    for item in events:
        print(item)


class Event:
    def __init__(self):
        pass


# --- Run app ---
KnapsackGenerator()
PrintKnapsack()
