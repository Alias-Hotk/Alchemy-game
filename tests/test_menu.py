import io
import unittest
from unittest.mock import patch

def menu_text():
    print("Для сохранения прогресса наберите - save and exit")
    print("Для выхода наберите - exit")
    print("Для создания рецепта наберите - создать рецепты")
    print("Для перемещения между страницами используйте знаки - < и >")

class TestMenuText(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_text_output(self, mock_stdout):
        expected_output = "Для сохранения прогресса наберите - save and exit\n" \
                          "Для выхода наберите - exit\n" \
                          "Для создания рецепта наберите - создать рецепты\n" \
                          "Для перемещения между страницами используйте знаки - < и >\n"

        menu_text()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()