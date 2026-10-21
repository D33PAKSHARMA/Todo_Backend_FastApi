from api.utils.exception_handler import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.routes.todo_routes import router as todo_router
from api.routes.user_routes import router as user_router
from api.config.database import create_db_and_table

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_table()
    yield

app = FastAPI(lifespan=lifespan)
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

@app.get('/')
def root():
    return "Hello from todo app"


@app.get('/health')
def health():
    return {"status": 200, "message": "All is well!"}

# routes
app.include_router(todo_router)
app.include_router(user_router)