def longest_common_prefix(strs: list[str]) -> str:
    """
    Returns the longest common prefix among a list of strings.
    If no common prefix exists, returns an empty string.
    """
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))     # ""
    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # "inters"
