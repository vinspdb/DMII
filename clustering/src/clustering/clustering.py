from sklearn.cluster import KMeans


def run_kmeans(
    X,
    n_clusters: int = 5,
    random_state: int = 42,
):
    """Fit K-Means and return the model and cluster labels."""

    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10,
    )

    labels = model.fit_predict(X)

    return model, labels