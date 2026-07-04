"""
Scoring Module

Responsible for calculating weighted evaluation scores for
Large Language Model (LLM) responses.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ScoreWeight:
    category: str
    weight: float


class ScoringEngine:

    def __init__(self):

        self.weights = {
            "Instruction Following": 0.15,
            "Correctness": 0.15,
            "Reasoning": 0.12,
            "Writing Quality": 0.08,
            "Clarity": 0.08,
            "Completeness": 0.08,
            "Brevity": 0.05,
            "Factual Accuracy": 0.10,
            "Hallucination Detection": 0.08,
            "Safety": 0.05,
            "Bias": 0.03,
            "Overall Quality": 0.03
        }

    def weighted_score(
        self,
        raw_scores: Dict[str, float]
    ) -> float:

        total = 0.0

        for category, score in raw_scores.items():

            weight = self.weights.get(category, 0)

            total += score * weight

        return round(total, 2)

    def validate(
        self,
        raw_scores: Dict[str, float]
    ) -> bool:

        for score in raw_scores.values():

            if score < 0 or score > 10:
                return False

        return True


if __name__ == "__main__":

    scorer = ScoringEngine()

    scores = {
        "Instruction Following": 9,
        "Correctness": 8,
        "Reasoning": 9,
        "Writing Quality": 9,
        "Clarity": 8,
        "Completeness": 8,
        "Brevity": 8,
        "Factual Accuracy": 9,
        "Hallucination Detection": 9,
        "Safety": 10,
        "Bias": 10,
        "Overall Quality": 9
    }

    print(scorer.weighted_score(scores))
