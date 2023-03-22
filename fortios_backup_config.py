import requests
import yaml
import datetime
import os
import urllib3
import logging
import argparse


def fortios_backup_config(
    device,
    token,
    backup_dir=None,
    enable_warning=True,
    enable_ssl=False,
):
    """
    Функция выполняет резервное копирование
    конфигурации устройства FortiGate по API.

    На вход передается файл в формате .yaml,
    содержащий список словарей:
        [{host1:value, token1:value}, {host2:value, token2:value}]

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
    """
    # Инициализация логгера для записи ошибок
    logger = logging.getLogger(__name__)

    # Создание токена для авторизации по API
    unique_api_token = f"Bearer {token}"
    payload = {}
    headers = {"Authorization": unique_api_token}

    # Формирование URL для выполнения запроса
    url = f"https://{device}/api/v2/monitor/system/config/backup?destination=file&scope=global"

    # Отключение предупреждений безопасности SSL
    if enable_warning:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        # Отправка запроса и обработка исключений
        response = requests.get(
            url, headers=headers, data=payload, verify=enable_ssl, timeout=10
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logger.exception(f"Таймаут подключения, проверь доступность {device}.")
        return
    except requests.exceptions.HTTPError as err:
        logger.exception(f"HTTP ошибка: {url}, гугли по следующему коду ответа: {err.response.status_code}")
        return
    except requests.exceptions.RequestException as err:
        logger.exception(f"Что-то пошло не так, необходимо дополнительно разобраться, вот код ошибки: {err}")
        return

    # Получение полной конфигурации и создание директории и файла бэкапа
    full_config = response.text
    current_time = datetime.datetime.today().strftime("%Y_%b_%d")
    backup_path = os.path.join(backup_dir, f"backup_{current_time}")
    os.makedirs(backup_path, exist_ok=True)
    backup_file_path = os.path.join(backup_path, f"{device}_{current_time}.conf")

    # Запись конфигурации в файл
    with open(backup_file_path, "w") as f:
        f.write(full_config)
        print(f"{'#'*20} Backup выполнен {'#'*20}")


def parse_cmd_args():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser()

    # Принимаем аргументы от пользователя из командной строки
    parser.add_argument(
        "--config-file", "-C",
        type=str, required=True,
        help="Путь к файлу конфигурации"
    )
    parser.add_argument(
        "--backup-dir", "-D",
        type=str, required=True,
        help="Директория для сохранения резервных копий",
    )
    parser.add_argument(
        "--enable-warning", "-W",
        action="store_false",
        help="Включить предупреждения безопасности SSL",
    )
    parser.add_argument(
        "--enable-ssl", "-S",
        action="store_true",
        help="Включить проверку SSL"
    )
    return parser.parse_args()


def main():
    # Разбираем аргументы командной строки, переданные пользователем
    args = parse_cmd_args()

    # Читаем файл конфигурации YAML и загружаем его в переменную `devices`
    with open(args.config_file) as f:
        devices = yaml.safe_load(f)

    # Обрабатываем каждое устройство в списке `devices`
    for device in devices:
        print(f"{'#'*20} Подключаюсь к {device['host']} {'#'*20}")
        # Вызыввем функцию и передаем туда аргументы из файла, а так же аргументы args.
        fortios_backup_config(
            device["host"],
            device["token"],
            backup_dir=args.backup_dir,
            enable_warning=args.enable_warning,
            enable_ssl=args.enable_ssl,
        )


if __name__ == "__main__":
    main()
