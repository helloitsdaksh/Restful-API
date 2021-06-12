from ssl import ALERT_DESCRIPTION_CERTIFICATE_REVOKED
from flask import Flask,jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app) 


class home(Resource):
    def get(self):
        return jsonify({"API" : "Simple Interest and Compounf Interest Calculator ","Input":["SI","CI"]})

class type(Resource):
    def get(self,A):
        if A =="SI":
            return jsonify({"output":"Simple Interest","input":"Principal Amount"})
        else:
            return
class principal(Resource):
    def get(self,A,P):
        return jsonify({'Principal Amount is :': P})


api.add_resource(home, '/',methods = ['GET'])
api.add_resource(type,'/<string:A>',methods = ['GET'])
api.add_resource(principal,'/<string:A>/<int:P>',methods = ['GET'])

if __name__ == "__main__":
    app.run(debug = True)

#api.add_resource(home,'/')