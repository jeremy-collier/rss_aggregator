from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as BSoup
# Create your views here.

def index(request):
    context = {
        'spd_news':spd_news,
    }
    return render(request, 'news/index.html', context)

# news from spdstorystudios.com
spd_r = requests.get('https://www.spdstorystudio.com/')
spd_soup = BSoup(spd_r.content, 'html5lib')
spd_headings = spd_soup.find_all('h2')
spd_news = []

for article in spd_headings:
    spd_news.append(article.text)
