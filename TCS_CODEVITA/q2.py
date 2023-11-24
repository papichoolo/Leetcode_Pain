def calculate_distance(good_string, student_name):
    total_distance = 0
    previous_good_letter = good_string[0]

    for current_letter in student_name:
        if current_letter in good_string:
            # If the current letter is present in the good string, no change needed
            continue

        distances = []

        for good_letter in good_string:
            distance = abs(ord(previous_good_letter) - ord(good_letter)) + abs(ord(current_letter) - ord(good_letter))
            distances.append((distance, good_letter))

        distances.sort()  # Sort by distance and then by lexicographical order

        selected_letter = distances[0][1]
        total_distance += distances[0][0]

        previous_good_letter = selected_letter

    return total_distance

# Example usage:
good_string = "@HR*i{kcQl"
student_name = "Vyom"

result = calculate_distance(good_string, student_name)
print(result)
