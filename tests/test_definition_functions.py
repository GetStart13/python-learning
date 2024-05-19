from unittest import TestCase

from python_learning.example.definition_functions import *


class Test(TestCase):
    def test_function(self):
        function("x", "y", "z", "a", "b", "c", key="key", word="word")
        # ** 表示拆包
        function("x", "y", "z", "a", "b", "c", **{"key": "key", "word": "word"})
        self.assertTrue(True)

    def test_unpacking(self):
        unpacking()
        self.assertTrue(True)

    def test_combine_positional_and_keyword_arguments(self):
        combine_positional_and_keyword_arguments("name", **{"name": "some"})
        self.assertTrue(True)

    def test_special_parameters(self):
        special_parameters("one", "two", "three", pos_or_kwd2="four", kwd1="key1", kwd2="key2")
        self.assertTrue(True)

    def test_lambda_expression(self):
        result = lambda_expression(3)
        self.assertEqual(13, result)

    def test_annotation(self):
        result = annotations(1, "注解")
        print(result)
        self.assertTrue(True)
