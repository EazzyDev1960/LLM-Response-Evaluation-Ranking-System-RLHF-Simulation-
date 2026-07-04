"""
Data models used throughout the evaluation framework.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class EvaluationDimension:
    name: str
    score: float
    weight: float
    comment: str = ""


@dataclass
class EvaluationResult:
    prompt: str
    response: str
    evaluator: str
    dimensions: List[EvaluationDimension] = field(default_factory=list)

    @property
    def overall_score(self) -> float:

        if not self.dimensions:
            return 0.0

        total_weight = sum(d.weight for d in self.dimensions)

        if total_weight == 0:
            return 0.0

        weighted = sum(
            d.score * d.weight
            for d in self.dimensions
        )

        return round(weighted / total_weight, 2)

    def to_dict(self) -> Dict:

        return {
            "prompt": self.prompt,
            "response": self.response,
            "evaluator": self.evaluator,
            "overall_score": self.overall_score,
            "dimensions": [
                {
                    "name": d.name,
                    "score": d.score,
                    "weight": d.weight,
                    "comment": d.comment
                }
                for d in self.dimensions
            ]
        }
