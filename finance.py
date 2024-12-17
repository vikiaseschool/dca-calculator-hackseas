import yfinance as yf
def get_annual_return_since_listing(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="max")


    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]


    years = (data.index[-1] - data.index[0]).days / 365.25

    annual_return = (end_price / start_price) ** (1 / years) - 1

    return round((annual_return * 100), 2)

def get_company_name(ticker):
    stock = yf.Ticker(ticker)
    company_name = stock.info.get('longName', 'Unknown Company')
    return company_name

def calculate_total_assets(start_capital, annual_return, years, frequency, how_much):
    if frequency == 1 or frequency == 2 or frequency == 3:
        n = float(365 / frequency)
    elif frequency == 7:
        n = 52
    elif frequency == 30:
        n = 12
    else:
        n = 26

    r = float(annual_return / 100)

    total_periods = years * n

    nasobek = ((1 + r / n) ** total_periods - 1) / (r / n)

    total_assets = start_capital * (1 + r / n) ** total_periods + how_much * nasobek

    return round(total_assets, 2)

def get_total_profit(start_capital, how_much, frequency, years, total_assets):
    if frequency == 1 or frequency == 2 or frequency == 3:
        n = float(365 / frequency)
    elif frequency == 7:
        n = 52
    elif frequency == 30:
        n = 12
    else:
        n = 26

    total_profit = total_assets - start_capital - how_much * n * years

    total_profit_perc = (total_profit / (start_capital + how_much * n * years)) * 100

    return round(total_profit, 2), round(total_profit_perc, 2)


def get_values_for_graph(start_capital, annual_return, years, how_much, frequency):
    if frequency == 1 or frequency == 2 or frequency == 3:
        n = float(365 / frequency)
    elif frequency == 7:
        n = 52
    elif frequency == 30:
        n = 12
    else:
        n = 26

    r = annual_return / 100
    total_value = start_capital
    total_investment_values = []

    total_periods = int(years * n)

    for period in range(1, total_periods + 1):
        total_value = total_value * (1 + r / n)

        total_value += how_much
        total_investment_values.append(round(total_value, 2))

    return total_investment_values