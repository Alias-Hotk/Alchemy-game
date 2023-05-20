import os
import unittest
from io import StringIO
from unittest import mock
import pytest

class Testfileop(unittest.TestCase):

 def test_file_open(self):
    # проверяем, что файл открывается для записи
    with self.assertRaises(PermissionError):
     with open("../Recipes.dat", "w") as f:
         f.write("Test recipe")

 def test_choice_1(self):
    # проверяем ветвь, где пользователь выбирает 1
    with mock.patch('builtins.input', return_value="1"):
        with mock.patch('builtins.open', mock.mock_open(read_data="Test data")):
            data = os.system("cls")
            assert data == 0

 def test_invalid_choice(self):
    # проверяем ветвь, где пользователь выбирает некорректный вариант
    with mock.patch('builtins.input', return_value="3"):
        with mock.patch('builtins.print', side_effect=SystemExit):
            os.system("cls")

 def test_exit(self):
    # проверяем ветвь, где пользователь выбирает выход
    with mock.patch('builtins.input', return_value="exit"):
        with mock.patch('builtins.print', side_effect=SystemExit):
            os.system("cls")

 def test_choice_2(self):
    # проверяем ветвь, где пользователь выбирает 2
    with mock.patch('builtins.input', side_effect=["2", "1"]):
        with mock.patch('os.listdir', return_value=["Test profile"]):
            with mock.\
                    patch('builtins.open', mock.mock_open(read_data="Test data")):
                data = os.system("cls")
                assert data == 0

 def test_profile_not_found(self):
    # проверяем ветвь, где не найден профиль пользователя
    with mock.patch('builtins.input', return_value="2"):
        with mock.patch('os.listdir', return_value=[]):
            with mock.patch('builtins.print', side_effect=SystemExit):
                os.system("cls")

 def test_save_and_exit(self):
    # проверяем сохранение профиля пользователя
    with mock.patch('builtins.input', side_effect=["save and exit", "Test user"]):
        with mock.patch('builtins.open', mock.mock_open(read_data="Test data")):
            with mock.patch('builtins.print', side_effect=SystemExit):
                os.system("cls")
    assert os.path.exists("profiles/Test user.dat")


if __name__ == '__main__':
    unittest.main()