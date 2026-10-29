import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

# Aapki Verified Keys:
STOCK_API_KEY = "NBFS65UZQWB70XV" 
NEWS_API_KEY = "cfa49206fd764ca4b4faf1f2a256abe4" 

BOT_TOKEN = "9177182614:AAH6sbPXQGr6rR1T7cHWd4fWUY3QeAFwXE8"
CHAT_ID = "8951054263"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TELEGRAM_ENDPOINT = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ----------------- STEP 1: STOCK PRICE CALCULATION -----------------
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()

time_series = data.get("Time Series (Daily)", {})
data_list = [value for (key, value) in time_series.items()]

if len(data_list) >= 2:
    yesterday_closing_price = float(data_list[0]["4. close"])
    day_before_yesterday_closing_price = float(data_list[1]["4. close"])

    difference = yesterday_closing_price - day_before_yesterday_closing_price
    up_down = "🔺" if difference > 0 else "🔻"
    diff_percent = round((abs(difference) / day_before_yesterday_closing_price) * 100, 2)
    print(f"Calculated Price Difference: {diff_percent}%")

    # Testing ke liye threshold >= 0 rakha hai taaki turant alert aaye
    if diff_percent >= 0:
        # ----------------- STEP 2: FETCH NEWS -----------------
        news_params = {
            "q": COMPANY_NAME,
            "apiKey": NEWS_API_KEY,
            "sortBy": "publishedAt",
            "language": "en",
        }

        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        news_data = news_response.json()
        articles = news_data.get("articles", [])
        print(f"Total articles fetched: {len(articles)}")

        three_articles = articles[:3]

        if not three_articles:
            formatted_articles = [
                f"{STOCK_NAME}: {up_down}{diff_percent}%\nAlert: News articles nahi mile."
            ]
        else:
            formatted_articles = [
                f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
                f"Headline: {article.get('title')}\n"
                f"Brief: {article.get('description')}"
                for article in three_articles
            ]

        # ----------------- STEP 3: SEND VIA TELEGRAM -----------------
        for msg in formatted_articles:
            telegram_params = {
                "chat_id": CHAT_ID,
                "text": msg,
            }
            res = requests.post(TELEGRAM_ENDPOINT, json=telegram_params)
            print("Telegram Response Status:", res.status_code)

        print(f"Sent {len(formatted_articles)} alerts to Telegram successfully!")
else:
    print("Market data fetch nahi ho paya. Response:", data)