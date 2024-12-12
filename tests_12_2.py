# Домашнее задание по теме "Методы Юнит-тестирования".
# Задача с целью освоения методов, которые содержит класс TestCase.

import unittest


class Runner:
    def __init__(self, name, speed=5):
        # Инициализация участника с его именем и скоростью
        # Проверяем, что имя является строкой
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')

        self.distance = 0  # Инициализация пройденного расстояния для участника
        # Проверяем, что скорость является положительным числом
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        # Метод, позволяющий участнику бежать
        # Увеличиваем пройденное расстояние участника в два раза от его скорости
        self.distance += self.speed * 2

    def walk(self):
        # Метод, позволяющий участнику идти
        # Увеличиваем пройденное расстояние участника на его скорость
        self.distance += self.speed

    def __str__(self):
        # Возвращает строковое представление имени участника
        return self.name

    def __repr__(self):
        # Возвращает представление участника, используемое в отладочных целях
        return self.name

    def __eq__(self, other):
        # Метод сравнения экземпляров Runner с другим объектом
        if isinstance(other, str):
            return self.name == other  # Сравниваем с строкой
        elif isinstance(other, Runner):
            return self.name == other.name  # Сравниваем с другим объектом Runner


class Tournament:
    def __init__(self, distance, *participants):
        # Инициализация турнира с заданной дистанцией и участниками
        self.full_distance = distance  # Полное расстояние турнира
        self.participants = list(participants)  # Список участников турнира

    def start(self):
        # Метод запуска турнира
        finishers = {}  # Словарь для хранения финишеров и их мест
        place = 1  # Начальное место для финишеров

        # Цикл продолжается пока есть участники, которые не завершили гонку
        while self.participants:
            for participant in self.participants:
                participant.run()  # Участник бежит
                # Если участник преодолел полное расстояние, добавляем его в финишеры
                if participant.distance >= self.full_distance:
                    finishers[place] = participant  # Записываем участника в словарь
                    place += 1  # Переходим к следующему месту
                    self.participants.remove(participant)  # Удаляем участника из гонки

        return finishers  # Возвращаем всех финиширов


class TournamentTest(unittest.TestCase):
    all_results = {}  # Словарь для хранения результатов всех тестов

    @classmethod
    def setUpClass(cls):
        # Метод, предшествующий выполнению всех тестов, для инициализации общих данных
        cls.all_results = {}

    def setUp(self):
        # Метод, выполняемый перед каждым тестом, для участников
        self.runner1 = Runner('Усэйн', 10)  # Создаем первого участника
        self.runner2 = Runner('Андрей', 9)  # Создаем второго участника
        self.runner3 = Runner('Ник', 3)  # Создаем третьего участника

    def tearDown(self):
        # Метод, выполняемый после каждого теста (можно использовать для очистки, если нужно)
        pass

    @classmethod
    def tearDownClass(cls):
        # Метод, выполняемый после окончания всех тестов, для вывода всех результатов
        for key, value in cls.all_results.items():
            print(value)

    def test_race_usain_nik(self):
        # Тест для гонки между Усэйном и Ником
        tournament = Tournament(90, self.runner1, self.runner3)  # Инициализируем турнир
        result = tournament.start()  # Запускаем турнир
        self.all_results[max(result.keys())] = result  # Сохраняем результат

        # Проверяем, что Ник финишировал последним
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_andrey_nik(self):
        # Тест для гонки между Андреем и Ником
        tournament = Tournament(90, self.runner2, self.runner3)  # Инициализируем турнир
        result = tournament.start()  # Запускаем турнир
        self.all_results[max(result.keys())] = result  # Сохраняем результат

        # Проверяем, что Ник финишировал последним
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_usain_andrey_nik(self):
        # Тест для гонки между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)  # Инициализируем турнир
        result = tournament.start()  # Запускаем турнир
        self.all_results[max(result.keys())] = result  # Сохраняем результат

        # Проверяем, что Ник финишировал последним
        self.assertTrue(result[max(result.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()  # Запуск тестов
