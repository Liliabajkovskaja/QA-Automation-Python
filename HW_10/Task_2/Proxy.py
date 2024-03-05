from HW_10.Task_2.Reader import Reader
from HW_10.Task_2.Writer import Writer
import os


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(self.file_path)
        self.data = None
        self.modified = False
        self.write_data = ''

    def read(self):
        if os.path.getsize(self.file_path) == 0:
            print("File is empty")
            return
        if not self.data or self.modified is True:
            self.data = None
            self.reader.read_file()
            self.data = self.reader.data
            print(f'File is reading: {self.data}')
            self.modified = False
        else:
            print(f'File is NOT reading: {self.data}')

    def write(self, row):

        if str(row) == str(self.write_data):
            print(f"You have re-entered the same data '{row}'")
            self.modified = False
        else:
            self.writer.write_to_file(row)
            self.reader.read_file()
            self.write_data = row
            self.modified = True
            print(f"Data '{row}' has been added to the file.")


proxy_rw = ProxyReaderWriter(file_path='tst.txt')
if __name__ == '__main__':
    proxy_rw.read()  # файл читається, текст повертається
    proxy_rw.read()  # файл НЕ читається, текст повертається
    proxy_rw.write('aa')  # запис в файл відбувається
    proxy_rw.read()  # файл читається, текст повертається
    proxy_rw.write('aa')  # запис в файл НЕ відбувається
    proxy_rw.read()  # файл НЕ читається, текст повертається
    proxy_rw.write('ab')  # запис в файл відбувається
    proxy_rw.read()  # файл читається, текст повертається
