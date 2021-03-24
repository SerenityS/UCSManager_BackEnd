import ucsListCrawler

from ucsSql import UcsSql

if __name__ == '__main__':
    UcsSql().resetSql()
    ucsList = ucsListCrawler.runCrawler('r')
    UcsSql().listToSql(ucsList)
