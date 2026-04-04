# Question 1

### Part A

#### Prior Probabilities

- $P(+)=3/8$
- $P(−)=5/8$

#### Conditional Probabilities for the '+' Class

- $P(A=1∣+)=2/3$
- $P(A=0∣+)=1/3$
- $P(B=1∣+)=1/3$
- $P(B=0∣+)=2/3$
- $P(C=1∣+)=1/3$
- $P(C=0∣+)=2/3$

#### Conditional Probabilities for the '-' Class

- $P(A=1∣−)=2/5$
- $P(A=0∣−)=3/5$
- $P(B=1∣−)=3/5$
- $P(B=0∣−)=2/5$
- $P(C=1∣−)=3/5$
- $P(C=0∣−)=2/5$

### Part B

#### Calculation for class '+'

$$
Score(+)=P(+)×P(A=1∣+)×P(B=0∣+)×P(C=0∣+)\\
Score(+)=(3/8)×(2/3)×(2/3)×(2/3)=24/216≈0.1111 \\
$$

So result is approx **0.1111**

#### Calculation for class '-'

$$
Score(−)=P(−)×P(A=1∣−)×P(B=0∣−)×P(C=0∣−)\\
Score(−)=(5/8)×(2/5)×(2/5)×(2/5)=40/1000=0.0400\\
$$

Since $0.1111 > 0.0400$, the Naïve Bayes approach predicts the **+** class.



# Question 2

Python code is in separate file to run, but code is also here to be copied if needed

```python
import numpy as np
from sklearn.svm import SVC

# 1. Define training data
RawTrainingData = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]

RawTrainingLabels = ["+", "-", "-", "-", "+", "-", "-", "+"]

TrainingData = np.array(RawTrainingData)
TrainingLabels = np.array(RawTrainingLabels)

TransformedTrainingData = np.array([[x * 1 for x in Sample] for Sample in TrainingData])

SvmModel = SVC(kernel="linear", C=1.0, random_state=42)

SvmModel.fit(TransformedTrainingData, TrainingLabels)

RawTestSample = [0, 1, 0]

TransformedTestSample = np.array([[x * 1 for x in RawTestSample]])

PredictedLabel = None
for Sample in TransformedTestSample:
    PredictedLabel = SvmModel.predict([Sample])[0]

print(f"Prediction for sample: {PredictedLabel}")

```

# Question 3

1. For X1=0,X2=0 (Output 1): $W1(0)+W2(0)+b>0$ --> $b>0$ *Let b=1.*
2. For X1=0,X2=1 (Output 0): $W1(0)+W2(1)+1≤0$ --> $W2≤−1$ *Let W2=−1.5.*
3. For X1=1,X2=0 (Output 0): $W1(1)+W2(0)+1≤0$--> $W1≤−1$ *Let W1=−1.5.*
4. For X1=1,X2=1 (Output 0): $(−1.5)(1)+(−1.5)(1)+1=−2≤0$ *(This inequality holds true).*

A valid set of values that satisfies the conditions is **W1=−1.5**, **W2=−1.5**, and **b=1**.