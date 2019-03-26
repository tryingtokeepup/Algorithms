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
    # if __name__ == '__main__':
    #     # This is just some code to accept inputs from the command line
    #     parser = argparse.ArgumentParser(
    #         description='Find max profit from prices.')
    #     parser.add_argument('integers', metavar='N', type=int,
    #                         nargs='+', help='an integer price')
    #     args = parser.parse_args()

    #     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
    #         profit=find_max_profit(args.integers), prices=args.integers))


# def find_max_profit(prices):
#     # I want to iterate through all the prices, so I will use iter
#     prices = iter(prices)

#     best_profit = 0
#     next_price = prices[1:2]
#     for price in prices:
#         if price > next_price:
#             profit = next_price - price
#             next_price = next(prices)
#             if profit > best_profit:
#                 best_profit = profit

#     print(best_profit)


find_max_profit([1050, 270, 1540, 3800, 2])
