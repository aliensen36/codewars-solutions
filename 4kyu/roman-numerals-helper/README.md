# Roman Numerals Helper

[![Codewars](https://img.shields.io/badge/Codewars-4%20kyu-red)](https://www.codewars.com/kata/51b66044bce5799a7f000003)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

## 📝 Описание задачи

Необходимо реализовать два метода для конвертации между римскими числами и целыми значениями:

- `to_roman(n)` — преобразует целое число в римскую запись
- `from_roman(s)` — преобразует строку с римским числом в целое

Современные римские числа записываются путём выражения каждой цифры отдельно, начиная с самой левой, пропуская нули.

**Диапазон входных значений:** `1 <= n < 4000`

> В этой ката число 4 записывается как `IV`, а не как `IIII` («часовое» четыре).

## 📊 Таблица соответствия

| Символ | Значение |
|--------|----------|
| M      | 1000     |
| CM     | 900      |
| D      | 500      |
| CD     | 400      |
| C      | 100      |
| XC     | 90       |
| L      | 50       |
| XL     | 40       |
| X      | 10       |
| IX     | 9        |
| V      | 5        |
| IV     | 4        |
| I      | 1        |

## ✅ Примеры

```python
# to_roman
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

# from_roman
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
```

## 💡 Идея решения

### `to_roman(n)`
Жадный алгоритм: перебираем пары `(значение, символ)` в порядке убывания значений. Пока `n >= значение`, добавляем символ к результату и вычитаем значение из `n`.

### `from_roman(s)`
Проходим по строке слева направо. Если значение текущего символа меньше значения следующего — вычитаем его (например, `IV`: `I < V`, значит `-1`), иначе прибавляем. Это автоматически обрабатывает субтрактивные пары (`IV`, `IX`, `XL`, `XC`, `CD`, `CM`).

## 🧪 Тесты

```python
import pytest
from solution import RomanNumerals

rn = RomanNumerals()

@pytest.mark.parametrize("n, expected", [
    (1, "I"),
    (4, "IV"),
    (9, "IX"),
    (86, "LXXXVI"),
    (1666, "MDCLXVI"),
    (1990, "MCMXC"),
    (2000, "MM"),
    (2008, "MMVIII"),
    (3999, "MMMCMXCIX"),
])
def test_to_roman(n, expected):
    assert rn.to_roman(n) == expected

@pytest.mark.parametrize("s, expected", [
    ("I", 1),
    ("IV", 4),
    ("MM", 2000),
    ("MDCLXVI", 1666),
    ("LXXXVI", 86),
    ("MCMXC", 1990),
    ("MMVIII", 2008),
    ("MMMCMXCIX", 3999),
])
def test_from_roman(s, expected):
    assert rn.from_roman(s) == expected
```
