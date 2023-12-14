def process_queries(nums, queries):
    result = []

    for query in queries:
        k, trim_i = query

        trimmed_nums = [int(num[-trim_i:]) for num in nums]
        sorted_indices = sorted(range(len(trimmed_nums)), key=lambda x: trimmed_nums[x])

        result.append(sorted_indices.index(k - 1))

    return result

# Example usage:
nums = ["113", "933", "231", "719"]
queries = [(1, 1), (2, 2), (4, 2), (1, 3)]

output = process_queries(nums, queries)
print(*output)