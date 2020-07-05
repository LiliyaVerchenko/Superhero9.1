import requests
import json
import os

class YaUploader():
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_files_list(self):
        # получаем список файлов в директории
        real = r'C:\New'
        file_list = os.listdir(real)
        # print(file_list)

        # получаем список путей к каждому файлу
        path_list = []
        for file in file_list:
            path = os.path.join(r'C:\New', file)
            path_list.append(path)
        # print(path_list)

        for path1 in path_list:
            # открываем и читаем каждый файл
            with open(path1, encoding='utf-8') as f:
                _file = f.read()
            # получаем ссылку на загрузку файла
            header = {'Authorization': 'OAuth AgAAAAAQNAdaAADLW8BsETCInUdfkaLH2L-AcZE'}
            y_disk = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=/{os.path.basename(path1)}', headers=header)
            href = y_disk.json()['href']
            # загружаем файл на диск по ссылке
            result = requests.put(href, data=_file)
            print(result.text)
        return 'Загрузка файлов прошла успешно'

if __name__ == '__main__':
    uploader = YaUploader(r'C:\New')
    print(uploader.get_files_list())
