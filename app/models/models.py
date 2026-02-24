import re
from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    name: str
    id: int


class UserAge(BaseModel):
    name: str
    age: int

# задание 2.1


class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=2, max_length=50)

    @field_validator("message")
    @classmethod
    def check_bad_words(cls, v: str) -> str:
        # "кринж", "рофл", "вайб" и их формы
        pattern = r"(кринж\w*|рофл\w*|вайб\w*)"
        if re.search(pattern, v, flags=re.IGNORECASE):
            raise ValueError("Использование недопустимых слов")
        return v



