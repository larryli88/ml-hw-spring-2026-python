from module5_mod import DataManager

def main():
    manager = DataManager()

    # 1. Get N (the count of numbers)
    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # 2. Get N numbers one by one
    for i in range(n):
        try:
            val = int(input(f"Enter number {i + 1} of {n}: "))
            manager.insert_number(val)
        except ValueError:
            print("Invalid input, skipping this entry.")

    # 3. Get X (the search target)
    try:
        x = int(input("Enter the search value X: "))
        result = manager.search_value(x)
        print(result)
    except ValueError:
        print("Invalid input for X.")

if __name__ == "__main__":
    main()
