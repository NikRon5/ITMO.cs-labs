import unittest

from src.lab4.task2.main import Respondent, Breakdown

class BreakdownTestCase(unittest.TestCase):
    def test_breakdown(self):
        # Given
        respondents_data = [
            "Кошельков Захар Брониславович, 105",
            "Дьячков Нисон Иринеевич, 88",
            "Ярилова Розалия Трофимовна, 29",
            "Соколов Андрей Сергеевич, 15",
            "Иванов Варлам Якунович, 88",
            "Старостин Ростислав Ермолаевич, 50",
            "Егоров Алан Петрович, 7",
            "Егоров Ян Петрович, 7",
            "Егоров Борис Петрович, 7"
        ]
        breakdown = Breakdown()
        expected_output = """100+: Кошельков Захар Брониславович (105)

81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)

46-60: Старостин Ростислав Ермолаевич (50)

26-35: Ярилова Розалия Трофимовна (29)

0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7), Егоров Борис Петрович (7), Егоров Ян Петрович (7)"""

        # When
        for respondent_data in respondents_data:
            respondent = Respondent(respondent_data)
            breakdown.add_respondent(respondent)
        output = breakdown.get_output()

        # Then
        self.assertEqual(expected_output, output)