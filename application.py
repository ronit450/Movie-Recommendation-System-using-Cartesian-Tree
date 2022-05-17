

from read_data import ReadData
from cartesian_tree import CartesianTree

col_names = ["Film", "Genre", "Lead Studio", "IMDB", "Year"]

data_collection = ReadData("movies.csv")
movie_data = data_collection.read()

index = 0
movie_tree = CartesianTree()
for i in movie_data:
    if index == 0:
        index = 1
        continue
    movie_tree.addNode(i,3)

a = movie_tree.priorityQueue_Sorting(False, 5)
for i in a:
    print(i.filmName, i.genre, i.LeadStudio, i.Imbd, sep = ", ")

