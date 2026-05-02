# Assignment Five



## Question A




$$
A = \{a, b, d, e, g, h\}, \quad
B = \{b, c, d, e, f, g\}, \quad
C = \{a, c, d, f, g, h\}
$$

### Pair A & B

$$
\textbf{Intersection: }
[A \cap B = \{b, d, e, g\}, \quad |A \cap B| = 4]\\
\\
\textbf{Union: }
[A \cup B = \{a, b, c, d, e, f, g, h\}, \quad |A \cup B| = 8]\\
\\
\textbf{Calculation: }
[1 - \frac{|A \cap B|}{|A \cup B|} = 1 - \frac{4}{8} = 1 - 0.5 = \mathbf{\color{blue}0.5}]
$$

### Pair A & C

$$
\textbf{Intersection: }
[A \cap C = \{a, d, g, h\}, \quad |A \cap C| = 4]\\
\\
\textbf{Union: }
[A \cup C = \{a, b, c, d, e, f, g, h\}, \quad |A \cup C| = 8]\\
\\
\textbf{Calculation: }
[1 - \frac{|A \cap C|}{|A \cup C|} = 1 - \frac{4}{8} = 1 - 0.5 = \mathbf{\color{blue}0.5}]
$$

### Pair B & C

$$
\textbf{Intersection: }
[B \cap C = \{c, d, f, g\}, \quad |B \cap C| = 4]\\
\\
\textbf{Union: }
[B \cup C = \{a, b, c, d, e, f, g, h\}, \quad |B \cup C| = 8]\\
\\
\textbf{Calculation: }
[1 - \frac{|B \cap C|}{|B \cup C|} = 1 - \frac{4}{8} = 1 - 0.5 = \mathbf{\color{blue}0.5}]
$$

| User Pair | Intersection Size | Union Size | Jaccard Distance |
| --------- | ----------------- | ---------- | ---------------- |
| (A, B)    | 4                 | 8          | 0.5              |
| (A, C)    | 4                 | 8          | 0.5              |
| (B, C)    | 4                 | 8          | 0.5              |

## Question B

### Vector Representation

$$
\mathbf{A} = [1, 1, 0, 1, 1, 0, 1, 1]
\\
\mathbf{B} = [0, 1, 1, 1, 1, 1, 1, 0]
\\
\mathbf{C} = [1, 0, 1, 1, 0, 1, 1, 1]
$$


$$
\|\mathbf{A}\| = \sqrt{1+1+0+1+1+0+1+1} = \sqrt{6}\\
\|\mathbf{B}\| = \sqrt{0+1+1+1+1+1+1+0} = \sqrt{6}\\
\|\mathbf{C}\| = \sqrt{1+0+1+1+0+1+1+1} = \sqrt{6}
$$

### Pair A & B

$$
Dot(\mathbf{A} \cdot \mathbf{B}): (1\cdot0) + (1\cdot1) + (0\cdot1) + (1\cdot1) + (1\cdot1) + (0\cdot1) + (1\cdot1) + (1\cdot0) = 4\\
Similarity: 4 / (\sqrt{6} \cdot \sqrt{6}) = 4 / 6 \approx 0.667\\
Distance: 1 - 0.667 = \mathbf{\color{blue}0.333}
$$

### Pair A & C

$$
Dot(\mathbf{A} \cdot \mathbf{C}):$(1\cdot1) + (1\cdot0) + (0\cdot1) + (1\cdot1) + (1\cdot0) + (0\cdot1) + (1\cdot1) + (1\cdot1) = 4\\
Similarity: 4 / (\sqrt{6} \cdot \sqrt{6}) = 4 / 6 \approx 0.667\\
Distance: 1 - 0.667 = \mathbf{\color{blue}0.333}
$$

### Pair B & C

$$
Dot(\mathbf{B} \cdot \mathbf{C}): (0\cdot1) + (1\cdot0) + (1\cdot1) + (1\cdot1) + (1\cdot0) + (1\cdot1) + (1\cdot1) + (0\cdot1) = 4\\
Similarity: 4 / (\sqrt{6} \cdot \sqrt{6}) = 4 / 6 \approx 0.667\\
Distance: 1 - 0.667 = \mathbf{\color{blue}0.333}
$$

