import pandas as pd
import praw
from datetime import datetime
from collections import Counter

# add comments to search
# add GUI tkinter
# add password protection
# add password recovery twillio

# reddit API
posts = []
reddit = praw.Reddit(client_id='SWc41yqOyXqkgg', client_secret='4ueEkrOyx2lCGvl0mqcWxfRaSY_rBg', user_agent='WebScrape')
subreddits =['wallstreetbets', 'stocks', 'options', 'investing','thetagang','smallstreetbets']

all_posts = reddit.subreddit('{}'.format(input('What subreddit do you want to scrape?: '))).hot(
    limit=int(input('Sample Size?: ')))

for post in all_posts:
    posts.append([post.title])
posts = pd.DataFrame(posts, columns=['title'])
pd.set_option("display.max_rows", None, "display.max_columns", None)

# excel pull symbols
symbols = pd.read_excel(r'Path to US-Stock-Symbols.xlsx', index_col=None, na_values=['NA'],
                        usecols="A")
data = pd.DataFrame(symbols, columns=['Symbol'])
symbol_list = []
for symbol in data.Symbol:
    symbol_list.append(symbol)

# post titles
post_titles = []
for x in (str(posts.title).split()):
    post_titles.append(x)

post_titles_upper = [x.upper() for x in post_titles]

# post comments


# Find matches between lists
matches = []
for x in post_titles_upper:
    if x in symbol_list:
        matches.append(x)
# Filter out common words
common_words = ['FREE', 'A', 'AN', 'FOR', 'IN', 'TOO', 'TO', 'A', 'BEST', 'FOR', 'IT', 'THE', 'AND', 'HAS', 'IN',
                'ELSE', 'IF', 'S', 'SO', 'HOME', 'HIS', 'MY', 'ELON', 'AT', 'ALL', 'KID', 'DO', 'ARE', "WSB", 'GOOD',
                'GAIN', 'ge']

for i in common_words:
    for x in matches:
        if i == x:
            matches.remove(x)

# Count the matches
key = Counter(matches).keys()
value = Counter(matches).values()
# Zip them into a dictionary
final = dict(zip(key, value))
# Print the results
final_sorted = sorted(final)
for x in final_sorted:
    print(x, final[x])

