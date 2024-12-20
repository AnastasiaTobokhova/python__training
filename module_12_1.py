import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("TestRunner")
        # Вызов метода walk 10 раз
        for _ in range(10):
            runner.walk()
        # Проверка, что distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("TestRunner")
        # Вызов метода run 10 раз
        for _ in range(10):
            runner.run()
        # Проверка, что distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # Вызов методов run и walk 10 раз соответственно
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверка, что их distance не равны
        self.assertNotEqual(runner1.distance, runner2.distance)