| User Pair | Dot Product | Magnitude Product | Cosine Distance |
| --------- | ----------- | ----------------- | --------------- |
| (A, B)    | 4           | 6                 | 0.333           |
| (A, C)    | 4           | 6                 | 0.333           |
| (B, C)    | 4           | 6                 | 0.333           |

## Question C

$$
User A: \{a, b, d, g\}\\
User B: \{b, c, d\}\\
User C: \{d, f, g, h\}
$$

### Pair A & B

$$
Intersection (A \cap B): \{b, d\}\\
Union (A \cup B): \{a, b, c, d, g\}\\
Calculation: 1 - (2 / 5) = 1 - 0.4 = \mathbf{\color{blue}0.6}
$$

### Pair A & C

$$
Intersection (A \cap C): \{d, g\}\\
Union (A \cup C): \{a, b, d, f, g, h\}\\
Calculation: 1 - (2 / 6) \approx 1 - 0.333 = \mathbf{\color{blue}0.667}
$$

### Pair B & C

$$
Intersection (B \cap C): \{d\}\\
Union (B \cup C): \{b, c, d, f, g, h\}\\
Calculation: 1 - (1 / 6) \approx 1 - 0.167 = \mathbf{\color{blue}0.833}
$$

| User Pair | Intersection Size | Union Size | Jaccard Distance |
| --------- | ----------------- | ---------- | ---------------- |
| (A, B)    | 2                 | 5          | 0.600            |
| (A, C)    | 2                 | 6          | 0.667            |
| (B, C)    | 1                 | 6          | 0.833            |

## Question D

$$
Vector A: [1, 1, 0, 1, 0, 0, 1, 0]\\
Vector B: [0, 1, 1, 1, 0, 0, 0, 0]\\
Vector C: [0, 0, 0, 1, 0, 1, 1, 1]
$$

### Pair A & B

$$
Dot  (\mathbf{A} \cdot \mathbf{B}): (1\cdot0) + (1\cdot1) + (0\cdot1) + (1\cdot1) + (0\cdot0) + (0\cdot0) + (1\cdot0) + (0\cdot0) = 2\\
Similarity: 2 / (2 \cdot 1.732) \approx 0.577\\
Distance: 1 - 0.577 = \mathbf{\color{blue}0.423}
$$

### Pair A & C

$$
Dot(\mathbf{A} \cdot \mathbf{C}): (1\cdot0) + (1\cdot0) + (0\cdot0) + (1\cdot1) + (0\cdot0) + (0\cdot1) + (1\cdot1) + (0\cdot1) = 2\\
Similarity: 2 / (2 \cdot 2) = 0.5\\
Distance: 1 - 0.5 = \mathbf{\color{blue}0.500}
$$

### Pair B & C

$$
Dot(\mathbf{B} \cdot \mathbf{C}): (0\cdot0) + (1\cdot0) + (1\cdot0) + (1\cdot1) + (0\cdot0) + (0\cdot1) + (0\cdot1) + (0\cdot1) = 1\\
Similarity: 1 / (1.732 \cdot 2) \approx 0.289\\
Distance: 1 - 0.289 = \mathbf{\color{blue}0.711}
$$

| User Pair | Dot Product | Magnitude Product | Cosine Distance |
| --------- | ----------- | ----------------- | --------------- |
| (A, B)    | 2           | 3.464             | 0.423           |
| (A, C)    | 2           | 4.000             | 0.500           |
| (B, C)    | 1           | 3.464             | 0.711           |

## Question E

### Calculating Average

$$
A: (4+5+5+1+3+2) / 6 = 20 / 6 \approx \mathbf{\color{blue}3.333}\\
B: (3+4+3+1+2+1) / 6 = 14 / 6 \approx \mathbf{\color{blue}2.333}\\
C: (2+1+3+4+5+3) / 6 = 18 / 6 = \mathbf{\color{blue}3.000}
$$

### Subtracting Averages

