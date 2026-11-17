# User class for Banking System

- **Ссылка:** https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python
- **Сложность:** 7 kyu
- **Темы:** object-oriented programming, classes, exceptions, fundamentals

## Условие

Компания открывает банк, но программист, проектирующий класс пользователя, застрял. Нужно помочь ему и реализовать три метода на классе `User` (каркас класса уже дан в задании):

- **`withdraw(self, amount)`** — снимает `amount` с баланса пользователя. Если денег не хватает, бросает `ValueError` (overdraw). Иначе возвращает строку `"<Name> has <balance>."` с именем и **новым** балансом.
- **`check(self, issuer, amount)`** — переводит `amount` от `issuer` (того, кто выписывает чек) к `self` (получателю). Бросает `ValueError`, если у `issuer` не хватает денег (bad check) или если у `issuer` `checking_account == False` (non-checking account). Иначе возвращает строку `"<User name> has <user balance> and <Issuer name> has <issuer balance>."`.
- **`add_cash(self, amount)`** — пополняет баланс на `amount` и возвращает строку `"<Name> has <balance>."`.

### Замечания

- Атрибут `checking_account` (bool) должен существовать на классе.
- Все числовые входы — неотрицательные целые; баланс всегда должен оставаться целым.
- Возвращаемые строки должны заканчиваться точкой.
- Валюта не используется.

### Пример

```python
Jeff = User(name='Jeff', balance=70, checking_account=True)
Joe  = User(name='Joe',  balance=70, checking_account=False)

Jeff.withdraw(2)          # 'Jeff has 68.'
Joe.check(Jeff, 50)       # 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80)       # ValueError: Joe is not a checking account

Joe.checking_account = True
Jeff.check(Joe, 80)       # 'Jeff has 98 and Joe has 40.'

Joe.check(Jeff, 100)      # ValueError: bad check (у Jeff только 98)

Jeff.add_cash(20.00)      # 'Jeff has 118.'  ← баланс остался int, не 118.0
```

## Ключевая идея

**Кто есть кто в `check`.** `self` — получатель чека (ему прибавляем), `issuer` — плательщик (у него вычитаем). Легко перепутать, потому что оба — объекты `User`. В примере `Joe.check(Jeff, 50)` Joe получает, а Jeff платит: у Joe было 70 → стало 120, у Jeff было 70 → стало 18. Поэтому и в сообщениях об ошибках «виноват» всегда `issuer` — он платит, у него проверяют `checking_account` и баланс.

**Порядок проверок в `check` важен.** Сначала проверяем `issuer.checking_account`, и только потом — хватает ли у него баланса. Если поменять местами, то для Joe с `checking_account=False` и нехваткой денег мы бросим «bad check», а тест ждёт «non-checking account». После `raise` выполнение метода прерывается, поэтому `else` не нужен — код после блока `if` выполнится только при успешной проверке.

**Тип `int`.** В `add_cash(20.00)` приходит `float`, и `98 + 20.00` даёт `118.0`, а не `118`. Задание требует целый баланс, поэтому сумму нужно приводить к `int` (например, `int(self.balance + amount)`). `int()` отбрасывает дробную часть, а не округляет, — для неотрицательных целых это безопасно.

**Проверки в `withdraw`.** Сначала `if self.balance < amount: raise ValueError(...)`, и только потом вычитание. Так при нехватке денег баланс гарантированно не изменится.
