from textblob import TextBlob
import sys


def analyze_sentiment(text):
    # Initialize TextBlob's polarity scores and subjectivity
    blob = TextBlob(text)
    polarity, subjectivity = blob.polarity, blob.subjectivity

    if polarity > 0.05:
        sentiment = "Positive"
    elif polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity, subjectivity

def analyze_reviews_in_file(file_path, num_reviews):
    with open(file_path, 'r') as file:
        reviews = file.readlines()[:num_reviews]
        
        for idx, review in enumerate(reviews, start=1):
            sentiment, polarity, subjectivity = analyze_sentiment(review.strip())
            print(f"Review {idx}:")
            print(f"Sentiment: {sentiment}")
            print(f"Polarity: {polarity}")
            print(f"Subjectivity: {subjectivity}")
            print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_file_path = sys.argv[1]
        num_reviews = 20  # Specify the number of reviews to analyze
        analyze_reviews_in_file(text_file_path, num_reviews)
    else:
        print("Please provide the path to a text file as an argument.")

