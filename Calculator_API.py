from flask import Flask, jsonify
from flask_restful import Api, Resource,abort
from flask import (Blueprint, current_app, flash, jsonify, redirect, request,url_for)
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)
#home shows list of operators
class home(Resource):
    def get(self):
        x = ['+','-','/','*']
        return {'API':'Calculator','Input': x},201
#asks user for input(number1)
class operator(Resource):
    def get(self,A):
        func = A
        return {'API':'Calculator','operator': func,'Input':'Enter Number 1:'}
#asks user for input(number2)
class number1(Resource):
    def get(self,A,num1):
        number_one = num1
        return {'API':'Calculator','Number_1':number_one,'Input':'Enter Number 2:'}
#finally shows output of the two numbers in a json format
class number2(Resource):
    def get(self,A,num1,num2):
        number_one = num1
        number_two = num2
        output = 0
        if A == '+':
            output = number_one + number_two
        elif A == '-':
            output = number_one + number_two
        elif A == '/':
            output = number_one + number_two
        elif A == '*':
            output = number_one + number_two
        return {'API':'Calculator','Number_1':number_one,'Number_2':number_two,'Output':output}


api.add_resource(home,'/')
api.add_resource(operator,'/<string:A>')
api.add_resource(number1,'/<string:A>/<int:num1>')
api.add_resource(number2,'/<string:A>/<int:num1>/<int:num2>')


if __name__ == "__main__":
    app.run(debug = True)