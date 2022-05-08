import os.path
import shutil

src_r = r'D:\Testing\Excel_worker\Excel_file\Ex'
src_o = r'D:\Testing\Excel_worker\Excel_file\cy21hint_regression.xlsx'

class FileFolderGenerator:
    def __init__(self, path_from, path_to):
        self.path_from = path_from
        self.path_to = path_to

    def generate_files(self, count_files):

        for item in range(1, count_files+1):
            strPath = os.path.split(self.path_from)
            base_name, ext = os.path.splitext(strPath[1])
            new_file_name = base_name + '_' + str(item) + ext
            newPath = os.path.join(self.path_to, new_file_name)
            shutil.copy(self.path_from, newPath)
            print('Finish')

worker = FileFolderGenerator(src_o, src_r)
worker.generate_files(10)