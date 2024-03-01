from HW_10.Task_2.Reader import Reader
from HW_10.Task_2.Writer import Writer


class ProxyReaderWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.data = None

    def read(self):
        if not self.data:
            self.reader.read_file()
            self.data = self.reader.data

    def write(self, row):
        self.read()
        if row == self.data:
            print(f"You have re-entered the same data '{row}'")
        else:
            Writer.write_to_file(self.file_path, row)
            self.data = row
            print(f"Data '{row}' has been added to the file.")


proxy_rw = ProxyReaderWriter(file_path='Test.txt')

if __name__ == '__main__':
    proxy_rw.write('asd')  # буде запис
    proxy_rw.write('asd')  # не буде запису
    proxy_rw.write('asd2')  # буде запис
    proxy_rw.write('asd')  # буде запис
