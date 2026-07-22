"""
Basic tests for the Evaluation Engine.
"""

from src.evaluator import (
    EvaluationEngine,
    EvaluationDimension
)


def test_engine_initialization():

    engine = EvaluationEngine()

    assert engine is not None


def test_average_score():

    engine = EvaluationEngine()

    scores = [

        EvaluationDimension(
            name="Instruction Following",
            score=10,
            comment="",
            weight=1
        ),

        EvaluationDimension(
            name="Correctness",
            score=8,
            comment="",
            weight=1
        )

    ]

    average = engine.calculate_average(scores)

    assert average == 9.0


def test_weighted_score():

    engine = EvaluationEngine()

    scores = [

        EvaluationDimension(
            name="Instruction Following",
            score=9,
            comment="",
            weight=0.6
        ),

        EvaluationDimension(
            name="Correctness",
            score=8,
            comment="",
            weight=0.4
        )

    ]

    weighted = engine.calculate_weighted_score(scores)

    assert weighted > 0
