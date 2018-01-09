import feedparser
from datetime import datetime

# RSSのURL
feed_url = 'https://www.nxworld.net/feed/'

# RSSの取得
feed_result = feedparser.parse(feed_url)

for entry in feed_result.entries:
  title = entry.title
  # time.struct_time型のオブジェクトが生成される tuple型
  published = entry.published_parsed
  # datetime.datetime datetimeモジュールの中のdatetime型のオブジェクト
  # (*published[:6]) tuple型をunpackする
  date_time = datetime(*published[:6])
  # datetime型からstringに変換 2017/11/29
  date_str = datetime.strftime(date_time, "%Y/%m/%d")
  link = entry.link

  print(title)
  print(date_str)
  print(link)
