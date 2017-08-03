import os
def readproperty(propertyname):
    file_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)), 'config.properties')
    properties = dict(line.strip().split('=') for line in open(file_path) if not line.startswith('#') and not line.startswith('\n')) 
    return properties[propertyname].strip()