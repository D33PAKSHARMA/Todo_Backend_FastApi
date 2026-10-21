from sqlmodel import SQLModel, Field

class TodoBase(SQLModel):
    task: str
    desc: str
    is_completed: bool = Field(default=False)

class Todo(TodoBase, table=True): # db table
    id: int | None = Field(default=None, primary_key=True)
    
class TodoReq(TodoBase):
    task: str
    desc: str
    
class TodoRes(TodoBase):
    id: int