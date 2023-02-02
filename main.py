import stock_data
from stock_data import get_stock_info
from news_data import get_news_data
from send_sms_email import send_mail, send_message
import time

best_stocks = ["TSLA", "AAPL", "AMZN", "GOOG", "MSFT", "BA", "V", "JPM", "WMT", "PG", "FB", "BRK.A", "BRK.B", "DIS", "TATAMOTORS", "HDFCBANK", "RELIANCE", "INFY", "TCS", "BAJAJFINSV"]
for i, STOCK_NAME in enumerate(best_stocks):
    stock_info = get_stock_info(STOCK_NAME)
    # this check for free version as stock website allow only 5 calls per minutes. Max limit/day is 500.
    if (i + 1) % 4 == 0:
        time.sleep(100)
    elif stock_data.required_change:
        news_data = stock_info + get_news_data(STOCK_NAME)
        send_mail(STOCK_NAME, news_data)
        # send MSG
        # send_message(message_to_send=news_data)
