class TxtAdaptor:
    @staticmethod
    def csv_to_xml(file_path):
        with open(file_path) as f:
            lines = f.readlines()

            header = [k.strip() for k in lines[0].split(',')]
            rows = lines[1:]
            for row in rows:
                row = row.strip().split(',')
                for i in range(len(header)):
                    print(f'<{header[i]}>{row[i]}</{header[i]}>')


TxtAdaptor.csv_to_xml('tst_file.txt')
