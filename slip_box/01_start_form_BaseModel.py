from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = 'default_name'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    'id': 123,
    'signup_ts': '2023-10-01T12:00:00',
    'tastes': {
        'pizza': 5,
        b'sushi': 3, # key bytes will be converted to str
        'burger': '4', # value string will be converted to PositiveInt
    },
}


user = User(**external_data)
print(user.id)
print(user.model_dump())
print(user.model_dump_json(indent=2))