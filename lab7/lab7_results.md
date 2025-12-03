# Names: Zachary Kim, Andrew Flerchinger
# Lab: lab7 (RAG for Code with UniXcoder)
# Date: Today's date

## Reflections

### 2.2 "Comparing discrimination scores"

```
============================================================
Test 1: Similar Functions (both email validation)
============================================================
email_val_1 vs email_val_2
UniXcoder:      0.8549
Generic model:  0.8516
Difference:     +0.0033

============================================================
Test 2: Different Functions (email vs math)
============================================================
email_val_1 vs math_calc
UniXcoder:      0.0856
Generic model:  0.5131
Difference:     -0.4275

============================================================
Test 3: Very Different Functions (email vs string reversal)
============================================================
email_val_1 vs string_op
UniXcoder:      0.0858
Generic model:  0.4817
Difference:     -0.3959

============================================================
Analysis
============================================================
A good code embedding model should:
  - Give HIGH similarity for functionally similar code
  - Give LOW similarity for functionally different code

UniXcoder discrimination (similar - different): 0.7693
Generic discrimination (similar - different):   0.3385
```

    1. UniXcoder has a significantly higher discrimination score than the Generic model. This score reveals that the UniXcoder model is the much better code embedding model.

### 2.3

```
Base code:
def add_numbers(a, b):
    '''Add two numbers together.'''
    return a + b

============================================================
Similarity Scores:
============================================================
0.9538 - with_typing
0.9396 - renamed_vars
0.8935 - different_name
0.8359 - different_logic
0.1074 - completely_different
```

    1. Yes, UniXcoder largely recognizes functionally similar code despite the slight structural code differences. Completely different logic yields a very low similarity, which is as expected; the low score for completely different code suggests that the model is actually detecting similarity.

    2. Explicitly specifying types in the code is the most effective. However, excluding types still yields high results as the model recognizes the expected types in commonly used math operations.

### 2.4

```
Similarity to Original (sorted high to low):
======================================================================
Test Case            Similarity   Changes                       
----------------------------------------------------------------------
one_operator         0.9949       1 operator: < → >             
two_operators        0.9887       2 operators: < → >, flip returns
comment_only         0.9476       0 operators (added comment)   
three_operators      0.9298       3 operators: < → >=, 18 → 21, flip returns
cosmetic_only        0.9186       0 operators (cosmetic: age → user_age)
```

    1. Does UniXcoder recognize increasingly numerous changes?

        * Yes, though larger changes do seem to result in marginal decreases in similarity.

    2. How does it handle the "cosmetic" change? Does it think it's important, and if so, why?

        * Cosmetic only changes results in the largest decrease in similarity. This is an important discovery, as it reveals that the successful use of UniXcoder involves using code that is semantically similar to the questions askes, even if it is functionally identical; the "cosmetic" change, invovles a sematic change from age to user_age, causing the model to get slightly lost when looking into what the "user" is referring to, since the user refers to nothing in this case.

### 3.2 

    1. Do different phrasings of the same question retrieve the same functions?

        * Yes, all questions retrieve the same functions despite different wordings.
