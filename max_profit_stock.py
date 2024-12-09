def max_profit(price_list):
    min_value = price_list[0]
    profit = 0
    for element in range(1, len(price_list)):
        min_value = min(price_list[element],min_value)
        profit = max(profit, price_list[element] - min_value)

    return profit

price_list = [7, 10, 1, 3, 6, 9, 2]
print(max_profit(price_list))



def max_profit(price_list):
    min_value = price_list[0]
    profit = 0
    for i in range(1, len(price_list)):
        min_value = min(min_value, price_list[i])
        profit = max(profit, price_list[i] - min_value)
    return profit

price_list = [7, 10, 1, 3, 6, 9, 2]
print(max_profit(price_list))
































