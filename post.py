from flask import Flask,jsonify,request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app) 
class home(Resource):
    def get(self):
        return jsonify({"input" : "params"})

L = []
class parameters(Resource):
    def post(self):
        req_data = request.form['principal']
        L.append(req_data)
        print(L)
        return jsonify({"values":L})


api.add_resource(home,"/",methods = ['GET'])
api.add_resource(parameters,"/params",methods = ['POST'])

if __name__ == "__main__":
    app.run(debug = True)
