from unittest import TestCase

from python_learning.modules import module_main


class Test(TestCase):
    def test_module_main(self):
        module_main.module_main()
        self.assertTrue(True)
