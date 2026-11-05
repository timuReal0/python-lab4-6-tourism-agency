import logic

def show_menu():
    '''
    prints the menu
    '''
    print("\n--- Tourism Agency ---")
    print("1. Add a new offer")
    print("2. Show all offers")
    print("3. Modify the price of an offer")
    print("4. Delete all offers for a destination")
    print("5. Remove offers shorter than a number of days")
    print("6. Remove offers with a price greater than a given price")
    print("7. Show offers in an interval of time")
    print("8. Show offers for a destination, cheaper than a given price")
    print("9. Show offers with a given end date")
    print("10. Average price for a destination")
    print("11. Number of offers for each destination")
    print("12. Search destinations containing a text")
    print("13. Two best offers in an interval of time")
    print("14. Eliminate offers from a list of destinations")
    print("15. Eliminate expensive and short offers")
    print("16. Undo")
    print("E. Exit")

def read_offer():
    '''
    Read the offer's details
    '''
    destination = input("Type destination : ")
    data_start = input("Type start data (DD/MM/YYYY) : ")
    end_start = input("Type end data (DD/MM/YYYY) : ")
    price = input("Type price : ")
    return destination, data_start, end_start, price

def read_interval():
    '''
    Read the two limits of an interval of time
    '''
    data_start = input("Type start of the interval (DD/MM/YYYY) : ")
    data_end = input("Type end of the interval (DD/MM/YYYY) : ")
    return data_start, data_end

def print_offers(offer_list):
    '''
    Print all of the given offers
    '''
    if len(offer_list) == 0:
        print("\nNo offers found !")
        return
    print("\nThe available offers are : ")
    for o in offer_list:
        print(f"{logic.get_destination(o)} from {logic.get_start(o)} to {logic.get_end(o)} costing {logic.get_price(o):.2f}")

def print_numbered_offers(offer_list):
    '''
    Print all of the given offers with their number in front, starting from 1
    '''
    print("\nThe available offers are : ")
    number = 1
    for o in offer_list:
        print(f"{number}. {logic.get_destination(o)} from {logic.get_start(o)} to {logic.get_end(o)} costing {logic.get_price(o):.2f}")
        number = number + 1

def print_removed(removed):
    '''
    Print how many offers were removed
    '''
    print(f"Removed offers : {removed}")

def ui_add_offer(offers):
    data = read_offer()
    logic.add_offer(offers, data[0], data[1], data[2], data[3])
    print("Offer added successfully !")

def ui_modify_price(offers):
    if len(offers) == 0:
        print("\nNo offers found !")
        return
    print_numbered_offers(offers)
    position = input("Type the number of the offer : ")
    price = input("Type new price : ")
    logic.modify_price(offers, position, price)
    print("Price modified successfully !")

def ui_delete_by_destination(offers):
    destination = input("Type destination : ")
    print_removed(logic.delete_by_destination(offers, destination))

def ui_remove_shorter_than(offers):
    days = input("Type number of days : ")
    print_removed(logic.remove_shorter_than(offers, days))

def ui_remove_price_greater_than(offers):
    price = input("Type price : ")
    print_removed(logic.remove_price_greater_than(offers, price))

def ui_offers_in_interval(offers):
    data = read_interval()
    print_offers(logic.offers_in_interval(offers, data[0], data[1]))

def ui_offers_by_destination_and_price(offers):
    destination = input("Type destination : ")
    price = input("Type price : ")
    print_offers(logic.offers_by_destination_and_price(offers, destination, price))

def ui_offers_by_end_date(offers):
    data_end = input("Type end data (DD/MM/YYYY) : ")
    print_offers(logic.offers_by_end_date(offers, data_end))

def ui_average_price(offers):
    destination = input("Type destination : ")
    print(f"The average price is : {logic.average_price(offers, destination):.2f}")

def ui_count_per_destination(offers):
    counts = logic.count_per_destination(offers)
    if len(counts) == 0:
        print("\nNo offers found !")
        return
    print("\nThe number of offers for each destination : ")
    for destination in counts:
        print(f"{destination} : {counts[destination]}")

def ui_offers_containing(offers):
    substring = input("Type the text to search for : ")
    print_offers(logic.offers_containing(offers, substring))

def ui_two_best_offers(offers):
    data = read_interval()
    print_offers(logic.two_best_offers(offers, data[0], data[1]))

def ui_filter_by_destinations(offers):
    destinations = input("Type destinations separated by commas : ")
    print_removed(logic.filter_by_destinations(offers, destinations))

def ui_filter_by_price_and_days(offers):
    price = input("Type price : ")
    days = input("Type number of days : ")
    print_removed(logic.filter_by_price_and_days(offers, price, days))

def ui_undo(offers, history):
    logic.undo(offers, history)
    print("Undo done successfully !")

def run_UI():
    offers = []
    history = []

    while(True):
       show_menu()
       option = input("Select an option from above : ")
       before = logic.copy_offers(offers)
       try:
            if option == "1":
                ui_add_offer(offers)
            elif option == "2":
                print_offers(offers)
            elif option == "3":
                ui_modify_price(offers)
            elif option == "4":
                ui_delete_by_destination(offers)
            elif option == "5":
                ui_remove_shorter_than(offers)
            elif option == "6":
                ui_remove_price_greater_than(offers)
            elif option == "7":
                ui_offers_in_interval(offers)
            elif option == "8":
                ui_offers_by_destination_and_price(offers)
            elif option == "9":
                ui_offers_by_end_date(offers)
            elif option == "10":
                ui_average_price(offers)
            elif option == "11":
                ui_count_per_destination(offers)
            elif option == "12":
                ui_offers_containing(offers)
            elif option == "13":
                ui_two_best_offers(offers)
            elif option == "14":
                ui_filter_by_destinations(offers)
            elif option == "15":
                ui_filter_by_price_and_days(offers)
            elif option == "16":
                ui_undo(offers, history)
                continue
            elif option == "E":
                print("Goodbye !")
                exit()
            else:
                print("Invalid option !")
            logic.save_state(history, before, offers)
       except ValueError as error:
            print(f"Error : {error}")