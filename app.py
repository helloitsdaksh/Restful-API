from flask import Flask, json, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api=Api(app)
L=[]
class home(Resource):
    def get(self):
        return jsonify({"API" : "Simple Interest and Compounf Interest Calculator ","Input":["SI","CI"]})

class parameters(Resource):   
    def post(self):
        req = request.get_json()
        L.append(req)
        return jsonify(L)

class type(Resource):
    def get(self, t):
        if t == "SI":
            return jsonify({"Type" : t,"Input":"P"})
        elif t=="CI":
            return jsonify({"Type" : t,"Input":"P"})
        else:
            return "Wrong input"

class principal(Resource):
    def get(self, t, p):
        return jsonify({"Type" : t, "P" : p,"Input":"Rate of Interest"})

class rate(Resource):
    def get(self, t, p, r):
        return jsonify({"Type" : t, "P" : p, "Rate of Interest" : r,"Input":"Time"})

class time(Resource):
    def get(self, t, p, r, ti):
        return jsonify({"Type" : t, "P" : p, "Rate of Interest" : r, "Time" : ti,"Input":"="})

class result(Resource):
    def get(self, t, p, r, ti, res):
        if res=="=" and t=="SI":
            return jsonify({t : (p*r*ti)/100})
        else:
            n=12
            exp = n*ti
            value=p*(1+(r/n))
            return jsonify({t : round(pow(value, exp))})

class update(Resource):
    def put(self):
        upd_data = request.get_json()
        id =  upd_data['id']
        for i in L:
            if i["id"] == id:
                i["values"]=upd_data['values']
        return jsonify(L)

api.add_resource(home, '/')
api.add_resource(type, '/<string:t>')
api.add_resource(principal, '/<string:t>/<int:p>')
api.add_resource(rate, '/<string:t>/<int:p>/<int:r>')
api.add_resource(time, '/<string:t>/<int:p>/<int:r>/<int:ti>')
api.add_resource(result, '/<string:t>/<int:p>/<int:r>/<int:ti>/<string:res>')
api.add_resource(parameters, '/param', methods=['POST'])
api.add_resource(update, '/upd', methods=['PUT'])

if __name__=="__main__":
    app.run(debug=True)