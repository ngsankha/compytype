import pytest
from typing import Literal

@pytest.mark.mypy_testing
def test_annotated_add():
    op1: Literal[3] = 3
    op2: Literal[4] = 4
    reveal_type(op1 + op2) # N: Revealed type is 'Literal[7]'
