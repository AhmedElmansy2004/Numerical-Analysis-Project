class Vector:

    def __init__ (self, numOfElements=0):
        self.elements = numOfElements
        self.values = [0] * numOfElements
    
    def input(self):
        for i in range(self.elements):
            self.values[i] = (float(input(f"Enter element [{i+1}]: \n")))

    def output(self):
        for i in range(self.elements):
            element = self.values[i]
            display = int(element) if element.is_integer() else element
            print(f"{display:>8}", end="")
            print("\n")

    def clear(self):
        self.elements = 0
        self.values = [0] * self.elements
