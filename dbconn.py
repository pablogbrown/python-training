import sqlite3


# crear una db
db = sqlite3.connect('/home/user/Documents/python-training/todo-api/mydb2')
# Crear una tabla "todos"
cursor = db.cursor()
cursor.execute('''
    create table todos(id INTEGER PRIMARY KEY, title TEXT,
                        description TEXT, state TEXT)
''')
db.commit()
db.close()