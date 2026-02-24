from fastapi import FastAPI

mymy = FastAPI()


@mymy.get("/")
async def root():
    return {"message": "Добро пожаловать в мое приложение FastAPI!"}


# новый маршрут
@mymy.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}