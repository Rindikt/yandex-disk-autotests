import os
import pytest
from api.disk_client import YandexDiskClient

from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def yandex_disk_client():
    client = YandexDiskClient(token=os.getenv("YANDEX_TOKEN"))
    return client


@pytest.fixture
def folder_name():
    """Просто возвращает строку с именем. Полезно для теста создания."""
    return "TestFolder_AQA"

@pytest.fixture
def created_folder(yandex_disk_client, folder_name):
    """
    Гарантирует, что папка существует перед тестом
    и удаляет её после теста.
    """
    yandex_disk_client.delete_resource(folder_name)
    yandex_disk_client.create_folder(folder_name)

    yield folder_name

    yandex_disk_client.delete_resource(folder_name)
