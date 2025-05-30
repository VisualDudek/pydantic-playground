from typing import Annotated

Age = Annotated[int, 'Age in years']

def set_age(age: Age) -> None:
    ...

def set_age(age: int): ... # No way to say "must be >= 0" in type hints

NonNegativeAge = Annotated[int, 'Age in years', 'Must be >= 0']


def set_age(age: NonNegativeAge): ... 
# This lets static tools or lib enforce or interpret that the age must be non-negative,