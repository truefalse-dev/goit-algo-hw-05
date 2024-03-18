import re
from decimal import Decimal


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як \
основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def sum_profit(_text: str) -> str:
    """
    :param _text:
    :return:
    """
    def generator_numbers():
        for item in re.findall(r"\d+.\d+", _text):
            yield item

    return str(sum([Decimal(item) for item in generator_numbers()]))


def main():
    total_income = sum_profit(text)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()