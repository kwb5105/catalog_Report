# Database code for the DB catalog.

import psycopg2
DBNAME = "news"


def get_top_articles():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(log.id) as Views, articles.title \
    from log left join articles on \
    (log.path like CONCAT('%', articles.slug, '%')) \
    WHERE status = '200 OK' and title != '' GROUP BY articles.title \
    order by count(log.id) desc LIMIT 3")
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(log.id) as Views, authors.name \
    from log left join articles on (log.path like \
    CONCAT('%', articles.slug, '%')) inner join authors \
    on (authors.id = articles.author) WHERE status = '200 OK' \
    and title != '' GROUP BY authors.name \
    order by count(log.id) desc")
    authors = c.fetchall()
    db.close()
    return authors


def get_top_errors():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select round((round\
    (failedCount.count::decimal,2)/round\
    (logDateCount.count::decimal,2) *100)::decimal,2) \
    as failedPercentage, failedCount.time \
    from failedCount join logDateCount on \
    (failedCount.time = logDateCount.time) \
    where round((round(failedCount.count::decimal,2)\
    /round(logDateCount.count::decimal,2) *100)::decimal,2) > \
    1 order by failedPercentage desc")
    topErrors = c.fetchall()
    db.close()
    return topErrors
