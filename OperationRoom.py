import json
from JTF2 import JTF2
from CSOR import CSOR
from SpecialForcesSoldier import SFS


class OR:
    """ Operation Room Class """

    # Path to the JSON file
    # _filepath = "./data.txt"

    def __init__(self):
        """ Constructor for the Operation Room """
        self._available_soldier = {"JTF2": [], "CSOR": []}
        self._deployed_soldier = []
        self._SIN_Numbers = []

    def get_available_soldiers(self):
        """ Getter for the available soldiers """
        return self._available_soldier

    def get_deployed_soldier(self):
        """ Getter for the deployed soldier """
        return self._deployed_soldier

    def add_available_soldier(self, soldier):
        """ Adds a soldier to the available soldier inventory """
        self._available_soldier[soldier.DIVISION].append(soldier)

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
