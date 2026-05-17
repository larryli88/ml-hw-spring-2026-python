import numpy as np


class KNNRegression:

    def __init__(self, k):
        self.k = k
        self.points = None

    def fit(self, points_list):
        self.points = np.array(points_list, dtype=float)

    def predict(self, x_query):
        if self.points is None or len(self.points) == 0:
            raise ValueError("Error: No data points available to predict.")

        X_train = self.points[:, 0]
        Y_train = self.points[:, 1]

        distances = np.abs(X_train - x_query)
        k_indices = np.argpartition(distances, self.k)[: self.k]

        return np.mean(Y_train[k_indices])


def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Error: Please enter a positive integer greater than 0.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid real number.")


def main():
    print("--- k-NN Regression Program ---")

    N = get_positive_int("Enter the number of points (N): ")
    k = get_positive_int("Enter the number of neighbors (k): ")

    if k > N:
        print(
            f"\nError: k ({k}) cannot be greater than the number of points N ({N})."
        )
        print("k-NN Regression cannot be performed.")
        return

    points_list = []
    print(f"\nPlease enter the {N} points:")
    for i in range(1, N + 1):
        print(f"Point {i}:")
        x = get_float(f"  Enter x value: ")
        y = get_float(f"  Enter y value: ")
        points_list.append([x, y])

    knn_model = KNNRegression(k=k)
    knn_model.fit(points_list)

    print("\n--- Prediction ---")
    x_query = get_float("Enter the X value to predict Y for: ")

    y_pred = knn_model.predict(x_query)
    print(f"\nThe predicted Y value for X = {x_query} is: {y_pred}")


if __name__ == "__main__":
    main()
