from collections import Counter

def sort_by_frequency(word):
    letter_counts = Counter(word)
    return ''.join(letter for letter, count in letter_counts.most_common() for _ in range(count))

# usage
print(sort_by_frequency("hello"))