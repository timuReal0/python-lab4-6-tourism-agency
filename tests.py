from logic import *

def sample_offers():
    '''
    Creates the list of offers used as an example in the problem statement
    '''
    offers = []
    add_offer(offers, "Madrid", "11/08/2026", "20/08/2026", 4435.25)
    add_offer(offers, "Buenos Aires", "06/03/2026", "21/03/2026", 10215.75)
    add_offer(offers, "Athens", "13/09/2026", "19/09/2026", 3298.90)
    add_offer(offers, "Cairo", "15/08/2026", "25/08/2026", 3925.30)
    add_offer(offers, "Helsinki", "24/09/2026", "02/10/2026", 2010.75)
    return offers

def destinations_of(offer_list):
    '''
    Gives only the destinations of some offers, so the asserts are shorter
    '''
    names = []
    for o in offer_list:
        names.append(get_destination(o))
    return names

def gives_error(function, *arguments):
    '''
    Checks that calling a function with these arguments raises ValueError
    '''
    try:
        function(*arguments)
    except ValueError:
        return True
    return False

def test_get_destination():
    assert get_destination(sample_offers()[0]) == "Madrid"

def test_get_start():
    assert get_start(sample_offers()[0]) == "11/08/2026"

def test_get_end():
    assert get_end(sample_offers()[0]) == "20/08/2026"

def test_get_price():
    assert get_price(sample_offers()[0]) == 4435.25

def test_set_destination():
    offer = sample_offers()[0]

    set_destination(offer, "  new york ")
    assert get_destination(offer) == "New York"

    assert gives_error(set_destination, offer, "123")
    assert get_destination(offer) == "New York"

def test_set_start():
    offer = sample_offers()[0]

    set_start(offer, "12/08/2026")
    assert get_start(offer) == "12/08/2026"

    assert gives_error(set_start, offer, "21/08/2026")
    assert gives_error(set_start, offer, "abc")
    assert get_start(offer) == "12/08/2026"

def test_set_end():
    offer = sample_offers()[0]

    set_end(offer, "25/08/2026")
    assert get_end(offer) == "25/08/2026"

    assert gives_error(set_end, offer, "10/08/2026")
    assert gives_error(set_end, offer, "31/09/2026")
    assert get_end(offer) == "25/08/2026"

def test_set_price():
    offer = sample_offers()[0]

    set_price(offer, "99.5")
    assert get_price(offer) == 99.5

    assert gives_error(set_price, offer, "abc")
    assert gives_error(set_price, offer, -1)
    assert get_price(offer) == 99.5

def test_is_leap_year():
    assert is_leap_year(2024) == True
    assert is_leap_year(2026) == False
    assert is_leap_year(2028) == True
    assert is_leap_year(2025) == False

def test_days_in_month():
    assert days_in_month(1, 2026) == 31
    assert days_in_month(9, 2026) == 30
    assert days_in_month(2, 2026) == 28
    assert days_in_month(2, 2024) == 29

def test_split_date():
    assert split_date("11/08/2026") == (2026, 8, 11)
    assert split_date("31/09/2026") == (2026, 9, 31)
    assert gives_error(split_date, "1/8/2026")
    assert gives_error(split_date, "11-08-2026")
    assert gives_error(split_date, "ab/cd/efgh")
    assert gives_error(split_date, "32/01/2026")
    assert gives_error(split_date, "10/13/2026")
    assert gives_error(split_date, "")

def test_parse_date():
    assert parse_date("29/02/2024") == (2024, 2, 29)
    assert gives_error(parse_date, "29/02/2026")
    assert gives_error(parse_date, "31/09/2026")

def test_parse_interval():
    assert parse_interval("01/09/2026", "31/09/2026") == ((2026, 9, 1), (2026, 9, 31))
    assert gives_error(parse_interval, "10/09/2026", "01/09/2026")

def test_parse_price():
    assert parse_price("4435.25") == 4435.25
    assert parse_price(100) == 100.0
    assert gives_error(parse_price, "abc")
    assert gives_error(parse_price, "")
    assert gives_error(parse_price, "4435,25")
    assert gives_error(parse_price, "0")
    assert gives_error(parse_price, "-5")
    assert gives_error(parse_price, "nan")
    assert gives_error(parse_price, "inf")

def test_parse_days():
    assert parse_days("7") == 7
    assert parse_days(0) == 0
    assert gives_error(parse_days, "abc")
    assert gives_error(parse_days, "-1")
    assert gives_error(parse_days, "2.5")

