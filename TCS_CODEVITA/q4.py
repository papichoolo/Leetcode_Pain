def find_items(n, tokens, claim, k, item_costs):
    max_tokens = 0
    selected_days = []

    for i in range(n - k + 1):
        if claim[i:i+k].count(0) == k:
            total_tokens = sum(tokens[i:i+k])
            if total_tokens > max_tokens:
                max_tokens = total_tokens
                selected_days = list(range(i, i+k))

    selected_items = []
    for day in selected_days:
        selected_items.append((item, cost) for item, cost in item_costs.items() if claim[day] == 0 and total_tokens >= cost)

    selected_items.sort(key=lambda x: x[1])
    return [item for item, cost in selected_items]

# Input
n = int(input())
tokens = list(map(int, input().split()))
claim = list(map(int, input().split()))
k = int(input())
item_costs_raw = input().split(':')
item_costs = dict(zip(item_costs_raw[::2], map(int, item_costs_raw[1::2])))

# Find and print the items Mithra can buy
result = find_items(n, tokens, claim, k, item_costs)
print(" ".join(result))
