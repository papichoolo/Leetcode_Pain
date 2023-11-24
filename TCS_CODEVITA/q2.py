def calculate_distance(good_string, name):
    prev_good_char = good_string[0]
    total_distance = 0

    for char in name:
        min_distance = float('inf')
        for good_char in good_string:
            distance = abs(ord(char) - ord(good_char))
            if distance < min_distance or (distance == min_distance and abs(ord(prev_good_char) - ord(good_char)) < abs(ord(prev_good_char) - ord(min_distance_char))):
                min_distance = distance
                min_distance_char = good_char
        total_distance += min_distance
        prev_good_char = min_distance_char

    return total_distance

# Input
good_string = input().strip()
name = input().strip()

# Calculate and print the total distance
print(calculate_distance(good_string, name))