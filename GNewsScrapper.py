from gnews import GNews
import json
google_news = GNews(end_date=(2015, 12, 31), start_date=(2015, 1, 1))
business_news = google_news.get_news_by_topic('BUSINESS')
out_file = open("data_2015.json", "w")
json.dump(business_news, out_file, indent=6)
out_file.close()