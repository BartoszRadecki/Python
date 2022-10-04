def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    password = password.lower()
    wynik = any(map(str.isdigit, password))
    litera = any(map(str.isalpha, password))
    cond5 = 'password' not in password.lower()
    cond6 = len(set(password)) > 2
    if len(password) > 9:
        wynik = litera = True

    return all([cond1, wynik, litera, cond6, cond5])