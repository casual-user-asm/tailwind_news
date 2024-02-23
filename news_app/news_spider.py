import scrapy

class Unian(scrapy.Spider):
    name = 'pravda'
    start_urls = [
        "https://www.unian.ua/detail/main_news",
        "https://nv.ua/",
        "https://ua.korrespondent.net/",
        "https://tsn.ua/",
        "https://www.pravda.com.ua/news/",
        "https://www.bbc.com/news",
        "https://edition.cnn.com/world",
        "https://www.dw.com/en/top-stories/s-9097",
        "https://www.euronews.com/",
        "https://www.nytimes.com/trending/",
    ]

    def parse(self, response):
        counter = 0
        if "https://www.unian.ua/detail/main_news" in response.url:
            for h3 in response.xpath('//h3/a'):
                link = h3.xpath('@href').get().strip()
                text = h3.xpath('text()').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "Уніан",
                    "source_country": "ukrainian",
                }


                counter += 1
                if counter >= 5:
                    break
        elif "https://nv.ua/" in response.url:

            feed_items = response.css('div.tab.active .feed-item')

            for item in feed_items:
                link = item.css('a.feed-item-title::attr(href)').get().strip()
                title = item.css('a.feed-item-title::text').get().strip()
                yield {
                    "title": title,
                    "url": link,
                    "source": "НВ",
                    "source_country": "ukrainian",
                }
                counter += 1
                if counter >= 5:
                    break
        elif "https://ua.korrespondent.net/" in response.url:
            for article in response.css('div.article__title'):
                link = article.css('a::attr(href)').get().strip()
                text = article.css('a::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "Кореспондент",
                    "source_country": "ukrainian",
                }

                counter += 1
                if counter >= 5:
                    break
        elif "https://tsn.ua/" in response.url:
            for article in response.css('article.c-card'):
                link = article.css('h3.c-card__title a::attr(href)').get().strip()
                text = article.css('h3.c-card__title a::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "ТСН",
                    "source_country": "ukrainian",
                }

                counter += 1
                if counter >= 5:
                    break
        elif "https://www.pravda.com.ua/news/" in response.url:
            for article in response.css('div.article_news_bold'):
                link = "https://www.pravda.com.ua" + article.css('a::attr(href)').get().strip()
                text = article.css('a::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "Українська правда",
                    "source_country": "ukrainian",
                }

                counter += 1
                if counter >= 5:
                    break
        elif "https://www.bbc.com/news" in response.url:
            for article in response.css('div.gs-c-promo-body'):
                link = "https://www.bbc.com" + article.css('a::attr(href)').get().strip()
                text = article.css('h3::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "BBC",
                    "source_country": "foreign",
                }

                counter += 1
                if counter >= 5:
                    break
        elif "https://edition.cnn.com/world" in response.url:
            for article in response.css('div.container__item--type-media-image'):
                link = "https://edition.cnn.com" + article.css('a::attr(href)').get().strip()
                text = article.css('span::text').get().strip()
                if text:
                    yield {
                        "title": text,
                        "url": link,
                        "source": "CNN",
                        "source_country": "foreign",
                    }
                counter += 1
                if counter >= 6:
                    break
        elif "https://www.dw.com/en/top-stories/s-9097" in response.url:
            for article in response.css('h3.sc-iJfdHH'):
                link = "https://www.dw.com" + article.css('a::attr(href)').get().strip()
                text = article.css('span::text').get()
                if text:
                    yield {
                        "title": text,
                        "url": link,
                        "source": "Deutsche Welle",
                        "source_country": "foreign",
                    }
                counter += 1
                if counter >= 6:
                    break
        elif "https://www.euronews.com/" in response.url:
            for article in response.css('div.c-most-viewed__article'):
                link = "https://www.euronews.com" + article.css('a::attr(href)').get().strip()
                text = article.css('a::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "EuroNews",
                    "source_country": "foreign",
                }

                counter += 1
                if counter >= 5:
                    break
        elif "https://www.nytimes.com/trending/" in response.url:
            for article in response.css('li.css-1iski2w'):
                link = article.css('a::attr(href)').get().strip()
                text = article.css('h1::text').get().strip()
                yield {
                    "title": text,
                    "url": link,
                    "source": "NewYork Times",
                    "source_country": "foreign",
                }
                
                counter += 1
                if counter >= 5:
                    break
        
