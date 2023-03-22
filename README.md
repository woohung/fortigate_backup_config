# Python script for backup config Fortigates, using API Fortinet

Скрипт предназначен для сбора бэкап-конфигурации с одного или более FW Fortigate. 

Вызывать справку по скрипту - `-h`  
Основная функция `fortios_backup_config` имеет подробный Docstring.  

## Как работать со скриптом
Копируем скрипт и файл .yaml в удобное место, правим `devices.yaml` в соответствии с вашими устройствами:
- host: в формате IP-адреса)
- token: копируем значение вашего API-токена

Параметр `--config-file (-C)` и `--backup-dir (-D)` обязателен, остальное опционально.  

Пример вызова функции из терминала:
```
python fortios_backup_config.py -C ../devices_api.yaml -D ~/manage-tools/output/backups/
```
