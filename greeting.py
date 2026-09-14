"""Формирование приветствия."""


def greet(name: str) -> str:
    """Вернуть приветствие для указанного имени."""
    return f"Hello, {name.strip() or 'world'}!"
