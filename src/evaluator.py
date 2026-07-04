"""
LLM Response Evaluation & Ranking System
========================================

Enterprise Evaluation Engine

Author:
Ikenna Henry Ezeokeke

Description
-----------
Professional evaluation engine for assessing Large Language Model (LLM)
responses using structured human evaluation methodologies inspired by
RLHF, AI Training, and Quality Assurance workflows.

This module provides:

• Modular evaluation pipeline
• Structured score validation
• Confidence estimation
• Weighted scoring
• Professional logging
• Error handling
• Human-readable summaries
• JSON-ready data structures

Version:
2.0.0
"""

from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================
# LOGGER CONFIGURATION
# ============================================================

LOGGER = logging.getLogger("evaluation_engine")

if not LOGGER.handlers:

    LOGGER.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console = logging.StreamHandler()

    console.setFormatter(formatter)

    LOGGER.addHandler(console)


# ============================================================
# CONSTANTS
# ============================================================

MAX_SCORE = 10.0
MIN_SCORE = 0.0

DEFAULT_DIMENSIONS = [

    "Instruction Following",

    "Correctness",

    "Reasoning",

    "Writing Quality",

    "Clarity",

    "Completeness",

    "Brevity",

    "Factual Accuracy",

    "Hallucination Detection",

    "Safety",

    "Bias",

    "Overall Quality"

]


# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================

class EvaluationError(Exception):
    """Base evaluation exception."""


class InvalidScoreError(EvaluationError):
    """Raised when score is outside accepted range."""


class InvalidDimensionError(EvaluationError):
    """Raised when an unknown evaluation dimension is used."""


# ============================================================
# DATA MODELS
# ============================================================

@dataclass
class EvaluationDimension:

    name: str

    score: float

    comment: str

    weight: float = 1.0

    def validate(self) -> None:

        if self.score < MIN_SCORE:

            raise InvalidScoreError(
                f"{self.name}: score below minimum."
            )

        if self.score > MAX_SCORE:

            raise InvalidScoreError(
                f"{self.name}: score exceeds maximum."
            )


@dataclass
class EvaluationMetadata:

    evaluation_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    evaluator: str = "Human Evaluator"

    framework_version: str = "2.0.0"


@dataclass
class EvaluationResult:

    prompt: str

    response: str

    metadata: EvaluationMetadata

    dimensions: List[EvaluationDimension]

    confidence: float = 0.0

    overall_score: float = 0.0


# ============================================================
# MAIN ENGINE
# ============================================================

class EvaluationEngine:

    """
    Enterprise evaluation engine.

    Responsibilities
    ----------------

    • Validate evaluation input

    • Coordinate dimension scoring

    • Produce standardized outputs

    • Calculate overall quality

    • Generate evaluation summaries
    """

    def __init__(

        self,

        dimensions: Optional[List[str]] = None

    ):

        self.dimensions = (
            dimensions
            if dimensions
            else DEFAULT_DIMENSIONS
        )

        LOGGER.info(
            "Evaluation Engine initialized."
        )

    def validate_dimension(

        self,

        dimension: str

    ) -> None:

        if dimension not in self.dimensions:

            raise InvalidDimensionError(

                f"Unknown evaluation dimension: {dimension}"

            )

    def validate_scores(

        self,

        scores: List[EvaluationDimension]

    ) -> None:

        for item in scores:

            self.validate_dimension(item.name)

            item.validate()

    def calculate_average(

        self,

        scores: List[EvaluationDimension]

    ) -> float:

        if not scores:

            return 0.0

        total = sum(

            item.score

            for item in scores

        )

        return round(

            total / len(scores),

            2

        )
    def calculate_weighted_score(
        self,
        scores: List[EvaluationDimension]
    ) -> float:
        """
        Calculates the weighted evaluation score.
        """

        if not scores:
            return 0.0

        weighted_sum = 0.0
        total_weight = 0.0

        for item in scores:

            weighted_sum += item.score * item.weight
            total_weight += item.weight

        if total_weight == 0:
            return 0.0

        return round(weighted_sum / total_weight, 2)

    def calculate_confidence(
        self,
        scores: List[EvaluationDimension]
    ) -> float:
        """
        Confidence is estimated from score consistency.
        """

        if not scores:
            return 0.0

        values = [item.score for item in scores]

        average = sum(values) / len(values)

        variance = sum(
            (value - average) ** 2
            for value in values
        ) / len(values)

        confidence = max(
            0.0,
            min(
                1.0,
                1 - (variance / 25)
            )
        )

        return round(confidence, 3)

    def evaluate(
        self,
        prompt: str,
        response: str,
        evaluator: str,
        scores: List[EvaluationDimension]
    ) -> EvaluationResult:
        """
        Performs a complete evaluation.
        """

        LOGGER.info(
            "Starting evaluation..."
        )

        self.validate_scores(scores)

        metadata = EvaluationMetadata(
            evaluator=evaluator
        )

        overall = self.calculate_weighted_score(
            scores
        )

        confidence = self.calculate_confidence(
            scores
        )

        result = EvaluationResult(
            prompt=prompt,
            response=response,
            metadata=metadata,
            dimensions=scores,
            confidence=confidence,
            overall_score=overall
        )

        LOGGER.info(
            "Evaluation completed successfully."
        )

        return result

    def generate_summary(
        self,
        result: EvaluationResult
    ) -> Dict:
        """
        Returns a concise evaluation summary.
        """

        return {

            "evaluation_id":
                result.metadata.evaluation_id,

            "timestamp":
                result.metadata.timestamp,

            "evaluator":
                result.metadata.evaluator,

            "overall_score":
                result.overall_score,

            "confidence":
                result.confidence,

            "dimensions":
                len(result.dimensions)

        }

    def grade(
        self,
        score: float
    ) -> str:
        """
        Converts a numeric score into a quality grade.
        """

        if score >= 9.5:
            return "Outstanding"

        if score >= 8.5:
            return "Excellent"

        if score >= 7.5:
            return "Good"

        if score >= 6.5:
            return "Fair"

        if score >= 5:
            return "Needs Improvement"

        return "Poor"

    def print_report(
        self,
        result: EvaluationResult
    ) -> None:

        print("=" * 60)

        print("LLM RESPONSE EVALUATION REPORT")

        print("=" * 60)

        print(f"Evaluator : {result.metadata.evaluator}")

        print(f"Overall   : {result.overall_score}")

        print(f"Confidence: {result.confidence}")

        print(
            f"Grade      : {self.grade(result.overall_score)}"
        )

        print("-" * 60)

        for dimension in result.dimensions:

            print(
                f"{dimension.name:30}"
                f"{dimension.score:5}"
            )

        print("=" * 60)
    def compare_responses(
        self,
        first: EvaluationResult,
        second: EvaluationResult
    ) -> EvaluationResult:
        """
        Compare two evaluation results and return the better one.
        """

        LOGGER.info("Comparing evaluation results.")

        if first.overall_score > second.overall_score:
            return first

        if second.overall_score > first.overall_score:
            return second

        if first.confidence >= second.confidence:
            return first

        return second

    def rank_responses(
        self,
        responses: List[EvaluationResult]
    ) -> List[EvaluationResult]:
        """
        Rank responses from highest to lowest score.
        """

        LOGGER.info("Ranking responses.")

        return sorted(
            responses,
            key=lambda item: (
                item.overall_score,
                item.confidence
            ),
            reverse=True
        )

    def evaluation_statistics(
        self,
        responses: List[EvaluationResult]
    ) -> Dict:
        """
        Generate overall evaluation statistics.
        """

        if not responses:

            return {
                "evaluations": 0,
                "average_score": 0.0,
                "highest_score": 0.0,
                "lowest_score": 0.0
            }

        scores = [
            item.overall_score
            for item in responses
        ]

        return {

            "evaluations": len(scores),

            "average_score": round(
                sum(scores) / len(scores),
                2
            ),

            "highest_score": max(scores),

            "lowest_score": min(scores)

        }

    def export_json(
        self,
        result: EvaluationResult
    ) -> Dict:
        """
        Convert an evaluation result into a JSON-ready dictionary.
        """

        return {

            "metadata": {

                "evaluation_id":
                    result.metadata.evaluation_id,

                "timestamp":
                    result.metadata.timestamp,

                "evaluator":
                    result.metadata.evaluator,

                "framework_version":
                    result.metadata.framework_version

            },

            "prompt": result.prompt,

            "response": result.response,

            "overall_score":
                result.overall_score,

            "confidence":
                result.confidence,

            "dimensions": [

                {

                    "name": d.name,

                    "score": d.score,

                    "weight": d.weight,

                    "comment": d.comment

                }

                for d in result.dimensions

            ]

        }

    def health_check(self) -> bool:
        """
        Verify that the evaluation engine is operational.
        """

        LOGGER.info("Health check completed.")

        return True
