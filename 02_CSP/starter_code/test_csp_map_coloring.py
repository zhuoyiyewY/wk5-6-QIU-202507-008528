"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories rather than 3 variations of the same thing
(e.g. one typical/solvable case, one edge/boundary case, one
unsolvable/over-constrained case).

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint. Already implemented -- reuse this in your tests.
    """
    if solution is None:
        return False
    if set(solution.keys()) != set(variables):
        return False
    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False
    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small solvable case (from the mind-map:
# "Solvability -> solvable case").
# ---------------------------------------------------------------------
def test_given_example():
    # backtracking_search() in this starter file is wired to the fixed
    # Australia map problem (VARIABLES / NEIGHBOURS / DOMAIN, all module
    # level in csp_map_coloring.py), so this test solves that real problem.
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 1
# Category: Constraint checking (valid assignment)
# Checks that a non-conflicting assignment is considered consistent.
# ---------------------------------------------------------------------
def test_case_1():
    assignment = {
        "WA": "Red"
    }

    assert is_consistent(assignment, "NT", "Green")


# ---------------------------------------------------------------------
# Test Case 2
# Category: Constraint checking (conflicting assignment)
# Checks that neighbouring regions cannot have the same colour.
# ---------------------------------------------------------------------
def test_case_2():
    assignment = {
        "WA": "Red"
    }

    assert not is_consistent(assignment, "NT", "Red")


# ---------------------------------------------------------------------
# TODO Test Case 3
# Category: Unsolvable / over-constrained case
# Only one colour is available, so no valid solution should exist.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES

    solution = backtracking_search(VARIABLES, ["Red"])

    assert solution is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
