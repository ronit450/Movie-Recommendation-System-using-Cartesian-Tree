

from read_data import ReadData
from cartesian_tree import CartesianTree


class Application:

    def __init__(self,column_name: str,sorting_order: bool , top:int) -> None:
        self.column_name = column_name  #column name that is to be sorted
        self.sortingOrder = sorting_order   #ascending or descending
        self.top = top                   #results range. 

    def data_processing(self):

        index_dic = {"Film Name": 0, "Year": 1, "Genre":2,"Duration":3,"Rating":4}
        column_index = index_dic[self.column_name]

        data_collection = ReadData("movie_data_set.csv")
        self.movie_data = data_collection.read()
        index = 0
        self.movie_tree = CartesianTree()
        for i in self.movie_data:
            if index == 0:
                index = 1
                continue
            self.movie_tree.addNode(i,column_index)
        final_sorted_nodes = self.movie_tree.priorityQueue_Sorting(self.sortingOrder, self.top)
        final_movie_lst = []
        for i in final_sorted_nodes:
            temp_lst = [i.filmName,i.year,i.genre,i.duration,i.rating]
            final_movie_lst.append(temp_lst)
        return final_movie_lst


program= Application("Year",True,5)
a = program.data_processing()
print(a)