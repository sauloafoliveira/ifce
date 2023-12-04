import mysql.connector
import random

INSERT_CIDADE = '''
    INSERT INTO City VALUES (?, ?, 'BRA', 'Ceará', ?)
'''

UPDATE_CIDADE = '''
    UPDATE City SET 
    Name = %s,
    Population = %s
    WHERE Id = %s
'''

DELETE_CIDADE = '''
    DELETE FROM City WHERE Id = %s
'''

SELECT_CIDADES = '''
    SELECT * FROM City WHERE District LIKE 'Ceará'
'''

SELECT_CIDADE_POR_ID = '''
    SELECT Id FROM City WHERE Name = %s
'''

def _connect():

    try:
            

        con = mysql.connector.connect(user='sauloafoliveira', 
                                    password='123456',
                                    host='127.0.0.1',
                                    database='world')
        
        if con.is_connected():
            cur = con.cursor()
            return con, cur
    except Exception as e:
        print(e)

    return None, None


def listar_todas():
    con, cur = _connect()

    result = None
    if con and cur:
        cur.execute( SELECT_CIDADES )
       
        columns = [column[0] for column in cur.description]
        result = [dict(zip(columns, row)) for row in list(cur)]

        con.close()

    return result


def buscar_id(nome):
    con, cur = _connect()

    if con and cur:
        cur.execute( SELECT_CIDADE_POR_ID, (nome, ))
        result = list( cur )
        con.close()
        return None if len(result) < 1 else result[0]

    return None



def inserir_cidade(nome, populacao):
    con, cur = _connect()

    if con and cur:
        cur.execute( INSERT_CIDADE, (nome, populacao, ) )
        con.commit()
        con.close()
    
def alterar_cidade(nome, populacao):

    id = buscar_id(nome)

    if id:
        con, cur = _connect()
        cur.execute( UPDATE_CIDADE, (id, nome, populacao, ) )
        con.commit()
        con.close()

def deletar_cidade(nome):
    id = buscar_id(nome)

    if id:
        con, cur = _connect()
        cur.execute( DELETE_CIDADE, (id, ) )
        con.commit()
        con.close()


