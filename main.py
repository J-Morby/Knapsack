events = []

def main():
    pass


class Calener:
    def __init__(self):
        pass
        

class Event:
    def __init__(self, name, length, value, denominations):
        self.name = name
        self.length = length
        self.value = value
        self.denomination = denominations
    
    def __repr__(self):
        return (f"Item(name={self.name}, length={self.length}, "
                f"value={self.value}, denominations={self.denomination})")
    

def EventGanerator():
    count = int(input("How many objects? "))
    for i in range(count):
        name = input("enter name? ")
        length = float(input("enter length? "))
        value = float(input("enter value? "))
        denomination = float(input("enter denominations? "))
        
        events.append(Event(name, length, value, denomination))


def PrintEvents():
    print("\nGenerated Items:")
    for item in events:
        print(item)


class Knapsack:
    def __init__(self,size):
        self.size = size

    


# --- Run app ---
EventGanerator()
PrintEvents()