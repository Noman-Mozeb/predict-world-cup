import requests
import xml.etree.ElementTree as ET

def pull_rss_news_stream():
    rss_url = "https://google.com"
    news_items = []
    try:
        response = requests.get(rss_url, timeout=5)
        root = ET.fromstring(response.content)
        for item in root.findall('.//item')[:3]:
            news_items.append({
                'title': item.find('title').text,
                'link': item.find('link').text,
                'date': item.find('pubDate').text
            })
    except Exception:
        pass
    return news_items
