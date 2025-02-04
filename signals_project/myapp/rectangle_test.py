class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
        self._attributes = [("length", self.length), ("width", self.width)]
    
    def __iter__(self):
        """Make the Rectangle object iterable."""
        for attr, value in self._attributes:
            yield {attr: value}

# Example Usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)  # Create an object of Rectangle

    # Print the attributes one by one using iteration
    for item in rect:
        print(item)
