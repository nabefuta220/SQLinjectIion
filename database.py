import sqlite3


class database:

    def __init__(self, db: str):
        """
        データベースに接続する

        parameters
        -----
        db : str
            データベースの名前
        """
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    def execute(self, command: str):
        """
        コマンドを実行する

        parameters
        ---
        command : str
            実行するコマンド
        """
        self.cur.execute(command)
        self.con.commit()

    def __del__(self):
        """
        データベースとの接続を切断する
        """
        self.con.close()
