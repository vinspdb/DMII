import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def reduce_with_pca(X, n_components: int = 2):
    """Reduce the feature space using PCA."""
    pca = PCA(n_components=n_components)

    X_pca = pca.fit_transform(X)

    return X_pca, pca


def plot_clusters(X_pca, labels):
    """Plot the clusters in a 2D PCA space."""
    fig, ax = plt.subplots(figsize=(8, 6))

    scatter = ax.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=labels,
        alpha=0.7,
    )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("Pokémon clusters")

    ax.legend(
        *scatter.legend_elements(),
        title="Cluster",
    )

    return fig, ax