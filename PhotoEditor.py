from photoeditor_config import (
    FILTERS,
    FILTERS_DICT,
    IMG_FOLDER,
    OUTPUT_FOLDER,
    SELECT_FILTER,
)
import os
from PIL import Image, ImageFilter
import time


def convert_img(filtered_img):
    return filtered_img.convert('RGB')


def filetype_save(converted_img, save_path, file):
    if file.endswith('.jpg'):
        converted_img.save(save_path, 'jpeg')
    converted_img.save(save_path, 'png')
    print(f'{file} is ready!')


class PhotoEditor:
    def __init__(self, filters, filters_dict, img_folder, output_folder, select_filter):
        self.filters = filters
        self.filters_dict = filters_dict
        self.img_folder = img_folder
        self.output = output_folder
        self.select_filter = select_filter

    def run(self):
        print("Looking for Images...")
        self.create_folder()
        print(f'Selected filter is: {self.get_mode()}')
        list_files = self.get_files()
        print(f'Found {len(list_files)} Images!')
        self.apply_filter(list_files)

    def apply_filter(self, files):
        if len(files) != 0:
            for file in files:
                file_path = f'{self.img_folder}\\{file}'
                img = Image.open(file_path)
                if img.size > (500, 500):
                    img.thumbnail((500, 500))
                attrib = getattr(ImageFilter, self.get_mode())
                filtered_img = img.filter(attrib)
                converted_img = convert_img(filtered_img)
                save_path = f"{self.output}\\{file}"
                filetype_save(converted_img, save_path, file)
            print('Opening folder...')
            time.sleep(2)
            os.startfile(self.output)
        else:
            print(f'No Images were found at the location - {self.img_folder}')
            print('Stopping Script...')

    def get_mode(self):
        return self.filters_dict[f'{self.select_filter}']

    def get_files(self):
        files = []
        for items in os.listdir(self.img_folder):
            if items.endswith(('.jpg', '.png')):
                files.append(items)
        return files

    def create_folder(self):
        if not os.path.exists(self.output):
            return os.makedirs(self.output)


if __name__ == '__main__':
    runner = PhotoEditor(FILTERS, FILTERS_DICT, IMG_FOLDER, OUTPUT_FOLDER, SELECT_FILTER)
    runner.run()
