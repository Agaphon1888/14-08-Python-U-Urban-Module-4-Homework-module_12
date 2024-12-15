# Домашнее задание по теме "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов".

import unittest
from tests_12_3 import TournamentTest  # Импорт тестового класса.

# Создаем объект TestSuite
class TestSuite:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(unittest.makeSuite(TournamentTest))

    def run(self):
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.suite)

if __name__ == '__main__':
    test_suite = TestSuite()
    test_suite.run()