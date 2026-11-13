# Tourism Agency – Vacation Offers Manager

A menu-based console application, written in Python, that manages the vacation offers
of a tourism agency. Each offer has a destination, a start date, an end date and a price.

Developed for Lab 4-6 of an introductory programming course, in three iterations,
using feature-driven and test-driven development.

## Features

| Option | Feature |
|--------|---------|
| `1` | Add a new offer |
| `2` | Show all offers |
| `3` | Modify the price of an offer |
| `4` | Delete all offers for a destination |
| `5` | Remove offers shorter than a given number of days |
| `6` | Remove offers with a price greater than a given price |
| `7` | Show the offers that take place in an interval of time |
| `8` | Show the offers for a destination, cheaper than a given price |
| `9` | Show the offers with a given end date |
| `10` | Average price for a destination |
| `11` | Number of offers for each destination |
| `12` | Search destinations containing a text, sorted alphabetically |
| `13` | The two cheapest offers in an interval of time |
| `14` | Eliminate the offers for a list of destinations |
| `15` | Eliminate the offers that are both expensive and short |
| `16` | Undo the last operation that changed the list |
| `E` | Exit |

## Project structure

| File | Contents |
|------|----------|
| `main.py` | Starts the application |
| `ui.py` | Console interface: the menu, reading input and printing results |
| `logic.py` | All computations and validations, with no input or output |
| `tests.py` | Tests written with `assert` for every function in `logic.py` |

## Implementation details

- Each offer is a dictionary, accessed only through getter and setter functions
  (`get_price`, `set_price`, ...).
- Dates are typed as DD/MM/YYYY and converted to tuples (year, month, day),
  so two dates can be compared directly with `<` and `>`.
- All input is validated in `logic.py`. Invalid data raises a `ValueError`
  with a clear message, the interface prints it, and the program keeps running.
- Undo works without `deepcopy`: before every operation the list is copied offer by offer,
  and the copy is saved in the history only if the operation actually changed the list.

## Example

Starting from the offers in the problem statement:

```
Madrid,       11/08/2026 - 20/08/2026,  4435.25
Buenos Aires, 06/03/2026 - 21/03/2026, 10215.75
Athens,       13/09/2026 - 19/09/2026,  3298.90
Cairo,        15/08/2026 - 25/08/2026,  3925.30
Helsinki,     24/09/2026 - 02/10/2026,  2010.75
```

- Option `7` with the interval 01/09/2026 - 31/09/2026 shows only the Athens offer.
- Option `12` with the text "e" shows Athens, Buenos Aires and Helsinki, in this order.
- Option `13` with the interval 01/07/2026 - 01/10/2026 shows Athens and Cairo.
- Option `14` with "Cairo, Buenos Aires, Vancouver" leaves Madrid, Athens and Helsinki.

## How to run

Requires Python 3.

```
python main.py
```

To run the tests:

```
python tests.py
```

or, with pytest installed, `pytest tests.py`.

## Documentation

`DocumentLab4.pdf` contains the problem statement, the list of features,
the plan for the three iterations, use case scenarios and the tasks for each feature.
