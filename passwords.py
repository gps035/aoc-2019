def has_double(password: str):
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            return True
    return False


def is_ascending(password: str):
    for i in range(1, len(password)):
        if password[i] < password[i - 1]:
            return False
    return True


def has_strict_double(password: str):
    current_duplicates = 1
    for i in range(1, len(password)):
        if password[i] != password[i - 1]:
            if current_duplicates == 2:
                return True
            current_duplicates = 0
        current_duplicates += 1
    return current_duplicates == 2


def is_valid_password_simple(password: str):
    return is_ascending(password) and has_double(password)


def is_valid_password_strict(password: str):
    if is_ascending(password) and has_strict_double(password):
        return True
    return False
