import string


def password():
    valid_chars = set(string.punctuation + 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') # Даша подсказала, что есть string.ascii_lowercase, string.ascii_uppercase, string.digits, а я, дурачок, пишу так
    in_pass = str(input('Введите пароль: '))
    return True\
        if all(char in valid_chars for char in in_pass)\
        else False


print(password())
