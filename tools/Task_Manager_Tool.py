import sqlite3
from crew.ai import tools

def init_db():
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT NOT NULL,
                   date TEXT NOT NULL,
                   reminder_time TEXT NOT NULL,
                   status TEXT DEFAULT 'Pending')
""")
    conn.commit()
    conn.close()

@tools("Add tasks to database")
def add_task_to_db(task: str,due_date: str,reminder_time):
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tasks(task,date,reminder_time) values(?,?,?)",(task,due_date,reminder_time))
    conn.commit()
    conn.close()

@tools("List all the tasks")
def list_task():
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        print(f"{row[0]}. Task: {row[1]} | Date: {row[2]}")
    conn.close()

@tools("Delete tasks")
def delete_task(task_id: int):
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks where id=?",(task_id,))
    conn.commit()
    conn.close()

#init_db()

# Usage
#add_task_to_db("Wake me up at 6 AM", "31/12/2025")
#delete_task(2)
#list_task()
#delete_task(1)
#list_task()


