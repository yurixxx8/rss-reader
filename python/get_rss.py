import feedparser
import datetime

# RSSのURL
feed_url = 'https://www.nxworld.net/feed/'

# RSSの取得
feed_result = feedparser.parse(feed_url)

for entry in feed_result.entries:
  title = entry.title
  # time.struct_time型のオブジェクトが生成される
  published = entry.published_parsed
  # tuple型をunpack
  # date_time datetime型
  date_time = datetime.datetime(*published[:6])
  # datetime型からstringに変換 2017/11/29
  date_str = datetime.datetime.strftime(date_time, "%Y/%m/%d")
  link = entry.link

  print(title)
  print(date_str)
  print(link)