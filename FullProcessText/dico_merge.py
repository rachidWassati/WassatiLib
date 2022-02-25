import pickle

def loadDicoMerge(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
