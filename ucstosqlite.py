import sqlite3

class UcsSql:
    def __init__(self):
        self.conn = sqlite3.connect('ucs_list.db')
        self.cur = self.conn.cursor()

    def listToSql(self, ucsList):
        for ucs_data in ucsList:
            try:
                self.cur.executemany(
                    'INSERT INTO ucsList VALUES (?, ?, ?, ?, ?)',
                    [ucs_data]
                )
            except:
                continue
        self.conn.commit()
        self.conn.close()

    def resetSql(self):
        self.conn.execute('DELETE FROM ucsList')
        self.conn.commit()
        self.conn.close()
