# pykeksikapi

<br>
<br>

Для начала импортируем и инициализируем экземпляр класса:
```Python
from pykeksikapi import KeksikAPI

keksik = KeksikAPI(token='your_keksik_token', group_id='your_id_group')
```

<br>
<br>

Пример получения списка донатов сообщества, сортировка по сумме доната:
```Python
await keksik.donates.get(sort='amount')
```

<br>
<br>

Пример получения текущего баланса кексика:
```Python
outcome = await keksik.other.balance()

print(outcome.balance) # Покажет текущий баланс кексика
```
