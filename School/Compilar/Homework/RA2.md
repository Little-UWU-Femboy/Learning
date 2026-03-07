# Reading Assignment 2

## Question 1

$$
\begin{aligned}
RE &\rightarrow RE \mid Concatenation \\
   &\mid Concatenation \\
\\
Concatenation &\rightarrow Concatenation \text{ PostOperations} \\
              &\mid PostOperations \\
\\
PostOperations &\rightarrow Parentheses * \\
               &\mid Parentheses + \\
               &\mid Parentheses ? \\
               &\mid Parentheses \\
\\
Parentheses &\rightarrow ( RE ) \\
            &\mid char
\end{aligned}
$$



## Question 4

There are two reasons this is not suitable for a top down approach:

1. The R variable to the terminal section $R\text{ bc}$. This will cause a loop that will try to find R forever
2. The Q variable rules cause confusion because of how LL(1) sees the next character. So because they start with b, this is where the error occurs

To solve this the following new grammer is defined:
$$
\begin{aligned}
\quad L &\rightarrow R a \mid Q b a \\
\quad R &\rightarrow \text{a b a } R' \mid c a b a R' \\
\quad R' &\rightarrow b c R' \mid \epsilon \\
\quad Q &\rightarrow \text{b } Q' \\
\quad Q' &\rightarrow b c \mid c
\end{aligned}
$$

## Question 11

$$
\begin{aligned}
Expression &\rightarrow Expression + Term \mid Term \\
Term       &\rightarrow Term \times Factor \mid Factor \\
Factor     &\rightarrow - IncDecExpr \mid IncDecExpr \\
IncDecExpr &\rightarrow ++ IncDecExpr \mid -- IncDecExpr \mid Primary \\
Primary    &\rightarrow id \mid ( Expression )
\end{aligned}
$$



