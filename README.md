# Currency Exchange Rate Analysis

## Table of Contents
* [General Info](#general-info)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Testing for Development](#testing-for-velopment)
* [Solutions](#solutions)
* [Future Plans](#future-plans)
* [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General Info
This application is designed to assist HSBC, the Swiss bank, in retrieving and analyzing currency exchange rate data from the National Bank of Poland (NBP) through its API. The program allows HSBC to obtain the value of a specified currency on a given date, which is crucial for issuing accurate invoices in foreign currencies in Poland. The invoices must be converted to Polish złoty (PLN) using the NBP exchange rates from specific dates, as required by regulations.

## Features
1. Retrieves the exchange rate of a specific currency on a given date from the NBP API.
2. Accepts currency and date as command-line arguments.
3. If currency and date are not provided as command-line arguments, the user is prompted to enter these details using the input() function.
4. Handles date parsing to the required format.
5. Requests the API response in JSON format.
6. Deals with situations when exchange rate tables are not published on weekends or public holidays.

## Technologies Used

The program is written in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites

To run this project, make sure you have Python 3.11.2 installed on your computer.

## Setup
To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program: using the command prompt or terminal:
```
python currency_exchange.py [currency_code] [date]
```
If the command-line arguments `[currency_code]` and `[date]` are not provided, the program will prompt you to enter them.

## Testing
?? TODO

## Solutions
The program fetches exchange rate data from the NBP API, which allows HSBC to accurately convert foreign currency amounts to Polish złoty (PLN) for invoicing purposes. By utilizing the API, HSBC can ensure compliance with Polish regulations regarding foreign currency invoicing.

## Future Plans
As the application's scope expands and requirements change, the following features or improvements could be considered:
- Adding visual representations (line charts or candlestick charts) to showcase currency trends over specific periods.
- Adding support for multiple currencies in a single request to optimize API calls.

## Inspirations and Acknowledgments
The program was adapted during the "Practical Python" training course. Thanks for the inspiring material and support!
