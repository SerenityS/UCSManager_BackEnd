import ucsListCrawler

from ucsSql import UcsSql

if __name__ == '__main__':
    ucsList = ucsListCrawler.runCrawler('u')
    UcsSql().listToSql(ucsList)
