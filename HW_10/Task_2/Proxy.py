from HW_10.Task_2.Reader import Reader
from HW_10.Task_2.Writer import Writer



class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.data = None

    def read(self):
        if self.data is None:
            self.reader.read_file()
            self.data = self.reader.data
            print(f'File is reading: {self.data}')
        else:
            print(f'File is NOT reading: {self.data}')

    def write(self, row):
        self.read()
        if row == self.data:
            print(f"You have re-entered the same data '{row}'")
        else:
            writer = Writer(self.file_path)
            writer.write_to_file(row)
            self.data = row
            print(f"Data '{row}' has been added to the file.")


proxy_rw = ProxyReaderWriter(file_path='tst.txt')

if __name__ == '__main__':
    proxy_rw.read()  # файл читаеться, текст повертаеться
    proxy_rw.read()  # файл НЕ читаеться, текст повертаеться
    proxy_rw.write('aa')  # запис в файл відбуваеться
    proxy_rw.read()  # файл читаеться, текст повертаеться
    proxy_rw.write('aa')  # запис в файл НЕ відбуваеться
    proxy_rw.read()  # файл НЕ читаеться, текст повертаеться
    proxy_rw.write('ab')  # запис в файл відбуваеться
    proxy_rw.read()  # файл читаеться, текст повертаеться
    proxy_rw.write('aa')