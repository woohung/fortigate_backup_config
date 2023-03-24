# Python script for backup config Fortigates, using API Fortinet

Скрипт предназначен для сбора бэкап-конфигурации с одного или более FW Fortigate. 

> Это один из моих первых проектов на Python, если вы знаете, как можно сделать код лучше, присылайте PR, буду рад любой посильной помощи.

> В связке с этим проектом, опубликована [статья](https://woohung.github.io/automation/2023/03/24/%D0%A0%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%D1%81%D1%8F-%D1%81-API-%D0%BD%D0%B0-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D0%B5-API-Fortinet.-%D0%9F%D0%B8%D1%88%D0%B5%D0%BC-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82-%D0%BF%D0%BE-%D0%B1%D1%8D%D0%BA%D0%B0%D0%BF%D1%83-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D0%B0/html) в блоге.

Вызывать справку по скрипту - `-h`  

На вход передается файл в формате .yaml, содержащий список словарей: `[{host1:value, token1:value}, {host2:value, token2:value}]`  
```
Args:
    device (str): IP-адрес устройства FortiGate.
    token (str): Токен для аутентификации по API.
    backup_dir (str): Директория для сохранения резервных копий.
    enable_warning (bool, optional): Вкл/Выкл предупреждение sefl-sign SSL.
        По умолчанию True.
    enable_ssl (bool, optional): Вкл/Выкл проверку SSL.
        По умолчанию False.

Raises:
    requests.exceptions.Timeout: Если время ожидания ответа от API истекает.
    requests.exceptions.HTTPError: Если получен ответ с HTTP-кодом ошибки.
    requests.exceptions.RequestException: Если произошла какая-либо ошибка при выполнении запроса.
```

## Как работать со скриптом
Копируем скрипт и файл .yaml в удобное место, правим `devices.yaml` в соответствии с вашими устройствами:
- host: в формате IP-адреса)
- token: копируем значение вашего API-токена

Параметр `--config-file (-C)` и `--backup-dir (-D)` обязателен, остальное опционально.  

Пример вызова функции из терминала:
```
python fortios_backup_config.py -C ../devices_api.yaml -D ~/manage-tools/output/backups/
```


