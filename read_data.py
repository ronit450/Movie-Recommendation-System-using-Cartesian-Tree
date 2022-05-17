

import csv

class ReadData:

    def __init__(self,path) -> None:
        '''Constructor for Read Data class. 

        Args:
        - self: mandatory reference to this object.
        - elements: path to the csv file.

        Returns:
        None
        '''
        self.path = path

    def read(self):
        '''Reads data from csv file.

        Args:
        - self: mandatory reference to this object.
        - elements: 

        Returns:
        All the data from csv file. 
        '''
        movie_data_nodes = []
        with open(self.path,"r") as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                movie_data_nodes.append(row)
        return movie_data_nodes

