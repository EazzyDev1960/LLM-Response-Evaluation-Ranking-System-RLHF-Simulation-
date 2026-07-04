"""
Custom exceptions.
"""


class EvaluationError(Exception):
    """Base evaluation exception."""


class InvalidScoreError(EvaluationError):
    """Raised when score is outside valid range."""


class RankingError(EvaluationError):
    """Raised during ranking failures."""


class DatasetError(EvaluationError):
    """Raised when dataset loading fails."""
