# Evaluation Framework

This framework is inspired by RLHF (Reinforcement Learning from Human Feedback) principles used in AI model training.

## Step 1: Instruction Analysis
Check whether the response fully satisfies all parts of the prompt.


## Step 2: Scoring Dimensions (1–5 scale)

### 1. Instruction Following
- 5 = Fully follows instruction
- 3 = Partially follows instruction
- 1 = Fails to follow instruction

### 2. Correctness
- 5 = Fully correct and accurate
- 3 = Partially correct
- 1 = Incorrect or misleading

### 3. Reasoning Quality
- 5 = Clear logical structure
- 3 = Some reasoning gaps
- 1 = Illogical or unclear

### 4. Writing Quality
- 5 = Clear, professional, structured
- 3 = Understandable but imperfect
- 1 = Poor clarity

### 5. Brevity vs Detail
- 5 = Balanced and appropriate
- 3 = Slightly too long/short
- 1 = Poorly balanced

### 6. Tone & Style
- 5 = Perfect tone match
- 3 = Acceptable
- 1 = Incorrect tone


## Step 3: Pairwise Comparison
Compare Response A vs Response B and select a winner based on total score.


## Step 4: Justification
Provide short reasoning for final decision.