| User | a           | b           | c           | d           | e           | f           | g           | h           |
| ---- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| A    | $4 - 3.333$ | $5 - 3.333$ |             | $5 - 3.333$ | $1 - 3.333$ |             | $3 - 3.333$ | $2 - 3.333$ |
| B    |             | $3 - 2.333$ | $4 - 2.333$ | $3 - 2.333$ | $1 - 2.333$ | $2 - 2.333$ | $1 - 2.333$ |             |
| C    | $2 - 3.0$   |             | $1 - 3.0$   | $3 - 3.0$   |             | $4 - 3.0$   | $5 - 3.0$   | $3 - 3.0$   |



### Results

| User | a        | b       | c        | d       | e        | f        | g        | h        |
| ---- | -------- | ------- | -------- | ------- | -------- | -------- | -------- | -------- |
| A    | $0.667$  | $1.667$ |          | $1.667$ | $-2.333$ |          | $-0.333$ | $-1.333$ |
| B    |          | $0.667$ | $1.667$  | $0.667$ | $-1.333$ | $-0.333$ | $-1.333$ |          |
| C    | $-1.000$ |         | $-2.000$ | $0.000$ |          | $1.000$  | $2.000$  | $0.000$  |

## Question F

### Vector Magnitudes

$$
Vector A: \sqrt{0.667^2 + 1.667^2 + 1.667^2 + (-2.333)^2 + (-0.333)^2 + (-1.333)^2} = \sqrt{13.333} \approx \mathbf{\color{blue}3.651}\\
Vector B: \sqrt{0.667^2 + 1.667^2 + 0.667^2 + (-1.333)^2 + (-0.333)^2 + (-1.333)^2} = \sqrt{7.333} \approx \mathbf{\color{blue}2.708}\\
Vector C: \sqrt{(-1.0)^2 + (-2.0)^2 + (0.0)^2 + (1.0)^2 + (2.0)^2 + (0.0)^2} = \sqrt{10} \approx \mathbf{\color{blue}3.162}
$$

### Dot Products

$$
V_A \cdot V_B: (1.667 \cdot 0.667) + (1.667 \cdot 0.667) + (-2.333 \cdot -1.333) + (-0.333 \cdot -1.333) = \mathbf{\color{blue}5.778}\\
V_A \cdot V_C: (0.667 \cdot -1.0) + (-0.333 \cdot 2.0) = \mathbf{\color{blue}-1.333}\\
V_B \cdot V_C: (1.667 \cdot -2.0) + (-0.333 \cdot 1.0) + (-1.333 \cdot 2.0) = \mathbf{\color{blue}-6.333}
$$

### Distance

#### Pair A & B

$$
Similarity: 5.778 / (3.651 \cdot 2.708) \approx\color{blue}0.584\\
Distance: 1 - 0.584 = \mathbf{\color{blue}0.416}
$$

#### Pair A & C

$$
Similarity: -1.333 / (3.651 \cdot 3.162) \approx \color{blue}-0.115\\
Distance: 1 - (-0.115) = \mathbf{\color{blue}1.115}
$$

#### Pair B & C

$$
Similarity: -6.333 / (2.708 \cdot 3.162) \approx \color{blue}-0.740\\
Distance: 1 - (-0.740) = \mathbf{\color{blue}1.740}
$$

| User Pair | Dot Product | Magnitude Product | Cosine Distance |
| --------- | ----------- | ----------------- | --------------- |
| (A, B)    | 5.778       | 9.887             | 0.416           |
| (A, C)    | -1.333      | 11.545            | 1.115           |
| (B, C)    | -6.333      | 8.563             | 1.740           |

## Question G

The first methods were to simple. They only looked at if a person rated an item or if a rating was high. This treats everyone the same and hides the details. When math only uses zeros and ones, it loses the nuance of how much someone likes or dislikes something. Every user pair ended up with the same distance in the first parts because the math was not deep enough.

The normalized approach is the best choice. It fixes the problem of personal bias by subtracting the average score of a user from their ratings. This show if a score is actually good or bad for that specific person. Some people rate everything high and some rate everything low. Centering the numbers at zero makes the data fair. It proves that users A and B are similar, while B and C have opposite tastes.