import logging
import sqlite3


DB_URL = '/home/user/Documents/python-training/todo-api/mydb2'

logger = logging.getLogger('todosqslite')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('todos.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

class SqliteCtxMgr():
    
    def __init__(self,query=None):
        self.db = sqlite3.connect(DB_URL)
        self.cursor = self.db.cursor()
        self.query = query
        logger.error()

    def __enter__(self):
        if self.query:
            self.cursor.execute(self.query)
        return self.cursor
    
    def __exit__(self, exc_typ, exc_val, exc_tb):
        self.db.commit()
        self.db.close()

# Insertar un to-do
def insert_todo(title, description):
    logger.info("Insertando to-do")
    query = "insert into todos(title,description,state) values ('%s','%s','new')" % (title,description)
    with SqliteCtxMgr(query):
        return "Todo creado"

def get_todo(id):
    logger.info("Getting to-do")
    query = """select * from todos where id = """ + str(id)
    with SqliteCtxMgr(query) as cursor:
        data = cursor.fetchall()
        return data

# Listar todos los to-do
def list_todos():
    logger.info("List to-do")
    query = '''select * from todos'''
    with SqliteCtxMgr(query) as cursor:
        dataset = cursor.fetchall()
        return dataset

def update_todo(todo_id, title=None, description=None):
    logger.info("Update to-do")
    query = "update todos set title='"+title+"', description='"+description+"' where id = " + str(todo_id)
    with SqliteCtxMgr(query):
        return "Todo updated"

def delete_todo(todo_id):
    logger.info("Delete to-do")
    query = '''delete from todos where id = ''' + str(todo_id)
    with SqliteCtxMgr(query):
        return "Todo deleted"