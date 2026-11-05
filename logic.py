def get_destination(offer):
    '''
    Gives the destination of an offer
    offer - dictionary with the keys destination, start, end, price
    returns the destination (str)
    '''
    return offer["destination"]

def get_start(offer):
    '''
    Gives the start date of an offer
    offer - dictionary with the keys destination, start, end, price
    returns the start date (str, with the format DD/MM/YYYY)
    '''
    return offer["start"]

def get_end(offer):
    '''
    Gives the end date of an offer
    offer - dictionary with the keys destination, start, end, price
    returns the end date (str, with the format DD/MM/YYYY)
    '''
    return offer["end"]

def get_price(offer):
    '''
    Gives the price of an offer
    offer - dictionary with the keys destination, start, end, price
    returns the price (float)
    '''
    return offer["price"]

def set_destination(offer, destination):
    '''
    Changes the destination of an offer
    offer - dictionary with the keys destination, start, end, price
    destination - str
    raises ValueError if the destination is not valid
    '''
    offer["destination"] = parse_destination(destination)

def set_start(offer, data_start):
    '''
    Changes the start date of an offer
    offer - dictionary with the keys destination, start, end, price
    data_start - str, with the format DD/MM/YYYY
    raises ValueError if the date is not valid or is after the end date
    '''
    if parse_date(data_start) > parse_date(get_end(offer)):
        raise ValueError("The start date can't be after the end date !")
    offer["start"] = str(data_start).strip()

def set_end(offer, data_end):
    '''
    Changes the end date of an offer
    offer - dictionary with the keys destination, start, end, price
    data_end - str, with the format DD/MM/YYYY
    raises ValueError if the date is not valid or is before the start date
    '''
    if parse_date(get_start(offer)) > parse_date(data_end):
        raise ValueError("The start date can't be after the end date !")
    offer["end"] = str(data_end).strip()

def set_price(offer, price):
    '''
    Changes the price of an offer
    offer - dictionary with the keys destination, start, end, price
    price - str or number
    raises ValueError if the price is not valid
    '''
    offer["price"] = parse_price(price)

def is_leap_year(year):
    '''
    Checks if a year is a leap year (a leap year comes once every 4 years)
    year - int
    returns True if the year is a leap year, False otherwise
    '''
    return year % 4 == 0

def days_in_month(month, year):
    '''
    Finds how many days a month has
    month - int (between 1 and 12)
    year - int
    returns the number of days of that month (int)
    '''
    if month == 2 and is_leap_year(year):
        return 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def split_date(date):
    '''
    Splits a date from text into numbers
    date - str, with the format DD/MM/YYYY
    returns the tuple (year, month, day), in this order so that two dates
    can be compared directly with < and >
    raises ValueError if the format is wrong, or if the day is not between
    1 and 31, or the month is not between 1 and 12
    '''
    parts = str(date).strip().split("/")
    if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        raise ValueError(f"Date '{date}' must have the format DD/MM/YYYY !")
    if not (parts[0].isdecimal() and parts[1].isdecimal() and parts[2].isdecimal()):
        raise ValueError(f"Date '{date}' must have the format DD/MM/YYYY !")

    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
        raise ValueError(f"Date '{date}' does not exist !")
    return (year, month, day)

def parse_date(date):
    '''
    Checks that a text is a real calendar date (used for the dates of an offer)
    date - str, with the format DD/MM/YYYY
    returns the tuple (year, month, day)
    raises ValueError if the date is not valid (example : 30/02/2026)
    '''
    year, month, day = split_date(date)
    if day > days_in_month(month, year):
        raise ValueError(f"Date '{date}' does not exist !")
    return (year, month, day)

def parse_interval(data_start, data_end):
    '''
    Checks the two limits of an interval of time
    The limits only use split_date, so 31/09/2026 from the problem statement
    is accepted as a limit, even if the day does not exist
    data_start, data_end - str, with the format DD/MM/YYYY
    returns the two limits as tuples (year, month, day)
    raises ValueError if a limit is not valid or if the start is after the end
    '''
    start = split_date(data_start)
    end = split_date(data_end)
    if start > end:
        raise ValueError("The start of the interval can't be after its end !")
    return start, end

def parse_price(price):
    '''
    Transforms a price into a float
    price - str or number
    returns the price (float)
    raises ValueError if the price is not a positive number
    '''
    try:
        value = float(price)
    except ValueError:
        raise ValueError("Price must be a positive number (example : 4435.25) !")
    if not 0 < value < float("inf"):
        raise ValueError("Price must be a positive number (example : 4435.25) !")
    return value

