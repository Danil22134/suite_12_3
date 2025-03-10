import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = Runner("Ivan")
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner("Petr")
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Ivan")
        runner2 = Runner("Petr")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertEqual(runner1.distance != runner2.distance, True)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_variants = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = Runner('Усейн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)
        self.name = "Ник"

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == self.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[3] == self.name)

    @classmethod
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_variants):
            print(f'{k + 1}: {v}')


if __name__ == "__main__":
    unittest.main()
