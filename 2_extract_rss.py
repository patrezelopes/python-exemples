############
#
# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.
#
############

from xml.etree.ElementTree import parse
from urllib.request import urlopen

google_news_url = "https://news.google.com/news/rss"


def get_headlines(rss_url):
    url = urlopen(rss_url)
    xmldoc = parse(url)
    title = []
    for item in xmldoc.iterfind('channel/item'):
        title.append(item.findtext('title'))
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    return title


print(get_headlines(google_news_url))
