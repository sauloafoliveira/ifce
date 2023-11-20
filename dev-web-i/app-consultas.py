import sqlite3

conexao = sqlite3.connect('world.db')
cur = conexao.cursor()



query = '''
    SELECT * 
    FROM City 
    WHERE countrycode = 'BRA' and district LIKE 'Cear%';
'''
cur.execute( query )
result = list( cur )

for cidade in result:
    print(cidade)   

conexao.close()
