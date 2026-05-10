class DataManager:
    def __init__(self):
        self.numbers = []

    def insert_number(self, value):
        """Adds a number to the internal list."""
        self.numbers.append(value)

    def search_value(self, x):
        """
        Returns the 1-based index of x if found, 
        otherwise returns -1.
        """
        try:
            # list.index returns the 0-based index of the first occurrence
            return self.numbers.index(x) + 1
        except ValueError:
            return -1
