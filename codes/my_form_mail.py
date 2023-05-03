from re import fullmatch


def mail_is_correct(mail: str):
    """Проверка почты на корректность"""
    return fullmatch(r"[a-zA-Z0-9._&=‘\-+]{1,256}@[a-zA-Z0-9]{1,100}\.[a-zA-Z0-9]{1,7}", mail) is not None
