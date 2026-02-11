def singleNumber(nums: list[int]) -> int:
    seen = set()
    for n in nums:
        if n in seen:
            seen.remove(n)
        else:
            seen.add(n)
    return seen.pop()