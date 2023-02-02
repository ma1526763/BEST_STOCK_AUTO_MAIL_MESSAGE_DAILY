from datetime import datetime, timedelta
import os
import requests

# STOCK RELATED
ALPHA_ADVANTAGE_API_KEY = os.environ['STOCK_API_KEY']
ALPHA_ADVANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query"
required_change = False
def get_stock_info(STOCK_NAME):
    global required_change
    required_change = False
    alpha_stock_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK_NAME,
        "interval": "60min",
        "outputsize": "compact",
        "apikey": ALPHA_ADVANTAGE_API_KEY
    }
    try:
        stock_data = requests.get(ALPHA_ADVANTAGE_API_ENDPOINT, params=alpha_stock_parameters).json()['Time Series (Daily)']
    except KeyError:
        return f"Check your stock name {STOCK_NAME}"
    else:
        # taking yesterday date to avoid notifications on holidays
        yesterday_date = [key for key in stock_data.keys()][0]
        yesterday_data = [daily_data for daily_data in stock_data.values()][0]
        previous_day = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        if previous_day == yesterday_date:
            opening_price = float(yesterday_data["1. open"])
            closing_price = float(yesterday_data["4. close"])
            change_in_price = round((float(closing_price) - float(opening_price)) / float(opening_price) * 100, 2)
            stock_info = f"🔻 {STOCK_NAME} Stocks decreased by {change_in_price}%.\n"
            if abs(change_in_price) >= 1:
                if change_in_price >= 1:
                    required_change = True
                    stock_info = f"🔺 {STOCK_NAME} Stocks increased by {change_in_price}%.\n"
                return stock_info
            return f"{STOCK_NAME} {change_in_price}%"
