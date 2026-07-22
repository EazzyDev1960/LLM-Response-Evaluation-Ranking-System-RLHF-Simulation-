"""
Project Demonstration

Shows how the evaluation pipeline works.
"""

from src.evaluator import (
    EvaluationEngine,
    EvaluationDimension
)

from src.analytics import AnalyticsEngine


def main():

    engine = EvaluationEngine()

    analytics = AnalyticsEngine()

    scores = [

        EvaluationDimension(
            name="Instruction Following",
            score=9.5,
            comment="Excellent",
            weight=0.15
        ),

        EvaluationDimension(
            name="Correctness",
            score=9.2,
            comment="Accurate",
            weight=0.15
        ),

        EvaluationDimension(
            name="Reasoning",
            score=9.1,
            comment="Logical",
            weight=0.12
        ),

        EvaluationDimension(
            name="Writing Quality",
            score=9.0,
            comment="Professional",
            weight=0.08
        ),

        EvaluationDimension(
            name="Clarity",
            score=9.3,
            comment="Very clear",
            weight=0.08
        )

    ]

    result = engine.evaluate(

        prompt="Explain reinforcement learning.",

        response="Sample AI response.",

        evaluator="Human Reviewer",

        scores=scores

    )

    analytics.add_score(result.overall_score)

    print("=" * 60)

    print("LLM RESPONSE EVALUATION DEMO")

    print("=" * 60)

    print(engine.generate_summary(result))

    print()

    print("Analytics")

    print(analytics.export())


if __name__ == "__main__":

    main()
