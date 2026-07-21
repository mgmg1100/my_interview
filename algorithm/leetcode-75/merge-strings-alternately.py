"""
Merge Strings Alternately (LeetCode 1768)
Pattern: two pointers / interleaving

Problem:
You are given two strings, word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer
than the other, append the additional letters onto the end of the merged
string.

Return the merged string.

Examples:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Constraints:
1 <= len(word1), len(word2) <= 100
word1 and word2 consist of lowercase English letters.

Signature:
def mergeAlternately(word1: str, word2: str) -> str:
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
