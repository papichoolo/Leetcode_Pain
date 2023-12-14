def perform_operations(array_size, query_count, queries):
    # Initialize the array with zeros
    array = [0] * int(array_size)

    # Perform each operation
    for query in queries:
        start_index, end_index, value_to_add = map(int, query.split())
        for i in range(start_index - 1, min(end_index, int(array_size))):
            array[i] += value_to_add

    # Find and return the maximum value in the array
    max_value = max(array)
    return max_value

# Example usage:
array_size = input()
query_count= input()
queries= input().split(',')

result = perform_operations(array_size, query_count, queries)
print(result)