from flask import Blueprint, request
from readers.BitFlowCollectorCSVReader import *
from utils.PropertiesReader import readproperty

bitflowcollector_api = Blueprint('bitflowcollector_api', __name__)

path = readproperty("PATH")


@bitflowcollector_api.route("/size", methods=['GET'])
def getsize():
    try:
        return getcsvfilesize(path) + " byte(s)"
    except Exception as e:
        return "Error occurred: " + str(e)  

@bitflowcollector_api.route("/lines", methods=['GET'])    
def getlinenumbers():
    try:
        return str(getcsvrecordcount(path))
    except Exception as e:
        return "Error occurred: " + str(e)
@bitflowcollector_api.route("/head", methods=['GET'])
def getfirstlines():
    try:
        num = request.args.get("num")
        num = long(num) if num is not None else None
        num = 1 if num is None else num
        return getfirstxlines(path, num)
    except Exception as e:
        return "Error occurred: " + str(e)
@bitflowcollector_api.route("/tail", methods=['GET'])
def getlastlines():
    try:
        num = request.args.get("num")
        num = long(num) if num is not None else None
        num = 1 if num is None else num
        return getlastxlines(path, num)
    except Exception as e:
        return "Error occurred: " + str(e)