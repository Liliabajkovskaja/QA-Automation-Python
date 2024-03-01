class Reader:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None
        self.file_read = False

    def read_file(self):
        if not self.file_read:
            with open(self.__file_path, 'r') as f:
                self.data = f.read()
            self.file_read = True