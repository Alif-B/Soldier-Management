import json
from JTF2 import JTF2
from CSOR import CSOR


class OR:
    """ Operation Room Class """

    # Path to the JSON file
    _filepath = "./data.txt"

    def __init__(self):
        """ Constructor for the Operation Room """
        self._available_soldier = {"JTF2": [], "CSOR": []}
        self._deployed_soldier = []
        self._SIN_Numbers = []
        self.read_from_the_file()

    def get_available_soldiers(self):
        """ Getter for the available soldiers """
        return self._available_soldier

    def get_deployed_soldier(self):
        """ Getter for the deployed soldier """
        return self._deployed_soldier

    def add_available_soldier(self, soldier):
        """ Adds a soldier to the available soldier inventory """
        if soldier.get_SIN() in self._SIN_Numbers:
            raise ValueError("A soldier with this SIN number already exists")
        else:
            self._available_soldier[soldier.get_division()].append(soldier)
            self._SIN_Numbers.append(soldier.get_SIN())
            self.write_to_the_file()

    def deploy_JTf2(self, the_operation):
        """ Moves JTF2 soldiers from Available Soldier Inventory to Deployed Soldier Inventory"""
        if len(self._available_soldier['JTF2']) == 0:
            print("JTF2 is already deployed to another mission")
        else:
            for soldier in self._available_soldier["JTF2"]:
                if soldier in the_operation.op_team['JTF2']:
                    print("JTF2 is already deployed on this operation")
                else:
                    self._deployed_soldier.append(soldier)
                    the_operation.op_team['JTF2'].append(soldier)
                    self._available_soldier['JTF2'] = []
                    the_operation.refresh_troops()
        self.write_to_the_file()

    def deploy_CSOR(self, soldier, the_operation):
        """ Moves JTF2 soldiers from Available Soldier Inventory to Deployed Soldier Inventory"""
        if soldier in self._available_soldier['JTF2']:
            print("JTF2 soldiers can not be deployed as CSOR")
        else:
            if soldier in self._deployed_soldier:
                print(f"{soldier.rank} {soldier.lastname} is already deployed")
            else:
                self._deployed_soldier.append(soldier)
                the_operation.op_team['CSOR'].append(soldier)
                self._available_soldier['CSOR'].remove(soldier)
                the_operation.refresh_troops()
        self.write_to_the_file()

    def read_from_the_file(self):
        """ Reads data from the JSON file and coverts them to objects """
        with open(self._filepath, 'r') as JSON_file:
            data = json.load(JSON_file)

        for jtf2 in data['available_JTF2_soldier']:
            temp_soldier = JTF2(SIN=jtf2['Service_Number'], rank=jtf2['Rank'], lname=jtf2['Last_Name'],
                                fname=['First_Name'], role=jtf2['Role'])
            self.add_available_soldier(temp_soldier)

        for csor in data['available_CSOR_soldier']:
            temp_soldier = CSOR(call_sign=csor['Call_Sign'], kills=csor['Kill_Count'], SIN=csor['Service_Number'],
                                rank=csor['Rank'], lname=csor['Last_Name'], fname=csor['First_Name'],
                                tpay=csor['Training_Pay'], dpay=csor['Deployment_Pay'])
            self.add_available_soldier(temp_soldier)

        for soldier in data['deployed_soldier']:
            if soldier['Division'] == 'CSOR':
                temp_soldier = CSOR(call_sign=soldier['Call_Sign'], kills=soldier['Kill_Count'], SIN=soldier['Service_Number'],
                                    rank=soldier['Rank'], lname=soldier['Last_Name'], fname=soldier['First_Name'],
                                    tpay=soldier['Training_Pay'], dpay=soldier['Deployment_Pay'])
                self._deployed_soldier.append(temp_soldier)

            elif soldier['Division'] == 'JTF2':
                temp_soldier = JTF2(SIN=soldier['Service_Number'], rank=soldier['Rank'], lname=soldier['Last_Name'],
                                    fname=['First_Name'], role=soldier['Role'])
                self._deployed_soldier.append(temp_soldier)

    def write_to_the_file(self):
        """ Saves the state of the Operation Room in a txt file in JSON format """
        available_soldier_JTF2 = [soldier.to_dict() for soldier in self._available_soldier['JTF2']]
        available_soldier_CSOR = [soldier.to_dict() for soldier in self._available_soldier['CSOR']]
        deployed_soldier = [soldier.to_dict() for soldier in self._deployed_soldier]

        data = dict(
            available_JTF2_soldier=available_soldier_JTF2,
            available_CSOR_soldier=available_soldier_CSOR,
            deployed_soldier=deployed_soldier
        )

        with open('data.txt', 'w') as JSON_file:
            json.dump(data, JSON_file)

    def get_soldier_by_ID(self, sin):
        SIN = CSOR.validate_SIN(sin)
        for soldier in self._available_soldier['JTF2']:
            if soldier.get_SIN() == SIN:
                return soldier

        for soldier in self._available_soldier['CSOR']:
            if soldier.get_SIN() == SIN:
                return soldier

        for soldier in self._deployed_soldier:
            if soldier.get_SIN() == SIN:
                return soldier

    def remove_soldier(self, SIN):
        """ Removes the soldier from the list and updates the JSON file """
        soldier = self.get_soldier_by_ID(SIN)
        if not soldier:
            raise ValueError('No soldier with the following Service Number exists')
        if soldier in self._available_soldier['JTF2']:
            self._available_soldier['JTF2'].remove(soldier)
        if soldier in self._available_soldier['CSOR']:
            self._available_soldier["CSOR"].remove(soldier)
        if soldier in self._deployed_soldier:
            self._deployed_soldier.remove(soldier)

        self.write_to_the_file()

    def all_soldiers(self):
        """ Get a list of all the solders enrolled in the Canadian Armed Forces """
        all_soldiers = []
        [all_soldiers.append(soldier.to_dict()) for soldier in self._available_soldier['JTF2']]
        [all_soldiers.append(soldier.to_dict()) for soldier in self._available_soldier['CSOR']]
        [all_soldiers.append(soldier.to_dict()) for soldier in self._deployed_soldier]
        return all_soldiers

    def stats(self):
        """ Generate a statistics report """
        return dict(
            available_JTF2=len(self._available_soldier['JTF2']),
            available_CSOR=len(self._available_soldier['CSOR']),
            currently_deployed=len(self._deployed_soldier)
        )

