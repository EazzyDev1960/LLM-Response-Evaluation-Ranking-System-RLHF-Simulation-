# Human Feedback Guidelines

## Purpose

Human feedback is a fundamental component of modern Large Language Model (LLM) development. High-quality annotations improve model alignment, reduce harmful outputs, and provide reliable signals for reinforcement learning from human feedback (RLHF).

This document defines the annotation standards used throughout this project.

---

# Objectives

The goals of human evaluation are to:

- Measure response quality consistently
- Reward helpful and accurate answers
- Penalize hallucinations and unsafe outputs
- Produce reliable preference data
- Improve model alignment with user intent

---

# Evaluation Principles

Every response should be judged using the following principles:

- Accuracy
- Helpfulness
- Clarity
- Completeness
- Safety
- Neutrality
- Instruction Following

---

# Rating Scale

| Score | Meaning |
|------:|---------|
| 10 | Exceptional |
| 9 | Excellent |
| 8 | Good |
| 7 | Acceptable |
| 6 | Needs Improvement |
| 5 or below | Poor |

---

# Annotation Workflow

```
Read Prompt
      │
      ▼
Read Response
      │
      ▼
Evaluate Dimensions
      │
      ▼
Assign Scores
      │
      ▼
Write Justification
      │
      ▼
Submit Evaluation
```

---

# Annotation Best Practices

- Read the entire response before scoring.
- Judge the response, not the topic.
- Be consistent across evaluations.
- Provide concise and objective comments.
- Base scores on evidence rather than personal preference.

---

# Common Annotation Errors

Avoid:

- Personal bias
- Inconsistent scoring
- Guessing missing information
- Rewarding verbosity instead of quality
- Ignoring factual inaccuracies

---

# Example Evaluation

Prompt:

```
Explain reinforcement learning.
```

Score Summary:

| Dimension | Score |
|-----------|------:|
| Accuracy | 9.5 |
| Clarity | 9.2 |
| Helpfulness | 9.0 |
| Safety | 10.0 |

Overall Rating:

```
9.4 / 10
```

Reviewer Comment:

> The response is accurate, well-structured, and addresses the prompt without introducing unsupported claims.

---

# Reviewer Responsibilities

Evaluators should:

- Remain objective
- Follow the scoring rubric
- Document significant issues
- Escalate uncertain cases
- Maintain consistency across evaluations

---

# Summary

Consistent human feedback improves evaluation quality and creates reliable datasets for AI training, benchmarking, and RLHF workflows.
