from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class Todo(BaseModel):
    task: str
    done: bool
    deadline: Optional[date]
    
taskList = []

@app.post('/addtask')
def add(todo: Todo):
    try:
        taskList.append(todo)
        return {"status": "New task added successfuly!"}
    except:
        return {"status": "error adding task!"}


@app.post('/listtasks')
def listtasks(option: int = 1):
    if (option == 1):
        if (len(taskList) == 0):
            return {"status; ": "taskList is empty!"}
        else:
            return taskList
    elif (option == 2):
        return list(filter(lambda x: x.done == False, taskList))
    elif (option == 3):
        return list(filter(lambda x: x.done == True, taskList))


@app.get('/listtaskbyid')
def listtaskbyid(id: int):
    try:
        return taskList[id]
    except:
        return {"status: ": "taks not found!"}
        
    
@app.post('/changestatus')
def changestatus(id: int):
    try:
        taskList[id].done = not taskList[id].done
        return {"status: ": "task status changed!"}
    except:
        return {"status: ": "error trying to change tasks status!"}


@app.post('/deltask')
def deltask(id: int):
    try:
        del taskList[id]
        return {"status:": "task has been deleted!"}
    except:
        return {"status:": "task could not be deleted or not found!"}
