import pytest
import os
import pathlib

@pytest.fixture(scope="package", autouse=True)
def set_wdir():
    os.chdir(pathlib.Path(__file__).parent)
