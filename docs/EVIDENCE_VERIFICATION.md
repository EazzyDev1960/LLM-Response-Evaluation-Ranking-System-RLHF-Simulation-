# Evidence Verification

## Purpose

Evidence verification is a critical stage in evaluating Large Language Model (LLM) responses. Its objective is to determine whether the claims made by a model are supported by reliable evidence, internally consistent, and appropriately qualified when uncertainty exists.

This document defines the verification workflow used throughout this project.

---

# Objectives

The evidence verification process aims to:

- Detect unsupported factual claims
- Identify fabricated references and citations
- Evaluate source reliability
- Measure confidence in factual correctness
- Reduce hallucinations in generated responses

---

# Verification Workflow

```
User Prompt
      │
      ▼
LLM Response
      │
      ▼
Extract Factual Claims
      │
      ▼
Locate Supporting Evidence
      │
      ▼
Evaluate Source Reliability
      │
      ▼
Assign Confidence Score
      │
      ▼
Final Verification Decision
```

---

# Source Reliability Levels

| Level | Description | Reliability |
|-------|-------------|------------:|
| A | Peer-reviewed journals, official government publications | Very High |
| B | Official company documentation and recognized organizations | High |
| C | Established news organizations | Moderate |
| D | Personal blogs and opinion articles | Low |
| E | Anonymous or unverifiable sources | Very Low |

---

# Verification Criteria

Each factual claim should be assessed using the following questions:

- Is the claim supported by evidence?
- Is the evidence recent?
- Is the source authoritative?
- Can the information be independently verified?
- Does the evidence directly support the claim?

---

# Confidence Scoring

| Score | Interpretation |
|-------:|---------------|
| 0.90–1.00 | Very High Confidence |
| 0.75–0.89 | High Confidence |
| 0.50–0.74 | Moderate Confidence |
| 0.25–0.49 | Low Confidence |
| 0.00–0.24 | Very Low Confidence |

---

# Example

### Claim

```
Python was first released in 1991.
```

### Verification

Source:
Official Python documentation.

Assessment:

- Supported by authoritative documentation
- Consistent across multiple reliable references
- No conflicting evidence identified

Confidence Score:

```
0.99
```

Decision:

```
Verified
```

---

# Common Failure Cases

Evidence verification should identify:

- Fabricated statistics
- Fake citations
- Incorrect dates
- Misquoted research
- Unsupported numerical claims
- False attributions

---

# Limitations

Evidence verification cannot guarantee absolute correctness.

Potential limitations include:

- Outdated source material
- Conflicting authoritative references
- Rapidly changing information
- Domain-specific uncertainty

Human review remains essential for high-impact or safety-critical applications.

---

# Best Practices

- Prefer primary sources over secondary summaries.
- Cross-check important factual claims using multiple authoritative references.
- Clearly indicate uncertainty when evidence is incomplete.
- Avoid treating unsupported claims as established facts.
- Record verification decisions for transparency and reproducibility.

---

# Summary

Evidence verification improves the reliability of LLM evaluation by ensuring factual claims are supported by trustworthy sources. Combining structured verification with human oversight helps reduce hallucinations and increases confidence in evaluation outcomes.