def parse_days(days):
    '''
    Transforms a number of days into an int
    days - str or int
    returns the number of days (int)
    raises ValueError if it is not a whole number that is 0 or bigger
    '''
    text = str(days).strip()
    if not text.isdecimal():
        raise ValueError("Number of days must be a whole number (example : 7) !")
    return int(text)

def parse_destination(destination):
    '''
    Cleans a destination so that "madrid", "MADRID" and " Madrid " are the same
    destination - str
    returns the destination with one space between words and capital
    first letters (example : "buenos  aires" becomes "Buenos Aires")
    raises ValueError if the destination has no letters
    '''
    cleaned = " ".join(destination.split()).title()
    for character in cleaned:
        if character.isalpha():
            return cleaned
    raise ValueError("Destination must contain letters !")

def date_to_days(date):
    '''
    Counts the days from the start of the calendar until a date
    date - tuple (year, month, day)
    returns the number of days (int)
    '''
    year, month, day = date
    total = day
    for y in range(1, year):
        total = total + 365
        if is_leap_year(y):
            total = total + 1
    for m in range(1, month):
        total = total + days_in_month(m, year)
    return total

def offer_duration(offer):
    '''
    Finds how many days an offer spans (end date - start date)
    offer - dictionary with the keys destination, start, end, price
    returns the number of days (int) (example : 11/08 to 20/08 is 9 days)
    '''
    return date_to_days(parse_date(get_end(offer))) - date_to_days(parse_date(get_start(offer)))

def add_offer(offer_list , destination , data_start , data_end, price):
    '''
    This function adds a new offer to the offer list
    offer_list - list of offers
    destination - str
    data_start, data_end - str, with the format DD/MM/YYYY
    price - str or number
    raises ValueError if the data is not valid, and then the list is not changed
    '''
    new_destination = parse_destination(destination)
    start = parse_date(data_start)
    end = parse_date(data_end)
    if start > end:
        raise ValueError("The start date can't be after the end date !")

    new_offer = {
        "destination" : new_destination,
        "start" : str(data_start).strip(),
        "end" : str(data_end).strip(),
        "price" : parse_price(price)
    }

    offer_list.append(new_offer)

def modify_price(offer_list, position, price):
    '''
    Changes the price of an offer
    offer_list - list of offers
    position - str or int, the number of the offer in the list, starting from 1
    price - str or number, the new price
    raises ValueError if the position or the price is not valid
    '''
    text = str(position).strip()
    if not text.isdecimal() or int(text) < 1 or int(text) > len(offer_list):
        raise ValueError(f"Offer number must be between 1 and {len(offer_list)} !")
    set_price(offer_list[int(text) - 1], price)

def keep_offers(offer_list, kept):
    '''
    Replaces the content of the offer list with the offers that remain
    offer_list - list of offers
    kept - list with the offers that remain
    returns how many offers were removed (int)
    '''
    removed = len(offer_list) - len(kept)
    offer_list[:] = kept
    return removed

def delete_by_destination(offer_list, destination):
    '''
    Deletes all the offers for a given destination
    offer_list - list of offers
    destination - str
    returns how many offers were removed (int)
    raises ValueError if the destination is not valid
    '''
    cleaned = parse_destination(destination)
    kept = []
    for o in offer_list:
        if get_destination(o) != cleaned:
            kept.append(o)
    return keep_offers(offer_list, kept)

def remove_shorter_than(offer_list, days):
    '''
    Removes all the offers with a shorter duration than a given number of days
    offer_list - list of offers
    days - str or int
    returns how many offers were removed (int)
    raises ValueError if the number of days is not valid
    '''
    limit = parse_days(days)
    kept = []
    for o in offer_list:
        if offer_duration(o) >= limit:
            kept.append(o)
    return keep_offers(offer_list, kept)

def remove_price_greater_than(offer_list, price):
    '''
    Removes all the offers with a price greater than a given price
    offer_list - list of offers
    price - str or number
    returns how many offers were removed (int)
    raises ValueError if the price is not valid
    '''
    limit = parse_price(price)
    kept = []
    for o in offer_list:
        if get_price(o) <= limit:
            kept.append(o)
    return keep_offers(offer_list, kept)

def offers_in_interval(offer_list, data_start, data_end):
    '''
    Finds the offers which take place completely inside an interval of time
    offer_list - list of offers
    data_start, data_end - str, with the format DD/MM/YYYY
    returns a list with the offers found
    raises ValueError if the interval is not valid
    '''
    start, end = parse_interval(data_start, data_end)
    found = []
    for o in offer_list:
        if parse_date(get_start(o)) >= start and parse_date(get_end(o)) <= end:
            found.append(o)
    return found

