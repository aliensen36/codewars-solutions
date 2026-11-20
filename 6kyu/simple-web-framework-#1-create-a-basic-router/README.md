# Simple Web Framework #1 — Create a basic router

**Уровень:** 6 kyu
**Темы:** ООП, словари, callable-объекты, обработка ошибок
**Ссылка:** https://www.codewars.com/kata/588a00ad70720f2cd9000005

## 📖 Описание задачи

Нужно реализовать класс `Router` — простейший маршрутизатор для веб-фреймворка. Роутер хранит привязки «URL + HTTP-метод → действие» и умеет выполнять действие по входящему запросу.

### Требования

1. **`bind(url, method, action)`** — привязывает действие (callable) к паре `(url, method)`.
2. **`runRequest(url, method)`** — находит действие по паре `(url, method)` и возвращает результат его вызова.
3. Если маршрут не найден — вернуть строку:
   ```
   'Error 404: Not Found'
   ```
4. Повторный `bind` для той же пары `(url, method)` **перезаписывает** существующее действие.
5. Один и тот же URL с разными методами — это **разные** маршруты.

## 💡 Пример использования

```python
router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')

router.runRequest('/hello', 'GET')   # 'hello world'
router.runRequest('/nope', 'GET')    # 'Error 404: Not Found'
```