def test_parse_destination():
    assert parse_destination("Madrid") == "Madrid"
    assert parse_destination("  buenos   AIRES ") == "Buenos Aires"
    assert gives_error(parse_destination, "")
    assert gives_error(parse_destination, "   ")
    assert gives_error(parse_destination, "123")

def test_date_to_days():
    assert date_to_days((2026, 1, 2)) - date_to_days((2026, 1, 1)) == 1
    assert date_to_days((2026, 3, 1)) - date_to_days((2026, 2, 28)) == 1
    assert date_to_days((2024, 3, 1)) - date_to_days((2024, 2, 28)) == 2
    assert date_to_days((2027, 1, 1)) - date_to_days((2026, 12, 31)) == 1

def test_offer_duration():
    offers = sample_offers()
    assert offer_duration(offers[0]) == 9
    assert offer_duration(offers[4]) == 8

def test_add_offer():
    offers = []

    add_offer(offers, "Madrid", "11/08/2026", "20/08/2026", 4435.25)

    assert len(offers) == 1

    assert offers[0]["destination"] == "Madrid"
    assert offers[0]["price"] == 4435.25

def test_add_offer_invalid_data():
    offers = []

    assert gives_error(add_offer, offers, "", "11/08/2026", "20/08/2026", 100)
    assert gives_error(add_offer, offers, "Madrid", "31/09/2026", "01/10/2026", 100)
    assert gives_error(add_offer, offers, "Madrid", "11/08/2026", "tomorrow", 100)
    assert gives_error(add_offer, offers, "Madrid", "20/08/2026", "11/08/2026", 100)
    assert gives_error(add_offer, offers, "Madrid", "11/08/2026", "20/08/2026", "abc")

    assert len(offers) == 0

def test_modify_price():
    offers = sample_offers()

    modify_price(offers, 1, 5000)
    assert get_price(offers[0]) == 5000.0
    assert get_price(offers[1]) == 10215.75

    modify_price(offers, "5", "99.5")
    assert get_price(offers[4]) == 99.5

    assert gives_error(modify_price, offers, 0, 100)
    assert gives_error(modify_price, offers, 6, 100)
    assert gives_error(modify_price, offers, "abc", 100)
    assert gives_error(modify_price, offers, 1, "abc")
    assert get_price(offers[0]) == 5000.0

def test_keep_offers():
    offers = sample_offers()
    assert keep_offers(offers, offers[:2]) == 3
    assert destinations_of(offers) == ["Madrid", "Buenos Aires"]

def test_delete_by_destination():
    offers = sample_offers()
    add_offer(offers, "Cairo", "01/01/2026", "05/01/2026", 500)

    assert delete_by_destination(offers, "cairo") == 2
    assert destinations_of(offers) == ["Madrid", "Buenos Aires", "Athens", "Helsinki"]
    assert delete_by_destination(offers, "Vancouver") == 0
    assert len(offers) == 4
    assert gives_error(delete_by_destination, offers, "")

def test_remove_shorter_than():
    offers = sample_offers()

    assert remove_shorter_than(offers, 9) == 2
    assert destinations_of(offers) == ["Madrid", "Buenos Aires", "Cairo"]
    assert gives_error(remove_shorter_than, offers, "abc")

def test_remove_price_greater_than():
    offers = sample_offers()

    assert remove_price_greater_than(offers, 3925.30) == 2
    assert destinations_of(offers) == ["Athens", "Cairo", "Helsinki"]
    assert gives_error(remove_price_greater_than, offers, "abc")

def test_offers_in_interval():
    offers = sample_offers()

    found = offers_in_interval(offers, "01/09/2026", "31/09/2026")
    assert destinations_of(found) == ["Athens"]

    found = offers_in_interval(offers, "11/08/2026", "20/08/2026")
    assert destinations_of(found) == ["Madrid"]

    assert gives_error(offers_in_interval, offers, "abc", "31/09/2026")
    assert gives_error(offers_in_interval, offers, "01/10/2026", "01/09/2026")

def test_offers_by_destination_and_price():
    offers = sample_offers()
    add_offer(offers, "Madrid", "01/01/2026", "05/01/2026", 500)

    found = offers_by_destination_and_price(offers, "madrid", 4435.25)
    assert len(found) == 1
    assert get_price(found[0]) == 500.0
    assert offers_by_destination_and_price(offers, "Vancouver", 9999) == []
    assert gives_error(offers_by_destination_and_price, offers, "Madrid", "abc")

def test_offers_by_end_date():
    offers = sample_offers()

    assert destinations_of(offers_by_end_date(offers, "25/08/2026")) == ["Cairo"]
    assert offers_by_end_date(offers, "26/08/2026") == []
    assert gives_error(offers_by_end_date, offers, "abc")

