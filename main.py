from dotenv import load_dotenv
from crew import task_crew

load_dotenv()

def run(task:str,date:str,time:str,status:str):
    result=task_crew.kickoff(inputs={"task":task,"date":date,"time":time,"status":status})
    print(result)

if __name__=="__main__":
    run(task="Plan an field trip.",date="03-01-2026",time="12:00",status="Scheduled")