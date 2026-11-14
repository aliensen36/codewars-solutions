# Never visit a . . . !?

- **Ссылка:** https://www.codewars.com/kata/never-visit-a
- **Сложность:** 8 kyu (по факту сложнее — 6–7 kyu)
- **Темы:** puzzles, strings, number theory, mathematics

## Условие

Дано число `n` (10 ≤ n < 10000). Нужно повторять:

1. Суммировать все цифры `n`.
2. Вычесть эту сумму из `n` — получаем новое `n`.
3. Если новое `n` есть в таблице (1–100 → фрукт) — вернуть фрукт.
   Иначе вернуться к шагу 1.

### Пример

```
n = 325
sum = 3+2+5 = 10
n = 325-10 = 315  (нет в таблице)
sum = 3+1+5 = 9
n = 315-9 = 306   (нет в таблице)
sum = 3+0+6 = 9
n = 306-9 = 297   (нет в таблице)
...
...пока не попадём в число из таблицы
```

Важно: это не про навыки кодирования — надо подумать перед тем, как писать код.

## Таблица фруктов (1–100)

| # | Фрукт | # | Фрукт | # | Фрукт | # | Фрукт |
|---|-------|---|-------|---|-------|---|-------|
| 1 | kiwi | 26 | kiwi | 51 | melon | 76 | melon |
| 2 | pear | 27 | apple | 52 | pineapple | 77 | pineapple |
| 3 | kiwi | 28 | melon | 53 | melon | 78 | cucumber |
| 4 | banana | 29 | banana | 54 | apple | 79 | pineapple |
| 5 | melon | 30 | melon | 55 | cucumber | 80 | cucumber |
| 6 | banana | 31 | pineapple | 56 | pineapple | 81 | apple |
| 7 | melon | 32 | melon | 57 | cucumber | 82 | grape |
| 8 | pineapple | 33 | pineapple | 58 | orange | 83 | orange |
| 9 | apple | 34 | cucumber | 59 | cucumber | 84 | grape |
| 10 | pineapple | 35 | orange | 60 | orange | 85 | cherry |
| 11 | cucumber | 36 | apple | 61 | grape | 86 | grape |
| 12 | pineapple | 37 | orange | 62 | cherry | 87 | cherry |
| 13 | cucumber | 38 | grape | 63 | apple | 88 | pear |
| 14 | orange | 39 | orange | 64 | cherry | 89 | cherry |
| 15 | grape | 40 | grape | 65 | pear | 90 | apple |
| 16 | orange | 41 | cherry | 66 | cherry | 91 | kiwi |
| 17 | grape | 42 | pear | 67 | pear | 92 | banana |
| 18 | apple | 43 | cherry | 68 | kiwi | 93 | kiwi |
| 19 | grape | 44 | pear | 69 | pear | 94 | banana |
| 20 | cherry | 45 | apple | 70 | kiwi | 95 | melon |
| 21 | pear | 46 | pear | 71 | banana | 96 | banana |
| 22 | cherry | 47 | kiwi | 72 | apple | 97 | melon |
| 23 | pear | 48 | banana | 73 | banana | 98 | pineapple |
| 24 | kiwi | 49 | kiwi | 74 | melon | 99 | apple |
| 25 | banana | 50 | banana | 75 | pineapple | 100 | pineapple |
