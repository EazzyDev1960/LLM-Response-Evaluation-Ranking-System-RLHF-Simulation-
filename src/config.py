"""
Global configuration for the LLM Evaluation Framework.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationConfig:
    MAX_SCORE: float = 10.0
    MIN_SCORE: float = 0.0
    PASSING_SCORE: float = 7.5
    CONFIDENCE_THRESHOLD: float = 0.85
    REPORT_DECIMALS: int = 2
    VERSION: str = "2.0.0"
    PROJECT_NAME: str = "LLM Response Evaluation & Ranking System"


config = EvaluationConfig()
