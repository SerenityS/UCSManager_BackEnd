import sqlite3

class UcsSql:
    def __init__(self):
        self.conn = sqlite3.connect('ucs_list.db')
        self.cur = self.conn.cursor()

    def findFromSql(self, song_title, song_lv, step_maker):
        self.cur.execute(f"SELECT * FROM ucsList WHERE (songTitle_ko LIKE '%{song_title}%' OR songTitle_en LIKE '%{song_title}%') AND songLv LIKE '%{song_lv}%' AND stepMaker LIKE '%{step_maker}%';")
        return self.cur.fetchall()

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

