class Respondent:
    def __init__(self, _input):
        info = _input.split(",")
        self.fio = info[0]
        self.age = int(info[1])

class Breakdown:
    def __init__(self):
        self.__respondents = {
            "100+":
                {"to": 123, "respondents": []},
            "81-100":
                {"to": 100, "respondents": []},
            "61-80":
                {"to": 80, "respondents": []},
            "46-60":
                {"to": 60, "respondents": []},
            "36-45":
                {"to": 45, "respondents": []},
            "26-35":
                {"to": 35, "respondents": []},
            "19-25":
                {"to": 25, "respondents": []},
            "0-18":
                {"to": 18, "respondents": []},
        }

    def add_respondent(self, respondent):
        for group in reversed(self.__respondents):
            if respondent.age <= self.__respondents[group]["to"]:
                self.__respondents[group]["respondents"].append(respondent)
                self.__respondents[group]["respondents"].sort(key=lambda _respondent: (-_respondent.age, _respondent.fio))
                break

    def print(self):
        for group in self.__respondents:
            if len(self.__respondents[group]["respondents"]) != 0:
                string = f"{group}: " + ", ".join(f"{resp.fio} ({resp.age})" for resp in self.__respondents[group]["respondents"])
                print(string, end="\n\n")


def main():
    # For debug
    # respondents_data = [
    #     "Кошельков Захар Брониславович, 105",
    #     "Дьячков Нисон Иринеевич, 88",
    #     "Ярилова Розалия Трофимовна, 29",
    #     "Соколов Андрей Сергеевич, 15",
    #     "Иванов Варлам Якунович, 88",
    #     "Старостин Ростислав Ермолаевич, 50",
    #     "Егоров Алан Петрович, 7",
    #     "Егоров Ян Петрович, 7",
    #     "Егоров Борис Петрович, 7"
    # ]

    breakdown = Breakdown()

    while True:
        respondent_data = input()
        if respondent_data == "END":
            break

        respondent = Respondent(respondent_data)
        breakdown.add_respondent(respondent)

    # For debug
    # for respondent_data in respondents_data:
    #
    #     respondent = Respondent(respondent_data)
    #     breakdown.add_respondent(respondent)

    breakdown.print()


if __name__ == "__main__":
    main()