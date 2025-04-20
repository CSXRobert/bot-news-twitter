import requests
import tweepy
import time
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Configure Twitter API credentials from environment variables
API_KEY = os.getenv('TWITTER_API_KEY')
API_KEY_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Configure NewsAPI key from environment variable
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

# Validate that all required credentials are present
if not all([API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN, NEWSAPI_KEY]):
    raise ValueError("Missing one or more required API credentials in .env file")

# List of news categories
CATEGORIES = ["business", "technology", "sports", "health", "entertainment", "science"]

# Authenticate with Twitter API
twitter_client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def fetch_news(category):
    try:
        # NewsAPI "Top Headlines" endpoint
        url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWSAPI_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok" and data.get("articles"):
            # Select the first article
            article = data["articles"][0]
            title = article["title"]
            article_url = article["url"]
            description = article.get("description", "Read more about this news.")

            return title, article_url, description
        else:
            print(f"No news found in the {category} category.")
            return None, None, None

    except Exception as e:
        print(f"Error fetching news: {e}")
        return None, None, None

def summarize_news(description):
    try:
        # Generate summary with the model
        summary = summarizer(description, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing news: {e}")
        return None

def post_to_twitter(title, article_url, summary):
    try:
        # Compose the tweet
        tweet = f"📰 {title}\n\n{summary}\n\n{article_url}"

        # Post the tweet
        twitter_client.create_tweet(text=tweet)
        print(f"Successfully posted: {tweet}")

    except Exception as e:
        print(f"Error posting to Twitter: {e}")

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_left = f"{mins:02}:{secs:02}"
        print(f"\rNext post in: {time_left}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r" + " " * 50 + "\r", end="")  # Clear the line

def main():
    interval = 35 * 60  # 35 minutes in seconds
    category_index = 0  # Index to cycle through categories

    while True:
        current_category = CATEGORIES[category_index]
        print(f"\nFetching {current_category} news...")

        title, article_url, description = fetch_news(current_category)

        if title and article_url and description:
            summary = summarize_news(description)
            if summary:
                post_to_twitter(title, article_url, summary)
            else:
                print("Failed to generate news summary.")
        else:
            print("No valid news article found.")

        # Move to the next category
        category_index = (category_index + 1) % len(CATEGORIES)

        # Wait before next post
        countdown_timer(interval)

if __name__ == "__main__":
    main()