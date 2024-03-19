import functools
import re
from pathlib import Path
from typing import Any


path = Path('storage/phonebook.txt')


def input_error(func):

    @functools.wraps(func)

    def inner(command, args):

        try:
            return func(command, args)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."

    return inner


@input_error
def add_contact(command: str, args: list) -> str:
    """
    :param command:
    :param args:
    :return:
    """
    username, phone = args

    with open(path, encoding='utf-8') as fh:
        if is_exist(username, fh.read()):
            return 'Contact is exists'

    with open(path, 'a', encoding='utf-8') as fh:
        fh.write(f'{username},{phone}\n')
        return 'Contact added.'


@input_error
def change_contact(command: str, args: list) -> str:
    """
    :param command:
    :param args:
    :return:
    """
    username, phone = args

    with open(path, encoding='utf-8') as fh:
        if not is_exist(username, fh.read()):
            return 'Contact not found'

        fh.seek(0)
        lines = [line.strip() for line in fh.readlines()]
        for k, line in enumerate(lines):
            lines[k] = f'{line}\n'
            if is_exist(username, line):
                lines[k] = f'{username},{phone}\n'

    with open(path, '+w', encoding='utf-8') as fh:
        fh.writelines(lines)

    return 'Contact changed.'


@input_error
def show_phone(command: str, args: list) -> str:
    """
    :param command:
    :param args:
    :return:
    """
    username = args[0]

    with open(path, encoding='utf-8') as fh:
        if not is_exist(username, fh.read()):
            return 'Contact not found'

        fh.seek(0)
        lines = [line.strip() for line in fh.readlines()]
        for line in lines:
            if is_exist(username, line):
                return dict_to_text([line_to_dict(line)])


def show_all() -> str:
    """
    :return:
    """
    try:
        with open(path, encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
    except FileNotFoundError as err:
        return f'{err.strerror}: {path.name}'

    return dict_to_text([line_to_dict(line) for line in lines])


def parse_input(command: str) -> tuple[Any, Any]:
    """
    :param command:
    :return:
    """
    cmd, *args = re.split(r"\s+", command)
    cmd = cmd.lower()

    return cmd, args


def line_to_dict(line: str) -> dict:
    """
    :param line:
    :return:
    """
    return dict(zip(['name', 'phone'], line.split(',')))


def dict_to_text(function) -> str:
    """
    :param function:
    :return:
    """
    return '\n'.join([pattern(item) for item in function])


def pattern(item: dict) -> str:
    """
    :param item:
    :return:
    """
    return f"{item['name']}: {phone_format(item['phone'])}"


def is_exist(username: str, context: str) -> bool:
    """
    :param username:
    :param context:
    :return:
    """
    return username in re.findall(r'(.*?),', context)


def phone_format(phone_number: str) -> str:
    """
    :param phone_number:
    :return:
    """
    return re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'(\1) \2-\3-\4', phone_number)


def main():
    print("Welcome to the assistant bot!")
    while True:
        try:
            command = input("Enter a command: ").strip()

            command, args = parse_input(command)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "add":
                result = add_contact(command, args)

            elif command == "change":
                result = change_contact(command, args)

            elif command == "phone":
                result = show_phone(command, args)

            elif command == "all":
                result = show_all()

            elif command == "hello":
                result = "How can I help you?"

            else:
                result = "Invalid command."

            print(result)

        except KeyboardInterrupt:
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
