from enum import Enum

class Mode(str, Enum):
    READ = 'r'
    WRITE = 'w'


def with_enum(mode: Mode):
    if mode == Mode.READ:
        return 'Reading mode'
    elif mode == Mode.WRITE:
        return 'Writing mode'
    else:
        raise ValueError(f'Unknown mode: {mode}')
    

from typing import Literal
# Lightweight alternative to Enum

def with_literal(mode: Literal['r', 'w']):
    if mode == 'r':
        return 'Reading mode'
    elif mode == 'w':
        return 'Writing mode'
    else:
        raise ValueError(f'Unknown mode: {mode}')