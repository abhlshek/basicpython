import pickle

dict = {"name": "abhishek", "village": "bhairopur", "collage": "saidpur"}

datafile = open('datastore.txt', 'ab')  # ab = append
pickle.dump(dict, datafile)  # save
datafile.close()

datafile = open('datastore.txt', 'rb')  # rb = read
data = pickle.load(datafile)  # read
print(data)

