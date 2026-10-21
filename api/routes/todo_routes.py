from api.config.authorization import authenticate
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.config.database import get_session
from api.models.todo_model import Todo, TodoReq, TodoRes
from api.models.user_model import User

router = APIRouter(prefix='/todo')

@router.post('/', response_model=TodoRes)
def createTodo(todo_in: TodoReq, session: Session=Depends(get_session)):
    todo = Todo(
        task=todo_in.task,
        desc=todo_in.desc
    )
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo
    
@router.get('/', response_model=list[TodoRes])
def getAllTodo(session: Session=Depends(get_session), user: User = Depends(authenticate)):
    print('user>>>',user)
    todos = session.exec(select(Todo)).all()
    return todos
    

