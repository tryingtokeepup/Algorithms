#!/usr/bin/python
def find_max_profit(prices):
    min_price = int(prices[0])
    best_profit = 0
    prices = iter(prices)
    for price in prices:
        if price < min_price:
            min_price = price
        elif (price - min_price) > best_profit:
            best_profit = price - min_price

    return print(best_profit)


# this is true for the rise, how about the dip?

    # if __name__ == '__main__':
    #     # This is just some code to accept inputs from the command line
    #     parser = argparse.ArgumentParser(
    #         description='Find max profit from prices.')
    #     parser.add_argument('integers', metavar='N', type=int,
    #                         nargs='+', help='an integer price')
    #     args = parser.parse_args()

    #     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
    #         profit=find_max_profit(args.integers), prices=args.integers))

# work on james's version and reformat it to be like my cooler soltuion
# def find_max_profit(prices):
#     min_loss = 0
#     loss = 0
#     max_profit = 0
#     increase = 0
#     starting_point = prices[0]

#     for i, price in enumerate(prices):
#         if i < (len(prices) - 1) and price > prices[i+1]:  # drop
#             starting_point = prices[i+1]
#             loss = prices[i+1] - price
#             if min_loss == 0:
#                 min_loss = loss
#             elif min_loss < loss:
#                 min_loss = loss
#         if i < (len(prices) - 1) and price < prices[i+1]:  # rise
#             increase = prices[i+1] - starting_point
#             if increase > max_profit:
#                 max_profit = increase

#     if max_profit == 0:
#         return min_loss
#     return max_profit


def get_max_profit(array):

    # for the rise
    global_max = 0
    # global_min = 0
    if len(array) < 2:
        print("hey, please put in at least 2 values into the array!")
        return global_max

	    i = 0

	    while i < len(array)-1:
	        curr_price = array[i]
	        max_potential_price = max(array[i+1:])
	        # we need to slice the array
	        if max_potential_price - curr_price > global_max:
	            global_max = max_potential_price - curr_price
	        i += 1
	    return global_max

	print(get_max_profit([1050, 270, 343, 100, 2]))
find_max_profit([1050, 270, 1540, 3800, 2])
find_max_profit([10, 7, 5, 8, 11, 9])
find_max_profit([100, 90, 80, 50, 20, 10])

# incredible solution from Laryna
# def find_max_profit(prices):
#   pass
#   low = prices[0]
#   profit = prices[1] - low

#   for price in prices[1:]:
#     profit = max(price - low, profit)
#     low = min(price, low)

#   return profit


# print(find_max_profit([1050, 270, 1540, 3800, 2])) 
