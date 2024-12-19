import pickle

data = {"name": "abhishek", "village": "bhairopur", "collage": "saidpur"}
datafile = open(datasture.txt, "ab")
pickle.dump(data, datafile)
datafile.close()

datafile = open("datasture.txt", "rb")
data = pickle.load(datafile)
print(data)
