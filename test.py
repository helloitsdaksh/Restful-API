from flask import Flask,jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class home(Resource):
    def get(self):
        return "<p>Hello, World!</p>"



class enter(Resource):
    def get(self,num):
        return f"Your number is {num}"

api.add_resource(home,"/",methods=["GET"])
api.add_resource(enter,"/<int:num>")

if __name__ == "__main__":
    app.run(debug=True)