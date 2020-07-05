import requests
import json
import os

class YaUploader():
    def __init__(self, token: str, file_path: str):
        self.headers = {'Accept': 'application/json', 'Authorization': token}
        self.file_path = file_path

    def upload(self):
        # получаем список файлов в директории
        file_list = os.listdir(my_file_path)

        # получаем список путей к каждому файлу
        path_list = []
        for file in file_list:
            path = os.path.join(my_file_path, file)
            path_list.append(path)

        for path1 in path_list:
            # открываем и читаем каждый файл
            with open(path1, encoding='utf-8') as f:
                _file = f.read()
            # получаем ссылку на загрузку файла
            y_disk = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=/{os.path.basename(path1)}', headers=self.headers)
            put_url = y_disk.json()['href']
            # загружаем файл на диск по ссылке
            result = requests.put(put_url, data=_file)
            # print(result.text)
        return 'Загрузка файлов прошла успешно'

if __name__ == '__main__':
    token = 'OAuth AgAAAAAQNAdaAADLW8BsETCInUdfkaLH2L-AcZE'
    my_file_path = r'C:\New'
    uploader = YaUploader(token, my_file_path)
    print(uploader.upload())
