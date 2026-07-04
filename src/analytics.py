"""
Analytics Engine

Provides statistical analysis for LLM evaluation results.
"""

from dataclasses import dataclass
from statistics import mean, median
from typing import List, Dict


@dataclass
class AnalyticsResult:
    total_evaluations: int
    average_score: float
    median_score: float
    highest_score: float
    lowest_score: float
    pass_rate: float


class AnalyticsEngine:

    PASSING_SCORE = 7.5

    def __init__(self):

        self.history: List[float] = []

    def add_score(self, score: float) -> None:

        self.history.append(score)

    def reset(self) -> None:

        self.history.clear()

    def calculate(self) -> AnalyticsResult:

        if not self.history:

            return AnalyticsResult(
                total_evaluations=0,
                average_score=0.0,
                median_score=0.0,
                highest_score=0.0,
                lowest_score=0.0,
                pass_rate=0.0
            )

        passed = len(
            [
                score
                for score in self.history
                if score >= self.PASSING_SCORE
            ]
        )

        return AnalyticsResult(

            total_evaluations=len(self.history),

            average_score=round(
                mean(self.history),
                2
            ),

            median_score=round(
                median(self.history),
                2
            ),

            highest_score=max(self.history),

            lowest_score=min(self.history),

            pass_rate=round(
                (passed / len(self.history)) * 100,
                2
            )

        )

    def export(self) -> Dict:

        result = self.calculate()

        return {

            "total_evaluations":
                result.total_evaluations,

            "average_score":
                result.average_score,

            "median_score":
                result.median_score,

            "highest_score":
                result.highest_score,

            "lowest_score":
                result.lowest_score,

            "pass_rate":
                result.pass_rate

        }


if __name__ == "__main__":

    analytics = AnalyticsEngine()

    scores = [

        9.2,
        8.5,
        7.9,
        8.8,
        9.4,
        6.9,
        7.7,
        8.1,
        9.0

    ]

    for score in scores:

        analytics.add_score(score)

    print(analytics.export())
