"""
Evaluation utilities for Credit Card Fraud Detection
----------------------------------------------------

This module focuses on metrics suitable for
imbalanced classification problems.
"""

import numpy as np
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model using standard metrics.

    Parameters
    ----------
    model : sklearn estimator
        Trained model
    X_test : array-like
        Test features
    y_test : array-like
        True labels

    Returns
    -------
    dict
        Evaluation results
    """
    y_pred = model.predict(X_test)

    results = {
        "classification_report": classification_report(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred)
    }

    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test)[:, 1]
        results["roc_auc"] = roc_auc_score(y_test, y_proba)

    return results


def print_evaluation(results: dict):
    """
    Pretty-print evaluation results.
    """
    print("Classification Report:")
    print(results["classification_report"])
    print("\nConfusion Matrix:")
    print(results["confusion_matrix"])

    if "roc_auc" in results:
        print(f"\nROC-AUC Score: {results['roc_auc']:.4f}")


def compute_business_cost(
    y_true,
    y_pred,
    cost_fp: float = 1.0,
    cost_fn: float = 5.0
):
    """
    Compute simple business cost based on prediction errors.

    Parameters
    ----------
    cost_fp : float
        Cost of false positive
    cost_fn : float
        Cost of false negative

    Returns
    -------
    float
        Total cost
    """
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()

    total_cost = (fp * cost_fp) + (fn * cost_fn)
    return total_cost
