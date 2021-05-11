from unittest import TestCase
from unittest.mock import patch


class TestExampleLambda(TestCase):
    def setUp(self):
        self.addCleanup(patch.stopall)

