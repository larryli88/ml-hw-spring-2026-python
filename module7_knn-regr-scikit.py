import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def main():
    print("--- k-NN Regression Tool ---")

    try:
        n_samples = int(input("Enter the number of points (N): "))
        k_neighbors = int(input("Enter the number of neighbors (k): "))

        if n_samples <= 0 or k_neighbors <= 0:
            print("Error: N and k must be positive integers.")
            return
    except ValueError:
        print("Error: Invalid input types.")
        return

    pts = np.zeros((n_samples, 2))

    print(f"\nEnter {n_samples} points:")
    for i in range(n_samples):
        print(f"Point {i+1}:")
        try:
            px = float(input("  Enter x: "))
            py = float(input("  Enter y: "))
            pts[i] = [px, py]
        except ValueError:
            print("Error: Inputs must be real numbers.")
            return

    x_train = pts[:, 0].reshape(-1, 1)
    y_train = pts[:, 1]

    y_var = np.var(y_train)
    print(f"\nVariance of training labels: {y_var:.4f}")

    try:
        target_x = float(input("\nEnter X value to predict: "))
    except ValueError:
        print("Error: Input must be a real number.")
        return

    if k_neighbors > n_samples:
        print(
            f"Error: k ({k_neighbors}) cannot exceed total points ({n_samples})."
        )
    else:
        model = KNeighborsRegressor(n_neighbors=k_neighbors)
        model.fit(x_train, y_train)

        pred_y = model.predict(np.array([[target_x]]))
        print(f"Predicted Y value: {pred_y[0]:.4f}")


if __name__ == "__main__":
    main()