def offers_by_destination_and_price(offer_list, destination, price):
    '''
    Finds the offers with a given destination and a price smaller than a given price
    offer_list - list of offers
    destination - str
    price - str or number
    returns a list with the offers found
    raises ValueError if the destination or the price is not valid
    '''
    cleaned = parse_destination(destination)
    limit = parse_price(price)
    found = []
    for o in offer_list:
        if get_destination(o) == cleaned and get_price(o) < limit:
            found.append(o)
    return found

def offers_by_end_date(offer_list, data_end):
    '''
    Finds the offers with a given end date
    offer_list - list of offers
    data_end - str, with the format DD/MM/YYYY
    returns a list with the offers found
    raises ValueError if the date is not valid
    '''
    end = parse_date(data_end)
    found = []
    for o in offer_list:
        if parse_date(get_end(o)) == end:
            found.append(o)
    return found

def average_price(offer_list, destination):
    '''
    Computes the average price of the offers for a given destination
    offer_list - list of offers
    destination - str
    returns the average price (float)
    raises ValueError if the destination is not valid or has no offers
    '''
    cleaned = parse_destination(destination)
    total = 0
    count = 0
    for o in offer_list:
        if get_destination(o) == cleaned:
            total = total + get_price(o)
            count = count + 1
    if count == 0:
        raise ValueError(f"There are no offers for {cleaned} !")
    return total / count

def count_per_destination(offer_list):
    '''
    Counts the offers available for each destination
    offer_list - list of offers
    returns a dictionary {destination : number of offers}
    '''
    counts = {}
    for o in offer_list:
        destination = get_destination(o)
        if destination in counts:
            counts[destination] = counts[destination] + 1
        else:
            counts[destination] = 1
    return counts

def offers_containing(offer_list, substring):
    '''
    Finds the offers for which the destination contains a substring, without
    looking at capital letters
    offer_list - list of offers
    substring - str
    returns a list with the offers found, sorted alphabetically by destination
    raises ValueError if the substring is empty
    '''
    if substring.strip() == "":
        raise ValueError("The text to search for can't be empty !")
    found = []
    for o in offer_list:
        if substring.lower() in get_destination(o).lower():
            found.append(o)
    return sorted(found, key=get_destination)

def two_best_offers(offer_list, data_start, data_end):
    '''
    Finds the two cheapest offers which take place inside an interval of time
    offer_list - list of offers
    data_start, data_end - str, with the format DD/MM/YYYY
    returns a list with at most two offers, the cheapest one being first
    raises ValueError if the interval is not valid
    '''
    found = offers_in_interval(offer_list, data_start, data_end)
    return sorted(found, key=get_price)[:2]

def filter_by_destinations(offer_list, destinations):
    '''
    Eliminates the offers that have one of the given destinations
    offer_list - list of offers
    destinations - str, with destinations separated by commas
    (example : "Cairo, Buenos Aires, Vancouver")
    returns how many offers were removed (int)
    raises ValueError if the text has no valid destinations
    '''
    cleaned = []
    for destination in destinations.split(","):
        if destination.strip() != "":
            cleaned.append(parse_destination(destination))
    if len(cleaned) == 0:
        raise ValueError("Type at least one destination !")

    kept = []
    for o in offer_list:
        if get_destination(o) not in cleaned:
            kept.append(o)
    return keep_offers(offer_list, kept)

def filter_by_price_and_days(offer_list, price, days):
    '''
    Eliminates the offers with a price greater than a given price and,
    at the same time, a duration smaller than a given number of days
    offer_list - list of offers
    price - str or number
    days - str or int
    returns how many offers were removed (int)
    raises ValueError if the price or the number of days is not valid
    '''
    price_limit = parse_price(price)
    days_limit = parse_days(days)
    kept = []
    for o in offer_list:
        if not (get_price(o) > price_limit and offer_duration(o) < days_limit):
            kept.append(o)
    return keep_offers(offer_list, kept)

def copy_offers(offer_list):
    '''
    Makes a copy of the offer list, without using deepcopy
    Each offer is copied too, so changing a price in the list does not change the copy
    offer_list - list of offers
    returns the new list
    '''
    copy = []
    for o in offer_list:
        copy.append(o.copy())
    return copy

def save_state(history, before, offer_list):
    '''
    Remembers the old state of the list, only if an operation really changed it
    history - list with the old states of the list
    before - copy of the list, made before the operation
    offer_list - the list after the operation
    '''
    if before != offer_list:
        history.append(before)

def undo(offer_list, history):
    '''
    Reverts the list to the state before the last operation that modified it
    offer_list - list of offers
    history - list with the old states of the list
    raises ValueError if there is nothing to undo
    '''
    if len(history) == 0:
        raise ValueError("There is nothing to undo !")
    offer_list[:] = history.pop()