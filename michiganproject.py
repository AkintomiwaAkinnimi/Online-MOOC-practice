
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(text):
    new_str = ""
    for char in text:
        if char not in punctuation_chars:
            new_str += char
    return new_str

def get_neg(tweet):
    negative_words = []
    with open("negative_words.txt") as neg_f:
        for lin in neg_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    new_tweet = strip_punctuation(tweet).lower()
    words_in_tweet = new_tweet.split()
    num_of_neg_words_per_tweet = 0
    for word in words_in_tweet:
        if word in negative_words:
            num_of_neg_words_per_tweet += 1
    return num_of_neg_words_per_tweet

def get_pos(tweet):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    num_of_pos_words_per_tweet = 0
    new_tweet = strip_punctuation(tweet).lower()
    words_in_tweet = new_tweet.split()
    for word in words_in_tweet:
        if word in positive_words:
            num_of_pos_words_per_tweet += 1
    return num_of_pos_words_per_tweet

# Read the input CSV file
with open("project_twitter_data.csv") as file:
    lines = file.readlines()

# Prepare to write the output CSV file
fieldnames = ["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"]
with open("resulting_data.csv", "w") as file2:
    file2.write(', '.join(fieldnames) + '\n')
    for line in lines[1:]:  # Skip the header
        row = line.strip().split(",")
        tweet = row[0]
        retweets = int(row[1])
        replies = int(row[2])
        pos_score = get_pos(tweet)
        neg_score = get_neg(tweet)
        net_score = pos_score - neg_score
        file2.write(f"{retweets},{replies},{pos_score},{neg_score},{net_score}\n")
 