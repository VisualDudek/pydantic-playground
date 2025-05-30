from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError
from pprint import pprint


class User(BaseModel):
    id: int
    name: str = 'default_name'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    'id': 'not_a_number',  # This will raise a validation error
    'tastes': {},
}

try:
    user = User(**external_data)
except ValidationError as e:
    pprint(e.errors(), indent=2)