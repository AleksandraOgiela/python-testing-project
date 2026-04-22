def czy_email(email):
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

print(czy_email("test@test.com"))
