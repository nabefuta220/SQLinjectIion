from pydoc import cli
from sys import argv

from cliant1 import cliant1

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

