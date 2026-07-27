# Logical Inference Using Backward Chaining

This project demonstrates a basic logical inference system in Python.

The program stores family relationships as facts and uses logical rules to determine whether statements are true.

## Facts

- John is the parent of Mary.
- Mary is the parent of Bob.
- Bob is the parent of Alice.
- John is male.
- Mary is female.

## Rules

- If X is the parent of Y and Y is the parent of Z, then X is the grandparent of Z.
- If X is the parent of Y and X is male, then X is the father of Y.
- If X is the parent of Y and X is female, then X is the mother of Y.

## Run the Program

```bash
python3 backward_chaining.py