def test_average_price():
    offers = sample_offers()
    add_offer(offers, "Madrid", "01/01/2026", "05/01/2026", 564.75)

    assert average_price(offers, "madrid") == 2500.0
    assert gives_error(average_price, offers, "Vancouver")

def test_count_per_destination():
    offers = sample_offers()
    add_offer(offers, "madrid", "01/01/2026", "05/01/2026", 500)

    counts = count_per_destination(offers)
    assert counts["Madrid"] == 2
    assert counts["Cairo"] == 1
    assert len(counts) == 5
    assert count_per_destination([]) == {}

def test_offers_containing():
    offers = sample_offers()

    assert destinations_of(offers_containing(offers, "e")) == ["Athens", "Buenos Aires", "Helsinki"]
    assert destinations_of(offers_containing(offers, "airo")) == ["Cairo"]
    assert destinations_of(offers_containing(offers, "AIRO")) == ["Cairo"]
    assert offers_containing(offers, "xyz") == []
    assert gives_error(offers_containing, offers, "")

def test_two_best_offers():
    offers = sample_offers()

    found = two_best_offers(offers, "01/07/2026", "01/10/2026")
    assert destinations_of(found) == ["Athens", "Cairo"]

    found = two_best_offers(offers, "01/01/2026", "31/12/2026")
    assert destinations_of(found) == ["Helsinki", "Athens"]

    found = two_best_offers(offers, "01/09/2026", "31/09/2026")
    assert destinations_of(found) == ["Athens"]

    assert two_best_offers(offers, "01/01/2030", "31/12/2030") == []
    assert gives_error(two_best_offers, offers, "abc", "01/10/2026")

def test_filter_by_destinations():
    offers = sample_offers()

    assert filter_by_destinations(offers, "Cairo, Buenos Aires, Vancouver") == 2
    assert destinations_of(offers) == ["Madrid", "Athens", "Helsinki"]
    assert gives_error(filter_by_destinations, offers, " , ")
    assert len(offers) == 3

def test_filter_by_price_and_days():
    offers = sample_offers()

    assert filter_by_price_and_days(offers, 3000, 7) == 1
    assert destinations_of(offers) == ["Madrid", "Buenos Aires", "Cairo", "Helsinki"]
    assert gives_error(filter_by_price_and_days, offers, "abc", 7)
    assert gives_error(filter_by_price_and_days, offers, 3000, "abc")

def test_copy_offers():
    offers = sample_offers()
    copy = copy_offers(offers)
    assert copy == offers

    set_price(offers[0], 1.0)
    assert get_price(copy[0]) == 4435.25

def test_save_state():
    offers = sample_offers()
    history = []

    before = copy_offers(offers)
    delete_by_destination(offers, "Vancouver")
    save_state(history, before, offers)
    assert len(history) == 0

    before = copy_offers(offers)
    delete_by_destination(offers, "Cairo")
    save_state(history, before, offers)
    assert len(history) == 1

def test_undo():
    offers = sample_offers()
    history = []
    assert gives_error(undo, offers, history)

    before = copy_offers(offers)
    modify_price(offers, 1, 5000)
    save_state(history, before, offers)

    before = copy_offers(offers)
    delete_by_destination(offers, "Cairo")
    save_state(history, before, offers)

    undo(offers, history)
    assert len(offers) == 5
    assert get_price(offers[0]) == 5000.0

    undo(offers, history)
    assert get_price(offers[0]) == 4435.25
    assert gives_error(undo, offers, history)

def run_all_tests():
    '''
    Runs all the tests, so they also work without pytest
    '''
    test_get_destination()
    test_get_start()
    test_get_end()
    test_get_price()
    test_set_destination()
    test_set_start()
    test_set_end()
    test_set_price()
    test_is_leap_year()
    test_days_in_month()
    test_split_date()
    test_parse_date()
    test_parse_interval()
    test_parse_price()
    test_parse_days()
    test_parse_destination()
    test_date_to_days()
    test_offer_duration()
    test_add_offer()
    test_add_offer_invalid_data()
    test_modify_price()
    test_keep_offers()
    test_delete_by_destination()
    test_remove_shorter_than()
    test_remove_price_greater_than()
    test_offers_in_interval()
    test_offers_by_destination_and_price()
    test_offers_by_end_date()
    test_average_price()
    test_count_per_destination()
    test_offers_containing()
    test_two_best_offers()
    test_filter_by_destinations()
    test_filter_by_price_and_days()
    test_copy_offers()
    test_save_state()
    test_undo()
    print("All tests passed !")

if __name__ == "__main__":
    run_all_tests()