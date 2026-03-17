# question set one

### Part One

#### Step One

This calculates the Gini index of both classes C0 and C1 for males.
$$
Gini(M) = 1 - \left(\frac{6}{10}\right)^2 - \left(\frac{4}{10}\right)^2
$$

$$
Gini(M) = 1 - 0.36 - 0.16 = 0.48
$$

The result here is **0.48**.

#### Step Two

This calculates the Gini index of both classes C0 and C1 for females.
$$
Gini(F) = 1 - \left(\frac{4}{10}\right)^2 - \left(\frac{6}{10}\right)^2
$$

$$
Gini(F) = 1 - 0.16 - 0.36 = 0.48
$$

The result here is **0.48**.

#### Step Three

This calculates the weighted Gini index for the genders.
$$
Gini_{Gender} = \left(\frac{10}{20}\right) \times Gini(M) + \left(\frac{10}{20}\right) \times Gini(F)\\
\text{Where } Gini(F) = 0.48 \text{ and } Gini(M) =0.48
$$

$$
Gini_{Gender} = 0.5 \times 0.48 + 0.5 \times 0.48
$$

$$
Gini_{Gender} = 0.24 + 0.24 = 0.48
$$

So the final answer is **0.48**.

### Part Two

#### Step One

Calculates the Gini index for sport section
$$
Gini(Sports) = 1 - \left(\frac{8}{8}\right)^2 - \left(\frac{0}{8}\right)^2
$$

$$
Gini(Sports) = 1 - 1 - 0 = 0
$$

The result here is **0**

#### Step Two

Calculates the Gini index for family section.
$$
Gini(Family) = 1 - \left(\frac{1}{4}\right)^2 - \left(\frac{3}{4}\right)^2
$$

$$
Gini(Family) = 1 - 0.0625 - 0.5625 = 0.375
$$

The result here is **0.375**.

#### Step Three

Calculates the Gini index for luxury section.
$$
Gini(Luxury) = 1 - \left(\frac{1}{8}\right)^2 - \left(\frac{7}{8}\right)^2
$$

$$
Gini(Luxury) = 1 - 0.015625 - 0.765625 = 0.21875
$$

The result here is **0.21875**.

#### Step Four

Calculates the Gini index for the car split.
$$
Gini_{CarType} = \left(\frac{4}{20}\right) \times 0.375 + \left(\frac{8}{20}\right) \times 0 + \left(\frac{8}{20}\right) \times 0.21875
$$

$$
Gini_{CarType} = 0.2 \times 0.375 + 0.4 \times 0 + 0.4 \times 0.21875
$$

$$
Gini_{CarType} = 0.075 + 0 + 0.0875 = 0.1625
$$

The result here is **0.1625**.

### Part Three

#### Step One

Calculates the Gini index for small section.
$$
Gini(Small) = 1 - \left(\frac{3}{5}\right)^2 - \left(\frac{2}{5}\right)^2
$$

$$
Gini(Small) = 1 - 0.36 - 0.16 = 0.48
$$



The result here is **0.48**.

#### Step Two

Calculates the Gini index for medium section.
$$
Gini(Medium) = 1 - \left(\frac{3}{7}\right)^2 - \left(\frac{4}{7}\right)^2
$$

$$
Gini(Medium) = 1 - 0.18367 - 0.32653 = 0.4898
$$



The result here is **0.4898**.

#### Step Three

Calculates the Gini index for large section.
$$
Gini(Large) = 1 - \left(\frac{2}{4}\right)^2 - \left(\frac{2}{4}\right)^2
$$

$$
Gini(Large) = 1 - 0.25 - 0.25 = 0.50
$$

The result here is **0.50**.

#### Step Four

Calculates the Gini index for extra large section.
$$
Gini(Extra Large) = 1 - \left(\frac{2}{4}\right)^2 - \left(\frac{2}{4}\right)^2
$$

$$
Gini(ExtraLarge) = 1 - 0.25 - 0.25 = 0.50
$$



The result here is **0.50**.

#### Step Five

Calculates the Gini index for the shirt sizes split.
$$
Gini_{ShirtSize} = \left(\frac{5}{20}\right)(0.48) + \left(\frac{7}{20}\right)(0.4898) + \left(\frac{4}{20}\right)(0.5) + \left(\frac{4}{20}\right)(0.5)
$$

$$
Gini_{ShirtSize} = 0.25(0.48) + 0.35(0.4898) + 0.2(0.5) + 0.2(0.5)
$$

$$
Gini_{ShirtSize} = 0.12 + 0.1714 + 0.1 + 0.1 = 0.4914
$$



The result here is **0.4914**.

### Part Four

Out of the calculated values, the **0.1625** value from the car type is the best since this is the lowest value. Therefore, the car type is the purest type. The worst here is the shirt size from **0.4914**.

# question set two

### Part One

For each of the ID values

1. The label is **positive**, but this predicts **negative**
2. The label is **positive**, but this predicts **negative**
3. The label is **positive** and this predicts **positive**
4. The label is **negative**, but this predicts **positive**
5. The label is **negative** and this predicts **negative**
6. The label is **negative**, but this predicts **positive**
7. The label is **negative** and this predicts **negative**
8. The label is **negative**, but this predicts  **positive**

### Part Two

$$
TP = 1\\
FP = 3\\
TN = 2\\
FN = 2\\
$$

### Part Three

#### Part One

$$
Accuracy = \frac{1 + 2}{1 + 3 + 2 + 2}
$$

$$
Accuracy = 3/8 = 0.375
$$

The result for accuracy is **0.375**.

#### Part Two

$$
Precision = \frac{1}{1 + 3}
$$

$$
Precision = \frac{1}{4} = 0.25
$$

The result for precision is **0.25**.

#### Part Three

$$
Recall = \frac{1}{1 + 2}
$$

$$
Recall = \frac{1}{3} \approx 0.3\overline{3}
$$

The result for Recall is about **$0.3\overline{3}$**.

#### Part Four

$$
F1 = 2 \times \frac{\frac{1}{4} \times \frac{1}{3}}{\frac{1}{4} + \frac{1}{3}}
$$

$$
F1 = 2 \times \frac{\frac{1}{12}}{\frac{3}{12} + \frac{4}{12}}
$$

$$
F1 = 2 \times \frac{\frac{1}{12}}{\frac{7}{12}}
$$

$$
F1 = 2 \times \frac{1}{7}
$$

$$
F1 = 2/7 \approx{0.2857}
$$

The result for the F1 is **0.2857**.

# question set three

### Part One

Here $k=1$. Because $k=1$, from each test case only the single closest data point needs to be found to determine the type this is.

-  The first case will be **setosa** since for all those test cases, the closet one of 0.2 which is example 0
- The second case will be **versicolor** since going through all the test cases 0.7 which is example 3
- The third case will be **virginica** since going through all the test cases 0.3 which is example 

### Part Two

Here $k=3$. Because $k=3$, from each test case only the three closet data point needs to be found to determine the type this is.

-  The first case will be **setosa**. The closest points are 0.2, 0.4, and 0.5 with each of these being setosa types.
-  The second case will be **versicolor**. The closest points are  0.7. 1.0, and 1.1. However, not all were the same type, but a majority were versicolor.
-  The third case will be **virginica**. The closest points are 0.3, 0.6, and 1.0. All three were of the same type. 