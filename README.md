# DCA Calculator

## Overview

The DCA (Dollar-Cost Averaging) Calculator is a web application that helps users simulate and analyze their investment strategies using the DCA method. The application allows users to input various parameters such as the investment instrument, starting capital, investment frequency, and amount to invest. It then calculates the potential returns and displays the results in a user-friendly format.

## Features

- Select from predefined investment instruments or enter a custom ticker.
- Input investment horizon, starting capital, investment frequency, and amount to invest.
- Calculate total assets and profit based on the provided inputs.
- Display investment growth over time using a line chart.
- User-friendly interface with validation and error handling.

## Technologies Used

- Python
- Flask
- yfinance
- Pandas
- Bootstrap
- Chart.js


## File Structure

- `app.py`: Main application file that handles routes and logic.
- `finance.py`: Contains functions for financial calculations and data retrieval.
- `templates/`: Directory containing HTML templates for the web pages.
  - `index.html`: Main input form page.
  - `result.html`: Results display page.
- `vercel.json`: Configuration file for deploying the application on Vercel.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
