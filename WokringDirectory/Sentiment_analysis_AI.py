import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the vader_lexicon resource if it's not already downloaded
nltk.download('vader_lexicon')

# Function to perform sentiment analysis
def perform_sentiment_analysis(input_file_path, output_file_path):
    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Read the content of the input file
    with open(input_file_path, 'r') as file:
        text = file.read()

    # Analyze sentiment
    sentiment = sia.polarity_scores(text)

    # Prepare the sentiment summary
    summary = (f"Overall Sentiments:\n"
               f"Positive: {sentiment['pos']:.2f}\n"
               f"Neutral: {sentiment['neu']:.2f}\n"
               f"Negative: {sentiment['neg']:.2f}")

    # Write the sentiment summary to the output file
    with open(output_file_path, 'w') as file:
        file.write(summary)

# Example usage
input_file_path = 'Feedback.txt'  # Replace with your input file name and path
output_file_path = 'sentiment_output.txt'  # Replace with your desired output file name and path

# Perform sentiment analysis
perform_sentiment_analysis(input_file_path, output_file_path)
