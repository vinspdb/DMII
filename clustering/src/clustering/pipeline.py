from pathlib import Path

from clustering.data import load_data
from clustering.preprocessing import (
    select_features,
    scale_features,
)
from clustering.clustering import run_kmeans
from clustering.evaluation import evaluate_clustering
from clustering.visualization import (
    reduce_with_pca,
    plot_clusters,
)
import matplotlib.pyplot as plt



PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "pokemon.csv"


def run_pipeline(n_clusters: int = 5):
    """Run the complete Pokémon K-Means pipeline."""

    # 1. Load data
    df = load_data(DATA_PATH)

    # 2. Select features
    X = select_features(df)

    # 3. Scale features
    X_scaled, scaler = scale_features(X)

    # 4. Run K-Means
    model, labels = run_kmeans(
        X_scaled,
        n_clusters=n_clusters,
    )

    # 5. Add cluster labels
    result = df.copy()
    result["cluster"] = labels

    # 6. Evaluate clustering
    metrics = evaluate_clustering(
        model,
        X_scaled,
        labels,
    )

    # 7. PCA
    X_pca, pca = reduce_with_pca(X_scaled)

    return {
        "data": result,
        "model": model,
        "scaler": scaler,
        "metrics": metrics,
        "pca": pca,
        "X_pca": X_pca,
    }


if __name__ == "__main__":
    output = run_pipeline(n_clusters=5)

    print("\nEvaluation:")
    print(f"Inertia: {output['metrics']['inertia']:.2f}")
    print(f"Silhouette: {output['metrics']['silhouette']:.3f}")

    print("\nClusters:")
    print(output["data"][["Name", "cluster"]].head(20))

    plot_clusters(
        output["X_pca"],
        output["data"]["cluster"],
    )

    plt.show()