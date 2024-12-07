# Домашнее задание по теме "Простые Юнит-Тесты".
# Задача "Проверка на выносливость".

import unittest
# Необходимо импортировать класс Runner из нужного файла
from runner_and_tournament import Runner  # Или из rt_with_exceptions.py, или из runner.py


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Проверяет, что метод 'walk' увеличивает 'distance' на 5 за каждый вызов."""
        walker = Runner('Walker')  # Создаем объект класса Runner
        for _ in range(10):
            walker.walk()  # Вызываем метод walk 10 раз
        self.assertEqual(walker.distance, 50, "Метод 'walk' не увеличивает 'distance' корректно.")
        # Проверяем, что дистанция равна 50

    def test_run(self):
        """Проверяет, что метод 'run' увеличивает 'distance' на 10 за каждый вызов."""
        runner = Runner('Runner')  # Создаем объект класса Runner
        for _ in range(10):
            runner.run()  # Вызываем метод run 10 раз
        self.assertEqual(runner.distance, 100, "Метод 'run' не увеличивает distance корректно.")
        # Проверяем, что дистанция равна 100

    def test_challenge(self):
        """
        Проверяет, что методы 'walk' и 'run' изменяют 'distance' на разные значения.
        Создаются два объекта 'Runner', один использует 'walk', другой - 'run'.
        """
        walker = Runner('Walker')  # Создаем объект класса Runner
        runner = Runner('Runner')  # Создаем еще один объект класса Runner
        for _ in range(10):
            walker.walk()  # Вызываем метод walk для первого объекта
            runner.run()  # Вызываем метод run для второго объекта
        self.assertNotEqual(walker.distance, runner.distance,
                            "Методы 'walk' и 'run' изменяют 'distance' на одинаковые значения.")
        # Проверяем, что дистанции объектов не равны


if __name__ == '__main__':
    unittest.main()