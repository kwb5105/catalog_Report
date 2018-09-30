#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from catalogdb import get_top_articles, get_top_authors, get_top_errors

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Catalog Report</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.ArticleType { color: #000}
      em.AuthorType { color: #000 }
    </style>
  </head>
  <body>
    %s
  </body>
</html>
'''

# HTML template for an individual article
ARTICLES = '''\
    <div class=post><em class=ArticleType>Article: %s</em><br>Views: %s</div>
'''
# HTML template for an individual author
AUTHORS = '''\
    <div class=post><em class=AuthorType>Author: %s</em><br>Views: %s</div>
'''
# HTML template for an error result lists
ERRORLOG = '''\
    <div class=post><em class=AuthorType>Day: %s</em><br>Error Percent: %s</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Top Article Report'''
  results = "<h1>Top Articles</h1>"
  results = results + "".join(ARTICLES % (article, views) for views, article in get_top_articles())
  results = results + "<h1>Top Authors</h1>"
  results = results + "".join(AUTHORS % (author, views) for views, author in get_top_authors())
  results = results + "<h1>Days with more than 1 percent request errors</h1>"
  results = results + "".join(ERRORLOG % (date, failedPercentage) for failedPercentage, date in get_top_errors())
  html = HTML_WRAP % results
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)