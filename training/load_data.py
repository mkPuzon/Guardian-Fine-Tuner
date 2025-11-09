'''load_data.py

Contains functions to load in custom .json format training data.

Oct 2025
'''
import os
import json

def file_exists(filepath):
    return os.path.exists(filepath)

def dir_exists(filepath):
    return os.path.isdir(filepath)
    
def load_data_split_json(filename, dataset):
    '''Loads .json data from /datasets folder in project top level.
    Parameters:
        filename: str, 
            Name of the file storing the data.
        dataset: str,
            Name of the dataset.
    Returns:
        data: dict,
            Question/label pairs from the given file.'''
    try:
        filepath = os.path.join(fr"C:\Users\madel\Desktop\Guardian-Fine-Tuner\datasets\{dataset}", filename)
        with open(filepath) as fp: # fp: _io.TextIOWrapper
            data = json.load(fp)
        return data["data"]
    except Exception as e:
        print(e)
        
def load_json_dataset(dataset):
    '''Returns three Python dicts'''
    train_set = load_data_split_json(filename="train.json", dataset=dataset)
    test_set = load_data_split_json(filename="test.json", dataset=dataset)
    val_set = load_data_split_json(filename="val.json", dataset=dataset)
    return train_set, test_set, val_set
            
if __name__ == "__main__":
    pass