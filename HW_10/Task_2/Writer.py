class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, data):
        with open(self.file_path, 'a') as f:
            f.write(data)
