"""CSC 161 Project Milestone 3

In this milestone, we make our own algorithim that buys or sells
stocks for us.

My algorithim will be as follows:

1)Compare the value of that current day's 'open' and 'close'. If
the difference between the two is positive (the close is lower
than the open) that means the stock price went down that day.
If the difference is negative the stock price went up that day.

2)Each day we calculate this difference.

3)I implemented a counter to see how many days in a row the stock went
up or down. If the stock goes up each day for 9 days in a row, we will
sell as we think this is a peak. If the price went down each day for 3
days in a row we will buy, as we think this is a minor drop.

I initially wrote the program where we'd buy or sell if either happened
3 days in a row, but as I tweaked the day numbers, I found that selling
after 9 in a row and buying after 3 in a row is most lucrative. My
algorithim makes more money for the AAPL stock, but for the MSFT stock
it makes less money.

Please note that all of my PEP8 errors are because lines are too long.
This is because of commenting, please disregard.

Jacob Hertz
Lab Section TR 12:30-1:45
Spring 2018
"""


def extract_info(filename):
    name = open(filename, 'r')  # open the file for read mode
    lines = name.read()  # read the file
    list_form = lines.split("\n")  # splits at the newline character
    return list_form


def _format(data, col, day):
    length = len(data)
    correct_order = data[length-day-1]  # reverses list, get in chronological order
    lines_2 = correct_order.split(",")  # split the data by commas
    columns = ["date", "open", "high", "low", "close", "volume", "adj_close"]
    y = 0  # index variable since our loop runs through the column and not a range
    for i in columns:
        if (col == i):  # nested for loops!
            price = lines_2[y]
        y += 1
    return price


def get_value(_extracted, col, day):

    formatted = _format(_extracted, col, day)  # calling my funcations
    float_rep = float(formatted)  # getting the float rep. of the info
    return float_rep





def main():

    money = 1000  # book keeping, how much money our user owns
    stocks = 0  # book keeping, hold owned stocks
    filename = input("Enter a filename for stock data (CSV format): ")
    print("\n***Moving Average Results***")
    print("\nYou started with {0} stocks and ${1:.2f}".format(stocks, money))
    # Call your moving average algorithm, with the filename to open.
    stocks, money = alg_moving_average(filename)  # calling the moving average function
    # Print results of the moving average algorithm, returned above:
    print("You now own {0} stocks and have ${1:.2f}".format(stocks, money))
    money = 1000  # book keeping, how much money our user owns
    stocks = 0  # book keeping, hold owned stocks
    print("\n***My Algorithim Results***")
    print("\nYou started with {0} stocks and ${1:.2f}".format(stocks, money))
    # Call your moving average algorithm, with the filename to open.
    stocks, money = alg_mine(filename)  # calling my function
    # Print results of the moving average algorithm, returned above:
    print("You now own {0} stocks and have ${1:.2f}".format(stocks, money))

if __name__ == '__main__':
    main()
