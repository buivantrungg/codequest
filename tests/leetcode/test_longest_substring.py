from solutions.leetcode.longest_substring import length_of_longest_substring

def test_longest_substring_example1():
    assert length_of_longest_substring("abcabcbb") == 3

def test_longest_substring_example2():
    assert length_of_longest_substring("bbbbb") == 1

def test_longest_substring_example3():
    assert length_of_longest_substring("pwwkew") == 3

def test_longest_substring_example4():
    assert length_of_longest_substring(" ") == 1

def test_longest_substring_example5():
    assert length_of_longest_substring("tmmzuxt") == 5