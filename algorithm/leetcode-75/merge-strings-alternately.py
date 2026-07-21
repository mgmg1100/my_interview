"""
Merge Strings Alternately (LeetCode 1768)
Pattern: two pointers / interleaving
"""

from __future__ import annotations


def mergeAlternately(word1: str, word2: str) -> str:
    # TODO: implement
    pass


def run_tests() -> None:
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"

    # edge cases
    assert mergeAlternately("a", "b") == "ab"
    assert mergeAlternately("x", "yz") == "xyz"
    assert mergeAlternately("abc", "d") == "adbc"

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
