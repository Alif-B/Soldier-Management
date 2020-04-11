from flask import Flask, jsonify, make_response, request
from OperationRoom import OR
from CSOR import CSOR
from JTF2 import JTF2
import json
import requests

app = Flask(__name__)
CAF = OR()


@app.route('/CAF/csor', methods=['POST'])
def new_csor():
    """ Creates a CSOR soldier and adds it to the available soldier list """
    data = request.json
    try:
        soldier = CSOR(_SIN=data['Service_Number'], _trainings=data['Trainings'], _rank=data['Rank'],
                       _lname=data['Last_Name'], _fname=data['First_Name'], _training_pay=data['Training_Pay'],
                       _deployment_pay=data['Deployment_Pay'], _section_call_sign=data['Section_Call_Sign'])
        soldier.save(force_insert=True)
        return make_response(f"{data['Service_Number']}", 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route('/CAF/jtf2', methods=['POST'])
def new_jtf2():
    """ Creates a JTF2 soldier and adds it to the available soldier list """
    try:
        data = request.json
        soldier = JTF2(_SIN=data['Service_Number'], _rank=data['Rank'], _lname=data['Last_Name'],
                       _fname=data['First_Name'], _role=data['Role'], _trainings=data['Trainings'])
        soldier.save(force_insert=True)
        return make_response(f"{data['Service_Number']}", 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route('/CAF/soldier/all')
def show_all_soldier():
    """ Show all the soldiers in the inventory """
    csor = CSOR.select()
    csor = [soldier.to_dict() for soldier in csor]
    jtf2 = JTF2.select()
    jtf2 = [soldier.to_dict() for soldier in jtf2]

    soldiers = {'CSOR': csor, 'JTF2': jtf2}
    return jsonify(soldiers)


@app.route('/CAF/soldier/stats', methods=['GET'])
def get_stats():
    stats = CAF.stats()
    return jsonify(stats)


@app.route('/CAF/soldier/<SIN>', methods=['PUT'])
def update_soldier(SIN):
    """ Finds a soldier by the service number and updates the rest of the info """
    data = request.json
    soldier = CSOR.get_or_none(CSOR._SIN == SIN)
    if soldier:
        soldier._rank = data['Rank']
        soldier._lname = data['Last_Name']
        soldier._fname = data['First_Name']
        soldier._training_pay = data['Deployment_Pay']
        soldier._deployment_pay = data['Training_Pay']
        soldier._trainings = data['Trainings']
        soldier._section_call_sign = data['Section_Call_Sign']

    if not soldier:
        try:
            soldier = JTF2.get_or_none(JTF2._SIN == SIN)
            soldier._rank = data['Rank']
            soldier._lname = data['Last_Name']
            soldier._fname = data['First_Name']
            soldier._role = data['Role']
            if not soldier:
                raise KeyError("No soldier with the provided Service Number exist")
        except KeyError as e:
            make_response(str(e), 400)

    soldier.save()
    return make_response("", 200)


@app.route('/CAF/soldier/<SIN>', methods=['DELETE'])
def delete_soldier(SIN):
    try:
        deleted_CSOR = CSOR.delete().where(CSOR._SIN == SIN).execute()
        deleted_JTF2 = JTF2.delete().where(JTF2._SIN == SIN).execute()
        if (deleted_CSOR + deleted_JTF2) == 0:
            raise ValueError('Nobody with the provided service number exist')
        return make_response("", 200)
    except ValueError as e:
        return make_response(str(e), 404)


@app.route('/CAF/soldier/<SIN>', methods=['GET'])
def find_soldier(SIN):
    """ Find a specific soldier by their service number """
    try:
        soldier = CSOR.get_or_none(CSOR._SIN == SIN)
        if not soldier:
            soldier = JTF2.get_or_none(JTF2._SIN == SIN)
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
