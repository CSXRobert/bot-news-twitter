# Twitter News Bot 🤖📰

This bot posts random news stories to Twitter and a summary of them every 35 minutes. The news may vary depending on the categories selected in the News API (sports, international, entertainment, etc.). It has a timer to estimate the time of the next post.

A Python bot that fetches news from **NewsAPI**, summarizes it using **Hugging Face's BART model**, and posts to **Twitter** at regular intervals.

## Features ✨
- Fetches news in 6 categories (business, tech, sports, etc.).
- Uses AI to generate concise summaries.
- Posts to Twitter every 35 minutes (configurable).

## Prerequisites 📋
- Python 3.8+
- Twitter Developer Account ([Get API Keys](https://developer.twitter.com/))
- NewsAPI Key ([Sign Up Here](https://newsapi.org/))
- Hugging Face `transformers` library (for summarization).

## Setup & Installation 🛠️

1. **Clone this repository**:
   ```bash
   git clone https://github.com/CSXRobert/bot-news-twitter.git
   cd bot-news-twitter

2. **Install dependencies**:
   pip install requests tweepy transformers python-dotenv

3. **Edit the .env file:**:
# Twitter API
TWITTER_API_KEY=YOUR_API_KEY_HERE
TWITTER_API_SECRET=YOUR_API_SECRET_HERE
TWITTER_ACCESS_TOKEN=YOUR_ACCESS_TOKEN_HERE
TWITTER_ACCESS_SECRET=YOUR_ACCESS_SECRET_HERE
TWITTER_BEARER_TOKEN=YOUR_BEARER_TOKEN_HERE

# NewsAPI
NEWSAPI_KEY=YOUR_NEWSAPI_KEY_HERE

4. **Run the bot:**:
python news_bot.py

5. **Run the bot:**:
Customization ⚙️
Change categories: Modify the CATEGORIES list in the code.

Adjust posting interval: Edit the interval variable (in seconds).

Switch summarization model: Replace facebook/bart-large-cnn with another Hugging Face model.

Notes ⚠️
The bot uses Twitter API v2 and requires elevated access.

Free NewsAPI has a 100 requests/day limit.

For production, consider adding error handling/logging.

License 📄
MIT License - Open source and free to use.
