print('''python program #24
Hashir - June 1 2018
This program is meant to introduce the pickle module and save some data in a file
''')
import pickle

save_data = ['Hashir','18','Male','168cm','115lbs']

save_file = open('favorites.dat','wb')
pickle.dump(save_data, save_file)
save_file.close()

load_file = open('favorites.dat','rb')
load_data = pickle.load(load_file)
load_file.close()

print(load_data)
