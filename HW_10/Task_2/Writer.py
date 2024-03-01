class Writer:
    @staticmethod
    def write_to_file(file_path, data):
        with open(file_path, 'a') as f:
            f.write(data +'\n')
