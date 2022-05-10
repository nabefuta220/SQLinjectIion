
from sys import argv

from cliant1 import cliant1
import argparse

def get_args():
    """
    引数を取得する

    Returns
    ---
    file : str
        データを追加するデータベースファイル名
    table : str 
        データを追加するテーブル名
    """
    parser=argparse.ArgumentParser()

    parser.add_argument('file',help='データを追加するデータベースファイル名')
    parser.add_argument('table', help='データを追加するテーブル名')

    args=parser.parse_args()
    return args.file,args.table
if __name__ =='__main__':
    file=argv[1]
    table = argv[2]
    db=cliant1(file,table)
    names = ['Nabe', 'Chris', 'Pat', 'Alex','Dana', 'Hunter',
             'Jamie', 'Morgan', 'Robin', 'Ronnie', 'Shannon', 'Terry']
	
    passwords = [
        'MCJ6er8n','fLrtPU5X','RsjR48f4','VXHEC6Vw','A7intDww','3rXvY84a','L7sHnCkR','fDcahwR7','nWXW6VWM','cvEx4UAy']
    for (name,password) in zip(names,passwords):
        db.register(name,password)

    db.show()

