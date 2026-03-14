import requests

class YandexDiskClient:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, token: str):
        self.headers = {
            'Authorization': f'OAuth {token}',
            'Content-Type': 'application/json'
        }

    def create_folder(self, path: str):
        """Метод PUT для создания папки на Яндекс.Диске"""
        params = {'path': path}
        response = requests.put(self.BASE_URL, headers=self.headers, params=params)
        return response

    def get_resource(self, path: str):
        """Метод GET для получения ресурса на Яндекс.Диске"""
        params = {'path': path}
        response = requests.get(self.BASE_URL, headers=self.headers, params=params)
        return response

    def copy_resource(self, from_path: str, to_path: str):
        """Метод POST для копирования файла или папки"""
        copy_url = f"{self.BASE_URL}/copy"
        params = {'from': from_path, 'path': to_path}
        response = requests.post(copy_url, headers=self.headers, params=params)
        return response

    def delete_resource(self, path: str, permanently: bool = True):
        """Метод DELETE для удаления папки или файла"""
        params = {'path': path, 'permanently': str(permanently).lower()}
        response = requests.delete(self.BASE_URL, headers=self.headers, params=params)
        return response