import os

import pytest
import logging

from src.math_operations import MathOperations


@pytest.fixture(scope="function")
def math_ops():
    """Fixture to create an instance of MathOperations."""
    return MathOperations()


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    log_dir = 'tests/logs'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f'{log_dir}/test.log', mode='a')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
