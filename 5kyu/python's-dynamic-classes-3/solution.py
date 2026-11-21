from typing import Type

def create_class(class_name: str, secrets: dict = {}) -> Type:
    if not class_name:
        return None
    return type(class_name, (object,), secrets)