# ============================================================
# DEMONSTRATION
# ============================================================

def build_sample_scores() -> List[EvaluationDimension]:
    """
    Creates sample evaluation scores for demonstration purposes.
    """

    return [

        EvaluationDimension(
            name="Instruction Following",
            score=9.5,
            weight=0.15,
            comment="Fully satisfies the prompt."
        ),

        EvaluationDimension(
            name="Correctness",
            score=9.0,
            weight=0.15,
            comment="Factually accurate."
        ),

        EvaluationDimension(
            name="Reasoning",
            score=9.2,
            weight=0.12,
            comment="Logical and coherent."
        ),

        EvaluationDimension(
            name="Writing Quality",
            score=9.3,
            weight=0.08,
            comment="Professional writing."
        ),

        EvaluationDimension(
            name="Clarity",
            score=9.1,
            weight=0.08,
            comment="Easy to understand."
        ),

        EvaluationDimension(
            name="Completeness",
            score=8.9,
            weight=0.08,
            comment="Addresses all requirements."
        ),

        EvaluationDimension(
            name="Brevity",
            score=8.5,
            weight=0.05,
            comment="Concise without losing meaning."
        ),

        EvaluationDimension(
            name="Factual Accuracy",
            score=9.4,
            weight=0.10,
            comment="No factual issues detected."
        ),

        EvaluationDimension(
            name="Hallucination Detection",
            score=9.8,
            weight=0.08,
            comment="No hallucinations observed."
        ),

        EvaluationDimension(
            name="Safety",
            score=10.0,
            weight=0.05,
            comment="Safe response."
        ),

        EvaluationDimension(
            name="Bias",
            score=9.8,
            weight=0.03,
            comment="Neutral language."
        ),

        EvaluationDimension(
            name="Overall Quality",
            score=9.4,
            weight=0.03,
            comment="High-quality answer."
        )

    ]


if __name__ == "__main__":

    engine = EvaluationEngine()

    sample_scores = build_sample_scores()

    result = engine.evaluate(

        prompt="Explain reinforcement learning.",

        response=(
            "Reinforcement learning is a machine learning "
            "approach where an agent learns by interacting "
            "with an environment and receiving rewards."
        ),

        evaluator="AI Quality Reviewer",

        scores=sample_scores

    )

    engine.print_report(result)

    summary = engine.generate_summary(result)

    print("\nSUMMARY")

    print(summary)

    exported = engine.export_json(result)

    print("\nJSON EXPORT READY")

    print(exported)

    LOGGER.info(
        "Enterprise evaluation engine demonstration completed."
    )
        
