import pandas as pd
from sklearn.preprocessing import StandardScaler


FEATURES = [
    "HP",
    "Attack",
    "Defense",
    "Sp. Atk",
    "Sp. Def",
    "Speed",
]


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """Select the numerical features used for clustering."""
    return df[FEATURES].copy()


def scale_features(
    X: pd.DataFrame,
) -> tuple[pd.DataFrame, StandardScaler]:
    """Standardize the input features."""
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_scaled = pd.DataFrame(
        X_scaled,
        columns=X.columns,
        index=X.index,
    )

    return X_scaled, scaler