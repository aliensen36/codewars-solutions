# The Lamp: Revisited

## Описание задачи

Реализовать класс `Lamp` (Лампа) со следующими характеристиками:

- **Атрибуты:**
  - `color` (строка) — цвет лампы
  - `on` (булево значение) — включена ли лампа

- **Конструктор** принимает параметр `color` и устанавливает `on = False` при инициализации.

- **Методы:**
  - `toggle_switch()` — переключает значение атрибута `on` (вкл/выкл)
  - `state()` — возвращает строку:
    - `"The lamp is on."` — если лампа включена
    - `"The lamp is off."` — если лампа выключена

## Пример использования

```python
lamp = Lamp("red")
print(lamp.state())        # "The lamp is off."
lamp.toggle_switch()
print(lamp.state())        # "The lamp is on."
lamp.toggle_switch()
print(lamp.state())        # "The lamp is off."
```
