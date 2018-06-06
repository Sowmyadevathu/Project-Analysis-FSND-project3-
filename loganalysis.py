#!/usr/bin/env python3
import datetime
import psycopg2


DBNAME = "news"


def popular_articles():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select articles.title,count(log.path) as views
        from log join articles
        on articles.slug = substring(log.path from 10)
        group by articles.title
        order by views desc limit 3;

          """
    c.execute(query)
    result = c.fetchall()
    print("\nMost popular three articles all the time ")
    for row in result:
        print("\n {:^10} -  {:^10}" .format(row[0], row[1]))
    db.close()


def popular_authors():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select authors.name,count(log.path) as views
        from log join articles
        on articles.slug = substring(log.path from 10)
        join authors
        on authors.id=articles.author where status = '200 OK'
        group by authors.name
        order by views desc;

        """
    c.execute(query)
    result = c.fetchall()
    print("\nMost popular article authors all the time")
    for row in result:
        print("\n {:^10} - {:^10}" .format(row[0], row[1]))
    db.close()


def errorpercentage_day():

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select a.date,((sum(a.errorcount)/sum(a.count))*100)
        as errorpercentage
        from
        (select date(time) as date,count(log.path) ,
        count(case when status='404 NOT FOUND' then log.path else null end)
        as errorcount
        from log group by date(time)) a
        group by a.date having  ((sum(a.errorcount)/sum(a.count))*100)>1;

        """
    c.execute(query)
    result = c.fetchall()
    print("\nDay more then 1% requests lead to errors")
    for row in result:
        date = row[0].strftime('%b %d, %Y')
        error = round(row[1], 2)
        print(" {} - {}%".format(date, error))
    db.close()


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    errorpercentage_day()
