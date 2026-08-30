import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron

SEED = 300

def create_dataset():
    X, y = make_classification(
        n_samples=30,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        weights=[0.5, 0.5],
        random_state=SEED
    )
    return X, y

def show_raw_data(X, y):
    plt.figure()
    for label in np.unique(y):
        points = X[y == label]
        plt.scatter(
            points[:, 0],
            points[:, 1],
            label=f"Class {label}",
            s=50
        )
    plt.title("Generated Dataset")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()

def draw_decision_boundary(X, y, model, step=0.02):
    x_min = X[:, 0].min() - 1
    x_max = X[:, 0].max() + 1
    y_min = X[:, 1].min() - 1
    y_max = X[:, 1].max() + 1
    x_grid, y_grid = np.meshgrid(
        np.arange(x_min, x_max, step),
        np.arange(y_min, y_max, step)
    )
    grid_points = np.column_stack(
        (x_grid.ravel(), y_grid.ravel())
    )
    predictions = model.predict(grid_points)
    predictions = predictions.reshape(x_grid.shape)
    colors = ["lightcoral", "lightblue"]
    cmap = ListedColormap(colors)
    plt.contourf(
        x_grid,
        y_grid,
        predictions,
        alpha=0.35,
        cmap=cmap
    )
    markers = ["o", "s"]
    for label in np.unique(y):
        points = X[y == label]
        plt.scatter(
            points[:, 0],
            points[:, 1],
            marker=markers[label],
            edgecolors="black",
            label=f"Class {label}"
        )

def train_perceptron(X, y):
    model = Perceptron(
        max_iter=100,
        eta0=0.002,
        fit_intercept=True,
        random_state=SEED
    )
    model.fit(X, y)
    return model

def main():
    X, y = create_dataset()
    show_raw_data(X, y)
    model = train_perceptron(X, y)
    accuracy = model.score(X, y)
    print(f"Training accuracy: {accuracy:.2%}")
    plt.figure()
    draw_decision_boundary(X, y, model)
    plt.title("Perceptron Decision Boundary")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()