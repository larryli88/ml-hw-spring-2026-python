class DataManager:
    def __init__(self):
        self.numbers = []

    def insert_number(self, value):
        self.numbers.append(value)

    def search_value(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1

def main():
    manager = DataManager()

    # Data Initialization & Insertion
    try:
        n_str = input("Enter N: ")
        n = int(n_str)
        
        for _ in range(n):
            num = int(input("Enter a number: "))
            manager.insert_number(num)

        # Data Search
        x = int(input("Enter X: "))
        print(manager.search_value(x))
        
    except ValueError:
        print("Please ensure all inputs are integers.")

if __name__ == "__main__":
    main()
