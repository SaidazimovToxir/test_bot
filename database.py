import mysql.connector
import config

MYSQL_HOST = config.MYSQL_HOST
MYSQL_USER = config.MYSQL_USER
MYSQL_PASSWORD = config.MYSQL_PASSWORD


class Database:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD
        )
        
        self.cursor = self.mydb.cursor()
        self.__createDatabase()
        self.__createTable()
        
    def __createDatabase(self):
        create_database = 'CREATE DATABASE IF NOT EXISTS TEST_BOT;'
        use_query = 'USE TEST_BOT;'
        self.cursor.execute(create_database)
        self.cursor.execute(use_query)
        
    def __createTable(self):
        create_table = """ 
            CREATE TABLE IF NOT EXISTS test_bot(
                NAME VARCHAR(256),
                USERNAME VARCHAR(256),
                USER_ID VARCHAR(256) UNIQUE,
                CREATED_DT DATETIME DEFAULT NOW()
            )
        """
        self.cursor.execute(create_table)
        
    def add_users(self, name: str, username: str, user_id: str):
        select_query = 'SELECT USER_ID FROM test_bot;'
        
        self.cursor.execute(select_query)
        data = self.cursor.fetchall()
        
        user_exists = any(i[0] == str(user_id) for i in data)
        
        if not user_exists:
            add_users = "INSERT INTO test_bot(NAME, USERNAME, USER_ID) VALUES (%s, %s, %s);"
            values = (name, username, user_id)
            self.cursor.execute(add_users, values)
            self.mydb.commit()
            return "Foydalanuvchi yaratildi"
        
        return "Foydalanuvchi mavjud;"
    
# db = Database()
# print(db.add_users("jalolov.de ☘️", "jalolv_de","5300379153"))

# db.send_all_users_massage()        