
from database import database

class cliant1(database):
    def __init__(self,db: str ,table:str):
        """
        テーブルを作成しする

        parameters
        ---
        db : str
            データベース名
        table : str
            デーブル名
        """

        super().__init__(db)
        self.table=table
        self.execute(f'create table if not exists {table} (id integer primary key autoincrement,user char(10) not null, password char(40) not null); ')


    def register(self,name:str=None,password:str=None):
        """
        登録する

        parameters
        ---
        name : str ,default = None
            登録するユーザー名
        password : str , default = None
            パスワード
        returns
        ---
        id : int
            登録したユーザーのid
        """
        if name is None:
            name=input('name> ')
        if password is None:
            password = input('password> ')
        self.execute(f'insert into {self.table}(user,password) values("{name}","{password}")')
        self.execute(f'select id from {self.table} where user = "{name}"')
        for i in self.cur:
            res,=i
        print(f'registered id: {res}')
        return res
    def login(self, name: str = None, password: str = None):
        """
        ログイン

        parameters
        ---
        name : str ,default = None
            ユーザー名
        password : str , default = None
            パスワード
        returns
        ---
        id : int
            ログインユーザーのid
            そのようなユーザーがいなければ、0を返す
        """
        res=0
        if name is None:
            name = input('name> ')
        if password is None:
            password = input('password> ')
        self.execute(f'select id from {self.table} where user = "{name}" and password = "{password}"')
        for i in self.cur:
            res, = i
        if res == 0:
            print('login failed!')
        else:
            print(f'logined id: {res}')
        return res
    def show(self):
        """
        現在のデータベースの情報を出力する
        """
        self.execute(f'select * from {self.table}')
        for i in self.cur:
            print(i)


if __name__ == '__main__':
    cliant = cliant1('cliant.db', 'cliant1')
    cliant.login()
    cliant.show()

