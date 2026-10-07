from sklearn.metrics import silhouette_score


def calculate_inertia(model) -> float:
    """Return the K-Means inertia."""
    return model.inertia_


def calculate_silhouette(X, labels) -> float:
    """Calculate the silhouette score."""
    return silhouette_score(X, labels)


def evaluate_clustering(model, X, labels) -> dict[str, float]:
    """Calculate the main clustering evaluation metrics."""
    return {
        "inertia": calculate_inertia(model),
        "silhouette": calculate_silhouette(X, labels),
    }