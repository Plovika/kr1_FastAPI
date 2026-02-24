from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.models.models import User, UserAge, Feedback
my_app = FastAPI()

# задание 1.1


@my_app.get('/')
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


# задание 1.2

@my_app.get("/html")
def html_return():
    return FileResponse("app/index.html")

# задание 1.3


class Calculate(BaseModel):
    num1: float
    num2: float


@my_app.post('/calculate')
async def calc(data: Calculate):
    return {"result": data.num1 + data.num2}

# задание 1.4
user = User(name="Демина Екатерина", id=1)


@my_app.get('/users')
async def get_user():
    return user


@my_app.get('/users/input')
async def get_user_input(name: str, id: int):
    return {"имя": name, "id": id}

# задание 1.5


@my_app.post('/user')
async def create_age_user(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult

    }

# задания 2.1
feedbacks: list[Feedback] = []


@my_app.post('/feedback')
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранен."}


# точно ли есть сохранение


@my_app.get("/save_feedbacks")
async def get_feedbacks():
    return feedbacks
