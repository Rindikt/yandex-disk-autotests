import pytest


def test_create_folder(yandex_disk_client, folder_name):
    """Проверка создания папки (Метод PUT)"""
    response = yandex_disk_client.create_folder(folder_name)
    assert response.status_code == 201


def test_get_folder_info(yandex_disk_client, created_folder):
    """Проверка получения информации о ресурсе (Метод GET)"""
    response = yandex_disk_client.get_resource(created_folder)
    assert response.status_code == 200
    assert response.json()['name'] == created_folder


def test_copy_folder(yandex_disk_client, created_folder):
    """Проверка копирования ресурса (Метод POST)"""
    backup_name = f"{created_folder}_backup"
    try:
        response = yandex_disk_client.copy_resource(created_folder, backup_name)
        assert response.status_code in [201, 202]
    finally:
        yandex_disk_client.delete_resource(backup_name)


def test_delete_folder(yandex_disk_client):
    """Проверка удаления ресурса (Метод DELETE)"""
    name = "for_delete"
    yandex_disk_client.create_folder(name)

    response = yandex_disk_client.delete_resource(name)
    assert response.status_code in [202, 204]