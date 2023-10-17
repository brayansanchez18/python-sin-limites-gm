def ListarTerminos(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

ListarTerminos(ide='ide')
ListarTerminos(dbms= 'databasems')