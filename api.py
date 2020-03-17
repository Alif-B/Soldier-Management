from flask import Flask, jsonify, make_response, request
from OperationRoom import OR
from CSOR import CSOR
from JTF2 import JTF2
import json

app = Flask(__name__)
CAF = OR()


@app.route('/CAF/csor', methods=['POST'])
def new_csor():
    """ Creates a CSOR soldier and adds it to the available soldier list """
    data = request.json
    try:
        soldier = CSOR(call_sign=data['Call_Sign'], kills=data['Kill_Count'], SIN=data['Service_Number'],
                       rank=data['Rank'], lname=data['Last_Name'], fname=data['First_Name'],
                       tpay=data['Training_Pay'], dpay=data['Deployment_Pay'])
        CAF.add_available_soldier(soldier)
        return make_response(f"{data['Service_Number']}", 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route('/CAF/jtf2', methods=['POST'])
def new_jtf2():
    """ Creates a JTF2 soldier and adds it to the available soldier list """
    data = request.json
    try:
        soldier = JTF2(SIN=data['Service_Number'], rank=data['Rank'], lname=data['Last_Name'],
                       fname=data['First_Name'], role=data['Role'])
        CAF.add_available_soldier(soldier)
        return make_response(f"{data['Service_Number']}", 200)
    except ValueError as e:
        return make_response(str(e), 400)


@app.route('/CAF/soldier/all')
def show_all_soldier():
    """ Show all the soldiers in the inventory """
    soldiers = CAF.all_soldiers()
    return jsonify(soldiers)


@app.route('/CAF/soldier/stats', methods=['GET'])
def get_stats():
    stats = CAF.stats()
    return jsonify(stats)


@app.route('/CAF/soldier/<SIN>', methods=['PUT'])
def update_soldier(SIN):
    """ Finds a soldier by the service number and updates the rest of the info """
    soldier = CAF.get_soldier_by_ID(SIN)
    data = request.json
    try:
        if not soldier:
            raise ValueError("No soldier with the following the Service Number exists")
        if soldier.get_division() == "CSOR":
            soldier.update_soldier_info(call_sign=data['Call_Sign'], kills=data['Kill_Count'], rank=data['Rank'],
                                        lname=data['Last_Name'], fname=data['First_Name'], tpay=data['Training_Pay'],
                                        dpay=data['Deployment_Pay'])
        else:
            soldier.update_soldier_info(role=data['Role'], missions=data['Missions'], rank=data['Rank'],
                                        lname=data['Last_Name'], fname=data['First_Name'], tpay=data['Training_Pay'],
                                        dpay=data['Deployment_Pay'])
        CAF.write_to_the_file()
        return make_response("", 200)
    except ValueError as e:
        return make_response(str(e), 404)
    except KeyError:
        return make_response("Wrong key name! Maybe you've entered wrong attributes for the soldier type", 400)


@app.route('/CAF/soldier/<SIN>', methods=['DELETE'])
def delete_soldier(SIN):
    try:
        CAF.remove_soldier(SIN)
        return make_response("", 200)
    except ValueError as e:
        return make_response(str(e), 404)


@app.route('/CAF/soldier/<SIN>', methods=['GET'])
def find_soldier(SIN):
    """ Find a specific soldier by their service number """
    try:
        soldier = CAF.get_soldier_by_ID(SIN)
        if not soldier:
            raise ValueError("No soldier with the following the Service Number exists")
        return jsonify(soldier.to_dict())
    except ValueError as e:
        return make_response(str(e), 404)


@app.route('/CAF/soldier/all/<division>', methods=['GET'])
def find_soldiers_by_division(division):
    unit = []
    try:
        army = CAF.all_soldiers()
        if division != 'JTF2' and division != 'CSOR':
            raise ValueError('Division must either be JTF2 or CSOR')

        for soldier in army:
            if soldier['Division'] == division:
                unit.append(soldier)
        return jsonify(unit)
    except ValueError as e:
        return make_response(str(e), 400)


if __name__ == "__main__":
    app.run()
