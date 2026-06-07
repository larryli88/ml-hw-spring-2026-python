import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def load_user_dataset(label_name):
    while True:
        try:
            num_samples = int(input(f"Enter the number of samples for {label_name} set (positive integer): "))
            if num_samples > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    features = np.zeros((num_samples, 1), dtype=float)
    labels = np.zeros(num_samples, dtype=int)

    print(f"Please provide {num_samples} (x, y) pairs:")
    for idx in range(num_samples):
        print(f" Pair {idx + 1}:")
        while True:
            try:
                x_input = float(input(f"   Enter x (real number): "))
                break
            except ValueError:
                print("   Invalid input. x must be a real number.")
        
        while True:
            try:
                y_input = int(input(f"   Enter y (non-negative integer): "))
                if y_input >= 0:
                    break
                print("   y must be non-negative.")
            except ValueError:
                print("   Invalid input. y must be an integer.")
        
        features[idx, 0] = x_input
        labels[idx] = y_input

    return features, labels

def main():
    print("--- Training Set Initialization ---")
    train_features, train_labels = load_user_dataset("Training")

    print("\n--- Test Set Initialization ---")
    test_features, test_labels = load_user_dataset("Test")

    upper_limit_k = min(10, len(train_features))
    k_options = list(range(1, upper_limit_k + 1))

    knn_model = KNeighborsClassifier()

    optimal_k = None
    highest_score = -1.0

    print("\n--- Tuning Hyperparameters ---")
    for k_val in k_options:
        classifier = KNeighborsClassifier(n_neighbors=k_val)
        classifier.fit(train_features, train_labels)
        
        preds = classifier.predict(test_features)
        current_acc = accuracy_score(test_labels, preds)
        
        if current_acc > highest_score:
            highest_score = current_acc
            optimal_k = k_val

    print("\n--- Results ---")
    if optimal_k is not None:
        print(f"The best k for the kNN Classification method is: {optimal_k}")
        print(f"The corresponding test accuracy is: {highest_score:.4f} (or {highest_score * 100:.2f}%)")
    else:
        print("Could not determine the best k.")

if __name__ == "__main__":
    main()
