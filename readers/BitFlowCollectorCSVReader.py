import csv
import os

def __init__(self, path):
    self.path = path
    
def getcsvfilesize(path):
    return str(os.stat(path).st_size)

def getfirstxlines(path, numberoflines):
    if numberoflines < 0:
        raise Exception('Number of lines must be greater than or equal to 0.')  
    total = getcsvrecordcount(path)
    numberoflines = numberoflines if numberoflines <= total else total
    csv_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for i in range(0, numberoflines):
            csv_list.append(reader.next())    
    return str(csv_list)
    
def getlastxlines(path, numberoflines):
    if numberoflines < 0:
        raise Exception('Number of lines must be greater than or equal to 0.')    
    total = getcsvrecordcount(path)
    numberoflines = numberoflines if numberoflines <= total else total
    csv_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        i = 1        
        skiplines = total - numberoflines
        for i in range(1, skiplines):
            reader.next()
        for i in range(skiplines, total):
            csv_list.append(reader.next())     
    return str(csv_list)
    
def getcsvrecordcount(path):
    count = 0
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter = ",")
        count = len(list(reader))
    return count