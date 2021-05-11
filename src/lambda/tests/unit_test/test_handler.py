from unittest.mock import patch
from handlers.example_lambda import handler

from . import TestExampleLambda


class TestHandler(TestExampleLambda):
    def setUp(self):
        super().setUp()

    def test_calls_print_with_hello_world(self):
        mock_print = patch("builtins.print").start()
        expected_message = "hello world"
        event = None
        context = None

        handler(event, context)

        mock_print.assert_called_once_with(expected_message)
