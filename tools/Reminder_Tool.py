
from datetime import datetime
import sqlite3
import smtplib
from crew.ai import tools

from datetime import datetime

@tools("Check reminder tool")
def check_reminders():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    now_date = datetime.now().strftime("%Y-%m-%d")   
    now_time = datetime.now().strftime("%H:%M")      

    cursor.execute(
        "SELECT description FROM tasks WHERE due_date = ? AND reminder_time = ?",
        (now_date, now_time)
    )
    reminders = cursor.fetchall()
    conn.close()
    return reminders

