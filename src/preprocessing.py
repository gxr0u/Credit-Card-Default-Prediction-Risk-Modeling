"""
Preprocessing utilities for Credit Card Fraud Detection
-------------------------------------------------------

This module handles:
- Train-test splitting
- Feature scaling
- Class imbalance handling using SMOTE

All transformations are designed to avoid data leakage.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str
        Path to the CSV file

    Returns
    -------
    pd.DataFrame
        Loaded dataset
    """
    return pd.read_csv(path)


def split_features_target(df: pd.DataFrame, target_col: str = "Class"):
    """
    Split dataframe into features and target.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Name of target column

    Returns
    -------
    X : pd.DataFrame
        Feature matrix
    y : pd.Series
        Target vector
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y


def train_test_split_stratified(X, y, test_size=0.2, random_state=42):
    """
    Perform stratified train-test split.

    Returns
    -------
    X_train, X_test, y_train, y_test
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )


def scale_features(X_train, X_test):
    """
    Standardize features using training data statistics.

    Returns
    -------
    X_train_scaled, X_test_scaled, scaler
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def apply_smote(X_train, y_train, random_state=42):
    """
    Apply SMOTE on training data only.

    Returns
    -------
    X_resampled, y_resampled
    """
    smote = SMOTE(random_state=random_state)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
    return X_resampled, y_resampled
