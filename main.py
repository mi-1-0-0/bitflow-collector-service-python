from flask import Flask
from resources.BitFlowCollectorResource import bitflowcollector_api

app = Flask(__name__)
app.register_blueprint(bitflowcollector_api)

def main():
    app.run(host="127.0.0.1", port=8000)
    
if __name__ == '__main__':
    main()