def find_max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


size1 = int(input())
arr1 = list(map(int, input().split()))

size2 = int(input())
arr2 = list(map(int, input().split()))

# Merge the two arrays
merged_array = sorted(arr1 + arr2)

# Calculate and display the maximum profit
max_profit = find_max_profit(merged_array)
print(max_profit)
