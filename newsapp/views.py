from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
	newsapi = NewsApiClient(api_key = '5042c08da271412c819bc0ea10d06873')
	top = newsapi.get_top_headlines(sources = 'techcrunch')
	l = top['articles']
	desc = []
	news = []
	img = []
	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)
	return render(request, 'index.html', context={'mylist':mylist})
