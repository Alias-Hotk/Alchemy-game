import unittest
from unittest.mock import patch
import io
import os


class TestCreateRecipes(unittest.TestCase):
    def setUp(self):
        self.input_values = ['test user', 'elem1+elem2=elem3', 'сохранить рецепты']
        self.expected_output = f"Рецепты сохранены в файле custom/рецепты test user.dat\n"

    @patch('builtins.input')
    def test_create_recipes(self, mock_input):
        mock_input.side_effect = self.input_values

        with patch('sys.stdout', new=io.StringIO()) as fake_output:

            username = input("Введите пользователя: ")
            recipes = []
            while True:
                recipe = input(
                    "Введите рецепты в формате элемент1+элемент2=результат(или 'сохранить рецепты' для сохранения): ")
                if recipe.lower() == "сохранить рецепты":
                    break
                recipes.append(recipe)
            filename = f"custom/рецепты {username}.dat"
            with open(filename, "w") as f:
                f.write("\n".join(recipes))
            print(f"Рецепты сохранены в файле {filename}")

        self.assertEqual(fake_output.getvalue(), self.expected_output)

        os.remove(filename)

if __name__ == '__main__':
    unittest.main()


