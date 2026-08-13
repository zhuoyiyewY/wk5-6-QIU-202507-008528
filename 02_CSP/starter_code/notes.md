# NOTES

## Heuristic

I used the simple first-unassigned-variable strategy instead of an advanced heuristic such as MRV. This approach follows the assignment requirements and always selects the next unassigned variable in a fixed order. It does not affect the correctness of the backtracking search.

## Test Cases

The test cases cover different branches of the test case design mind-map. They include a normal solvable case, a valid constraint checking case, a conflicting assignment case, and an unsolvable case with only one colour available. Together these tests verify that the solver finds valid solutions, detects conflicts correctly, and reports failure when no solution exists.