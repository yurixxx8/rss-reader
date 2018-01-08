import feedparser

# RSSのURL
feed_url = 'https://www.nxworld.net/feed/'

# RSSの取得
feed_result = feedparser.parse(feed_url)

for entry in feed_result.entries:
  title = entry.title
  link = entry.link
  print(title)
  print(link)