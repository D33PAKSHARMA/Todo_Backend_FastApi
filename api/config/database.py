from pathlib import Path
from sqlmodel import create_engine, Session, SQLModel

# BASE_DIR = Path(__file__).resolve().parent.parent.parent
sqlite_file_name = "database.db"
sqlite_db_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_db_url, connect_args={"check_same_thread": False})

def create_db_and_table():
    from api.models import user_model, todo_model
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
    

      