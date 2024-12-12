# Домашнее задание по теме "Методы Юнит-тестирования".
# Задача с целью освоения методов, которые содержит класс TestCase.

import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        # Условия для проверки завершения гонки
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results[max(result.keys())] = result

        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[max(result.keys())] = result

        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[max(result.keys())] = result

        self.assertTrue(result[max(result.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
