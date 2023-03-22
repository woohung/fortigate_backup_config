# Python script for backup config Fortigates, using API Fortinet

Скрипт предназначен для сбора бэкап-конфигурации с одного или более FW Fortigate. 

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
