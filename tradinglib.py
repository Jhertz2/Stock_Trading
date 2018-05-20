
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


def sell(shares, today, value):  # function to call when we decide to sell. Everytime we
    # sell, we sell all of the stock that we own.

    value = float(value + (shares * today))  # amount is the amount of money we now have
    shares = 0
    return shares, value


def buy(shares, today, value):  # function to call when we decide to buy. Everytime we buy
    # we buy all of the stock that our money will allow us to buy
    can_buy = int(value/today)  # how many stocks you can buy
    shares = shares + can_buy  # if we sell, the # of stocks we just got
    spent = can_buy * today  # for how much money we spend
    value = value - spent  # update the money we have

    return shares, value

def alg_moving_average(filename, person):  # changed the paramters to accept an object as well

    total = 0
    extracted = extract_info(filename)

    # for first 20 days of values
    for i in range(1, 21):  # for first 20 days
        x = get_value(extracted, "close", i)
        total = total + x
    moving_avg = float(total/20)  # moving average for the first 20 days
    total = 0  # reset the variable

    for i in range(21, 4049):  # run from day 21 until the last day (day 4048)
        today = get_value(extracted, "close", i)

        if ((today > float(moving_avg * 1.2)) or (i == 4048)):  # if todays value is 20% greater than the moving average
            if(person.stocks != 0):
                person.stocks, person.money = sell(person.stocks, today, person.money)  # update how much money we have and how many stocks we have

        if (today < float(moving_avg * .8)):  # if today's value is 20% less than the moving average

            person.stocks, person.money = buy(person.stocks, today, person.money)  # update how much money we have and how many stocks we have

        for j in range(i-19, i+1):  # calculate the new runnning average for the next day's comparison
            # this loop runs for the last 20 days. i-19 is so the loop starts
            # at the right spot. If we're on day i = 23 the loop will start
            # on day (23-19) 4 [inclusive] and end on day (23+1) 24 [exclusive]
            # this will allow the moving average to be compared with day 24 (next iteration)

            x = get_value(extracted, "close", j)
            total = total + x
        moving_avg = float(total/20)  # new moving average
        total = 0  # reset the variable

    return int(person.stocks), float(person.money)


def alg_mine(filename, person):  # changed the parameters to accept a parameter
    # book keeping, list to hold owned stocks in future milestones
    extracted = extract_info(filename)

    up_count = 0
    down_count = 0

    for i in range(1, 4049):  # run until the last day (day 4048)
        _open = float(get_value(extracted, "open", i))
        close = float(get_value(extracted, "close", i))
        difference = _open - close
        # if difference is positive (close is less than open) then stock price went down that day
        # if difference is negative (close is greater than open) the stock price went up that day

        if (difference < 0):  # if the stock went up in price that day incremnet the "up counter" and reset the "down counter" to 0.
            up_count += 1
            down_count = 0
        if(difference > 0):  # if the stock went down in price that day incremnet the "down counter" and reset the "up counter" to 0.
            up_count = 0
            down_count += 1
        if(difference == 0):  # if it neither went up or down, reset both counters to 0
            up_count = 0
            down_count = 0

        if ((up_count == 9) or (i == 4048)):  # if the stock has gone up in price 9 days in a row
            if(person.stocks != 0):
                person.stocks, person.money = sell(person.stocks, close, person.money)   # update how much money we have and how many stocks we have
                up_count = 0  # reset the up counter to 0

        if (down_count == 3):  # if the stock has gone down in price for 3 days in a row

            person.stocks, person.money = buy(person.stocks, close, person.money)  # update how much money we have
            down_count = 0  # reset he down counter to 0

    return int(person.stocks), float(person.money)
