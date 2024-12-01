"""
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите
следующие методы:

test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual
сравните distance этого объекта со значением 50.

test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual
сравните distance этого объекта со значением 100.

test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
Далее 10 раз у объектов вызываются методы run и walk соответственно.
Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
"""

import unittest
import runner


class RunnerTest(unittest.TestCase):
    """Дочерний класс, наследуемый от класса unittest.TestCase"""

    def test_walk(self):
        """Метод тестирует метод объекта 'walk'"""
        runner_walk = runner.Runner('Runner_1')  # создаем экземпляр класса
        for i in range(10):  # в цикле от 0 до 9
            runner_walk.walk()  # вызываем метод 'walk' объекта
        self.assertEqual(runner_walk.distance, 50)  # сравниваем значение атрибута объекта
        # с контрольным значением

    def test_run(self):
        """Метод тестирует метод объекта 'run'"""
        runner_run = runner.Runner('Runner_2')  # создаем экземпляр класса
        for i in range(10):  # в цикле от 0 до 9
            runner_run.run()  # вызываем метод 'run' объекта
        self.assertEqual(runner_run.distance, 100)  # сравниваем значение атрибута объекта
        # с контрольным значением

    def test_challenge(self):
        """Метод тестирует атрибуты двух объектов класса на неравенство"""
        test_runner_1 = runner.Runner('Runner_1')  # создаем первый объект класса
        test_runner_2 = runner.Runner('Runner_2')  # создаем второй объект класса
        for i in range(10):  # в цикле от 0 до 9
            test_runner_1.run()  # вызываем метод 'run' для первого объекта
            test_runner_2.walk()  # вызываем метод 'walk' для второго объекта
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)  # сравниваем значение атрибута объектов
        # с контрольным значением на неравенство


if __name__ == '__main__':
    unittest.main()  # вызов метода тестирования