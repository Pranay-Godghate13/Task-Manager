import sqlite3
a=[]
def add_task_to_db(task: str,due_date: str):
    a.append({"task":task,"date":due_date})
    #print("Task completed sucessfully.")

def list_task():
    for i,elem in enumerate(a):
        print(f"Task is : {elem['task']} | Due date is : {elem['date']}")

def delete_task(task_id: int):
    a.pop(task_id-1)
    #print("Deleted successfully.")



