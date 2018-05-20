"""CSC 161 Project Milestone 4

In this milestone, we implement OOD to complete our program.
I created a class called Portfolio that created objects which
are described by their name, how many stocks they own, and how
much money they have. I then created get and set functions for
each of these. I rewrote my moving_avg and my own algorithim
to use these objects. I had to change the parameters of both
to accept an object.

For statistics I compared how much money I made in each algorithim.
Then I used this difference to compare my percent increase between
algorithims. Given this information I determined why my algorithim
works better or worse than the moving average algorithim. My
algorithim should work better for APPL but worse for MSFT.

Please note: all of my PEP8 errors are from lines being
too long. This is because of comments, which are necessary
to explain to you my code. Please disregard.

Jacob Hertz
Lab Section TR 12:30-1:45
Spring 2018
"""

from tradinglib import *

class Portfolio:  # creating our class to be used for a person's portfolio

    def __init__(self, name, stocks=0, money=1000):  # each object will have a name, a number of stocks, and an amount of money
        self.stocks = stocks  # each object will be initialized to have 0 stocks and 1000 dollars
        self.money = money
        self.name = name

    def set_stocks(self, stocks):
        self.stocks = stocks

    def set_money(self, money):
        self.money = money

    def set_name(self, name):
        self.name = name

    def get_stocks():
        return self.stocks

    def get_money():
        return self.money

    def get_name():
        return self.name



def test_data(filename, col, day):
    
    """A test function to query the data you loaded into your program.

    Args:
        filename: A string for the filename containing the stock data,
                  in CSV format.

        col: A string of either "date", "open", "high", "low", "close",
             "volume", or "adj_close" for the column of stock market data to
             look into.

             The string arguments MUST be LOWERCASE!

        day: An integer reflecting the absolute number of the day in the
             data to look up, e.g. day 1, 15, or 1200.

    Returns:
        A value selected for the stock on some particular day, in some
        column col. The returned value *must* be of the appropriate type,
        such as float, int or str.
    """

    extracted = extract_info(filename)
    formatted = format(extracted, col, day)  # calling my funcations
    float_rep = float(formatted)  # getting the float representation of the info
    return float_rep


def main():

    name = input("Please enter your name: ")
    person = Portfolio(name)  # creating an object of the Portfolio class
    filename = input("Enter a filename for stock data (CSV format): ")

    print("\n***Moving Average Results***")
    print("\n{0} you started with {1} stocks and ${2:.2f}".format(person.name, person.stocks, person.money))
    # Call your moving average algorithm, with the filename to open.
    person.stocks, person.money = alg_moving_average(filename, person)
    # updating the objects money and stocks owned based on the results of the moving average function

    # Print results of the moving average algorithm, returned above:
    print("{0} you now own {1} stocks and have ${2:.2f}".format(person.name, person.stocks, person.money))
    moving_average_result = person.money  # to be used for statistics
    person.set_stocks(0)  # resetting the stocks and money so we can use the other algorithim
    person.set_money(1000)  # resetting the stocks and money so we can use the other algorithim

    print("\n***My Algorithim Results***")
    print("\n{0} you started with {1} stocks and ${2:.2f}".format(person.name, person.stocks, person.money))
    # Call your moving average algorithm, with the filename to open.
    person.stocks, person.money = alg_mine(filename, person)
    # updating the objects money and stocks owned based on the results of the moving average function

    # Print results of the moving average algorithm, returned above:
    print("{0} you now own {1} stocks and have ${2:.2f}".format(person.name, person.stocks, person.money))
    print("\n\n***Comparison (Statistics) ***")
    change = person.money-moving_average_result
    percent = change/moving_average_result

    if change >0:

        print("\nI made ${0:.2f} more in my algorithim than in the moving average algorithim for the {1} stock file".format(change, filename))

        print("This means I made {0:.2f}% more using my algorithim than\nthe moving average algorithim".format(100*percent))
        print("\n***Based on this I can say that my algorithim performs\nbetter than the moving average algorithim for the {0} stock file.***".format(filename))
    else:
        
        print("\nI made ${0:.2f} less in my algorithim than in the moving average algorithim for the {1} stock file".format(abs(change), filename))

        print("This means I made {0:.2f}% less using my algorithim than\nthe moving average algorithim".format(abs(100*percent)))
        print("\n***Based on this I can say that my algorithim performs\nworse than the moving average algorithim for the {0} stock file.***".format(filename))
        
if __name__ == '__main__':
    main()
