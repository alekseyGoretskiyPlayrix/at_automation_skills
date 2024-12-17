import pytest
import logging


@pytest.fixture(scope='function')
def provide_list():
    return [1, 2, 3, 4, 5]


class TestLogger:

    @pytest.mark.parametrize("value", [
        1,  # Value exists in the list
        2,  # Value exists in the list
        3,  # Value exists in the list
        4,  # Value exists in the list
        5,  # Value exists in the list
    ])
    def test_check_value_in_list(self, provide_list, value):
        logging.info("Starting test_check_value_in_list")
        assert value in provide_list
        logging.info("Finished test_check_value_in_list successfully")

    @pytest.mark.parametrize("value", [
        0,  # Value doesn't exist in the list
        6,  # Value doesn't exist in the list
        -1,  # Value doesn't exist in the list
    ])
    def test_check_value_not_in_list(self, provide_list, value):
        logging.info("Starting test_check_value_not_in_list")
        assert value not in provide_list, f"Value {value} unexpectedly found in the list"
        logging.info("Finished test_check_value_not_in_list successfully")

    def test_check_list_length(self, provide_list):
        logging.info("Starting test_check_list_length")
        assert len(provide_list) == 5
        logging.info("Finished test_check_list_length")
