# Tourism Agency

A Python console application that manages the vacation offers of a tourism agency. You can add, change, remove, search and filter offers, see reports, and undo your changes.

Each offer has a destination, a start date, an end date and a price.

## How to run

You need Python 3 and nothing else, as the project uses no external libraries. It was tested on Python 3.11 and 3.13.

```bash
python main.py
```

## Example

```text
Select an option from above : 1
Type destination : Madrid
Type start data (DD/MM/YYYY) : 11/08/2026
Type end data (DD/MM/YYYY) : 20/08/2026
Type price : 4435.25
Offer added successfully !

Select an option from above : 2

The available offers are : 
Madrid from 11/08/2026 to 20/08/2026 costing 4435.25
```

## Features

| Option | What it does |
|---|---|
| 1 | Add a new offer |
| 2 | Show all offers |
| 3 | Modify the price of an offer |
| 4 | Delete all offers for a destination |
| 5 | Remove offers shorter than a number of days |
| 6 | Remove offers with a price greater than a given price |
| 7 | Show offers in an interval of time |
| 8 | Show offers for a destination, cheaper than a given price |
| 9 | Show offers with a given end date |
| 10 | Show the average price for a destination |
| 11 | Show the number of offers for each destination |
| 12 | Search destinations containing a text, sorted alphabetically |
| 13 | Show the two cheapest offers in an interval of time |
| 14 | Eliminate offers from a list of destinations |
| 15 | Eliminate offers above a given price and shorter than a number of days |
| 16 | Undo the last change to the list |
| E | Exit |

## Input rules

- **Dates:** use the format `DD/MM/YYYY`, such as `11/08/2026`. An offer's start date can't be after its end date.
- **Prices:** use a positive number with a dot, such as `4435.25`.
- **Destinations:** capital letters and extra spaces don't matter, so `madrid` and `Madrid` are the same destination.
- **Lists of destinations:** separate them with commas, such as `Cairo, Buenos Aires, Vancouver`.

If the input isn't valid, the program shows what went wrong and returns to the menu.

## How some options work

- **Duration:** this is the end date minus the start date, so 11/08 to 20/08 is 9 days.
- **Intervals:** an offer must start and end inside the interval to be included.
- **Leap years:** every 4th year counts as a leap year, with no exceptions.
- **Saved data:** offers are kept only while the program runs, so they are lost when you exit.

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Starts the application |
| `ui.py` | Shows the menu, reads the input and prints the results |
| `logic.py` | Holds the offers' logic, with no reading or printing |
| `tests.py` | Tests the functions from `logic.py` with `assert` statements |

## Running the tests

```bash
python tests.py
```

If everything works, it prints `All tests passed !`.
