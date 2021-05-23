from flask import Flask, jsonify
from flask_restful import Api, Resource,abort
from flask import (Blueprint, current_app, flash, jsonify, redirect, request,url_for)
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class home(Resource):
    def get(self):
        x = ['+','-','/','*']
        return {'API':'Calculator','Input': x},201


api.add_resource(home,'/')
if __name__ == "__main__":
    app.run(debug = True)