import ucs_crawler

from ucstosqlite import UcsSql

if __name__ == '__main__':
    ucsList = ucs_crawler.runCrawler('u')
    UcsSql().listToSql(ucsList)
