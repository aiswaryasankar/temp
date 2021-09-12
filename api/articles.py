from http.server import BaseHTTPRequestHandler
import newspaper
from newspaper import news_pool, Article
from logtail import LogtailHandler
import logging
import time

handler = LogtailHandler(source_token=process.env.NEXT_PUBLIC_LOGTAIL_SOURCE_TOKEN)

logger = logging.getLogger(__name__)
logger.handlers = []
logger.addHandler(handler)

logger.info('logtail is ready')


class handler(BaseHTTPRequestHandler):

    news_sources = [
      "http://slate.com",
      "http://techcrunch.com",
      "http://espn.com",
      "https://www.economist.com",
      "https://cnn.com",
      "https://www.nytimes.com/",
      "https://www.wsj.com/",
      "https://www.politico.com/",
      "https://www.foxnews.com/",
      "https://www.bbc.com/news",
      "https://www.washingtonpost.com/",
      "https://www.washingtonexaminer.com/",
      "https://www.breitbart.com/",
      "https://www.washingtontimes.com/",
      "https://thehill.com/",
      "https://www.vox.com/",
      "https://fivethirtyeight.com/",
      "https://nypost.com/",
    ]

    def populateArticles():
      """
      This function will read in the entire feedlist, go through the entire build process and then emit metrics regarding how many articles were parsed, the length of each article and the time taken for each of the articles to be pulled.
      """
      global news_sources
      startTime = time.time()

      newspapers = []
      for source in news_sources:
        newspapers.append(newspaper.build(source))


      news_pool.set(newspapers, threads_per_source=2)
      news_pool.join()
      endTime = time.time()
      logger.info("Time taken to read articles %d", endTime - startTime)

      for paper in newspapers:
        logger.info("Number of articles in the paper")
        logger.info(len(paper.articles))

        for article in paper:
          logger.info(article.text)
          if len(article.text) <= 5:
            logger.warn("Article has less than 5 words")





