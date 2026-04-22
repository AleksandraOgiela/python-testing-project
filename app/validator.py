def czy_email(email):
    if not isinstance(email, str):
        return False
    
    if "@" not in email:
        return False
    
    if "." not in email:
        return False
    
    return True

def czy_mac(mac):
    if not isinstance(mac, str):
        return False
    
    parts = mac.split(":")

    if len(parts) != 6:
        return False
    
    for part in parts:
        if len(part) != 2:
            return False
        try:
            int(part, 16)
        except ValueError:
            return False
        
    return True