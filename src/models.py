"""
Model definitions for Credit Card Fraud Detection
-------------------------------------------------

This module provides factory functions for initializing
machine learning models used in the project.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def get_logistic_regression():
    """
    Initialize Logistic Regression model.
    """
    return LogisticRegression(max_iter=1000, random_state=42)


def get_decision_tree():
    """
    Initialize Decision Tree model.
    """
    return DecisionTreeClassifier(random_state=42)


def get_random_forest():
    """
    Initialize Random Forest model.
    """
    return RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )


def get_all_models():
    """
    Return a dictionary of all models.

    Returns
    -------
    dict
        Model name -> model instance
    """
    return {
        "Logistic Regression": get_logistic_regression(),
        "Decision Tree": get_decision_tree(),
        "Random Forest": get_random_forest()
    }
