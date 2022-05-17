

import csv

class ReadData:

    def __init__(self,path) -> None:
        self.path = path

    def read(self):
        movie_data_nodes = []
        with open(self.path,"r") as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                movie_data_nodes.append(row)
        return movie_data_nodes

