

from read_data import ReadData
from cartesian_tree import CartesianTree

col_names = ["Name", "Year", "Duration", "Genre", "Rating"]

data_collection = ReadData("movie_data_set.csv")
movie_data = data_collection.read()

index = 0
movie_tree = CartesianTree()
for i in movie_data:
    if index == 0:
        index = 1
        continue
    movie_tree.addNode(i,4)

a = movie_tree.priorityQueue_Sorting(True, 10)

for i in a:
    print("Name: ", i.filmName)
    print("Year: ", i.year)
    print("Genre: ", i.genre)
    print("Duration: ",i.duration)
    print("Rating: ", i.rating)
    print("--------- New Movie ----------")
