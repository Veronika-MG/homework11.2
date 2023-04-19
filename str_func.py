def str_upper(str):
    """
    Переводит все буквы в верхний регистр.
    :param str:
    :return:
    """
    return str.upper()


def first_letter(str):
    """
    Переводит первые буквы в заглавные.
    :param str: str
    :return: строку с заглавными первыми буквами.
    """
    return ' '.join(map(lambda x: x.capitalize(), str.split(' ')))
