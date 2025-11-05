def length_of_longest_substring(s: str) -> int:
    visited = {}
    start_idx = 0
    longest = 0
    count = 0
    for index, c in enumerate(s):
        if c not in visited:
            visited[c] = index
            count = count + 1
        else:
            longest = longest if longest > count else count
            if visited[c] >= start_idx:
                start_idx = visited[c] + 1
                count = index - start_idx + 1
            else:
                count = count + 1
            visited[c] = index
    return longest if longest > count else count


if __name__ == '__main__':
    s = "tmmzuxt"
    print(length_of_longest_substring(s))