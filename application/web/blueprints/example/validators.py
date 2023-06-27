from pydantic import BaseModel, validator
from typing import List


class ExampleModel(BaseModel):
    name: str
    grade: str
    roll: int
    email: str
    phone: int
    subjects: List[str]
    friends: List[str]

    @validator("name")
    def name_must_contain_space(cls, name):
        if " " not in name:
            raise ValueError("must contain a space")
        return name.title()

    @validator("phone")
    def phone_number_len(cls, phone):
        if len(str(phone)) != 10:
            raise ValueError("Phone number must contain 10 digits")
        return phone