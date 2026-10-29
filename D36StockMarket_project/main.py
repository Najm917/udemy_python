import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "SKQWUMEGGBS2JAO5"
NEWS_API_KEY = "cfa49206fd764ca4b4faf1f2a256abe4"[cite: 8]

BOT_TOKEN = "9177182614:AAH6sbPXQGr6rR1T7cHWd4fWUY3QeAFwXE8"
CHAT_ID = "8951054263"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TELEGRAM_ENDPOINT = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

responce = requests.get(STOCK_ENDPOINT, params=stock_params)
responce.raise_for_status()
raw_data = responce.json()

# FIX 1: Brackets [] hataye
data = raw_data.get("Time Series (Daily)")

if data is None:
    print("API error ya limit hit:", raw_data)
else:
    data_list = [value for (key, value) in data.items()]
    yestarday_data = data_list[0]
    yestarday_closing_price = float(yestarday_data["4. close"])
    print("Yesterday Close:", yestarday_closing_price)

    # TODO 2. - Get day before yesterday's closing price
    day_befor_yestarday_data = data_list[1]
    day_befor_yestarday_closing_price = float(day_befor_yestarday_data["4. close"])
    print("Day Before Yesterday Close:", day_befor_yestarday_closing_price)

    # Up/Down Icon logic
    difference_raw = yestarday_closing_price - day_befor_yestarday_closing_price
    up_down = "🔺" if difference_raw > 0 else "🔻"

    # TODO 3. - Positive difference
    difference = abs(difference_raw)
    print("Difference:", difference)

    # TODO 4. - Percentage difference
    diff_percent = round((difference / day_befor_yestarday_closing_price) * 100, 2)
    print(f"Diff Percent: {diff_percent}%")

    # TODO 5. - Check if threshold is crossed (testing ke liye >= 0 set hai)
    if diff_percent >= 0:
        news_params = {
            "q": "Tesla",
            "apiKey": NEWS_API_KEY,
            "sortBy": "publishedAt",
            "language": "en",
        }
        news_responce = requests.get(NEWS_ENDPOINT, params=news_params)
        # FIX 2: news_responce check karein
        news_responce.raise_for_status()
        article = news_responce.json().get("articles", [])

        three_articles = article[:3]

        # TODO 8. - List comprehension for formatted messages
        formatted_articles = [
            f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
            f"Headline: {art['title']}\n"
            f"Brief: {art['description']}"
            for art in three_articles
        ]

        # TODO 9. - Send each article via Telegram
        for msg in formatted_articles:
            telegram_params = {
                "chat_id": CHAT_ID,
                "text": msg,
            }
            res = requests.post(TELEGRAM_ENDPOINT, json=telegram_params)
            print("Telegram Status:", res.status_code)

        print(f"Successfully sent {len(formatted_articles)} alerts to Telegram.")
    else:
        print(f"Price change ({diff_percent}%) threshold se kam hai. No alert sent.")