from typing import Annotated, Literal

from annotated_types import Gt

from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green']
    weight: Annotated[float, Gt(0)]
    bazam: dict[str, list[tuple[int, bool, float]]]


print(
    Fruit(
        name='Apple',
        color='red',
        weight=0.5,
        bazam={
            'foobar': [(1, True, 2.5)],
        }
    )
)