import sys
import re
import collections


def parse_log_line(line: str) -> dict:
    """
    :param line:
    :return:
    """
    keys = ['date', 'level', 'info']
    datetime_pattern = "^[0-9]{4}-[0-9]{2}-[0-9]{2}\\s[0-9]{2}:[0-9]{2}"
    level_pattern = '\\b[A-Z]+\\b'
    info_pattern = '.*'
    match = re.search(rf'({datetime_pattern}).+({level_pattern})\s({info_pattern})', line)
    return dict(zip(keys, match.groups()))


def load_logs(file_path: str) -> list:
    """
    :param file_path:
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            for line in file:
                yield parse_log_line(line.strip())
    except FileNotFoundError as er:
        print(er.strerror)


def filter_logs_by_level(logs: list, _level: str) -> list:
    """
    :param logs:
    :param _level:
    :return:
    """
    return list(filter(lambda line: line['level'] == _level, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    :param logs:
    :return:
    """
    leveldict = collections.defaultdict(int)

    for log in logs:
        leveldict[log['level']] += 1

    return leveldict


def display_log_counts(counts: dict):
    """
    :param counts:
    """
    items = counts.items()

    if items:
        print('Рівень логування | Кількість')
        print('-----------------|----------')
        for item in counts.items():
            print(f"{item[0]:16} | {item[1]}")
    else:
        print('Список логів пустий.')


def main():
    if len(sys.argv) > 1:
        _list = [item for item in load_logs(sys.argv[1])]

        display_log_counts(count_logs_by_level(_list))

        if len(sys.argv) > 2:
            level = sys.argv[2].upper()

            list_of_levels = filter_logs_by_level(_list, level)

            if list_of_levels:
                print(f"\nДеталі логів для рівня '{level}':")
                for item in list_of_levels:
                    print(f"{item['date']} - {item['info']}")
    else:
        print('input a logs file path as an argument')


if __name__ == '__main__':
    main()