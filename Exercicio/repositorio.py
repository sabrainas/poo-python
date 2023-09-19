class Repositorio:
    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('conectei ao banco de dados {}'.format(connection))
        print('fazendo um SELECT * FROM...')
        db_connection.desconectar()
    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('conectei ao banco {}'.format(connection))
        print('fazendo um Insert Values...')
        db_connection.desconectar()