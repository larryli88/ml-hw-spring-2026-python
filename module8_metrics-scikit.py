import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    print("--- Precision and Recall Calculator ---")
    
    while True:
        try:
            n = int(input("Enter the number of points (N): "))
            if n > 0:
                break
            print("N must be a positive integer. Try again.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    y_true = np.zeros(n, dtype=int)
    y_pred = np.zeros(n, dtype=int)

    print("\nPlease enter the points one by one.")
    for i in range(n):
        print(f"\n--- Point {i + 1} ---")
        
        while True:
            try:
                x = int(input("Enter ground truth class label x (0 or 1): "))
                if x in [0, 1]:
                    break
                print("Error: The ground truth label must be either 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")
                
        while True:
            try:
                y = int(input("Enter predicted class label y (0 or 1): "))
                if y in [0, 1]:
                    break
                print("Error: The predicted label must be either 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

        y_true[i] = x
        y_pred[i] = y

    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    print("\n===============================")
    print("           RESULTS             ")
    print("===============================")
    print(f"Ground Truths (X): {y_true}")
    print(f"Predictions   (Y): {y_pred}")
    print("-------------------------------")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print("===============================")

if __name__ == "__main__":
    main()
