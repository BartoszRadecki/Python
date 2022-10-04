def is_all_upper(text: str) -> bool:

    print(text.upper())
    text = text.replace(" ", "")
    cond1 = len(text) > 0
    cond2 = text == text.upper()
    cond3 = text.isdigit() == False
    return all([cond1,cond2,cond3])

