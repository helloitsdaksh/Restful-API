from flask import Flask,jsonify,request
from flask_restful import Api, Resource
from flask_cors import CORS
from typer import params

app = Flask(__name__)
CORS(app)
api = Api(app) 
class home(Resource):
    def get(self):
        return jsonify({"input" : "params"})

L =[]
class parameters(Resource):
    def post(self):
        req_data = request.get_json()
        L.append(req_data)
        return jsonify(L)

api.add_resource(home,"/",methods = ['GET'])
api.add_resource(parameters,"/params",methods = ['POST'])

if __name__ == "__main__":
    app.run(debug = True)
