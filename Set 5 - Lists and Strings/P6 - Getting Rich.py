stock_prices = [50,120,45,76,32,82,90,21,120,12]
#A list of stock prices
high,low,greatest_return,return_val = 0,0,0,0
#high = highest stock values
#low = lowest stock value
#greatest_return = greatest return (sell - purchase) from the stock prices
#return_val = temporary return to be compared
low_index, high_index = 0,0
first = True
for x in range(len(stock_prices)):
    if first:
        high = stock_prices[x]
        low = stock_prices[x]
        low_index = x
        high_index = x
        first = False
    else:
        if stock_prices[x] <= low:
            low = stock_prices[x]
            low_index = x
            high = 0
        elif stock_prices[x] >= high:
            high = stock_prices[x]
            high_index = x
            if high_index > low_index:
                return_val = high - low
                if return_val > greatest_return:
                    greatest_return = return_val
print(greatest_return)

