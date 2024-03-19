import re
from decimal import Decimal
from typing import Callable

text = "176.45 Загальний дохід працівника складається з декількох частин: 1000.01 як \
основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.34.67"


def generator_numbers(_text: str):
    for item in re.findall(r"\s\d+.\d+\s", _text):
        yield item.strip()


def sum_profit(_text: str, func: Callable) -> str:
    """
    :param func:
    :param _text:
    :return:
    """
    return str(sum([Decimal(item) for item in func(_text)]))


def main():
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()