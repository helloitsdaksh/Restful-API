from flask import Flask, jsonify
from flask_restful import Api, Resource,abort
from flask import (Blueprint, current_app, flash, jsonify, redirect, request,url_for)
import pandas as pd
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
api = Api(app)