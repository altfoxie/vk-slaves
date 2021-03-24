# vk-slaves
Простая библиотека для взаимодействия с игрой [Рабы](https://vk.com/app7794757) во ВКонтакте.

## Установка
```bash
$ pip3 install vk-slaves
```

## Использование
Для отправки запросов к игре нужно получить токен VK, например [здесь](https://oauth.vk.com/authorize?client_id=6121396&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1).

### Создание клиента
```python
from vk_slaves import Slaves
client = Slaves('token123456')
```

### Взаимодействие
```python
print(client.start())
print(client.top_users())
print(client.slave_list(id=12345678))

client.buy_slave(87654321)
```
