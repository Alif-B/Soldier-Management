class OR:
    """ Operation Room Class """
    def __init__(self):
        """ Constructor for the Operation Room """
        self._available_soldier = {"JTF2": [], "CSOR": []}
        self._deployed_soldier = []

    def get_available_soldiers(self):
        """ Getter for the available soldiers """
        return self._available_soldier

    def get_deployed_soldier(self):
        """ Getter for the deployed soldier """
        return self._deployed_soldier

    def add_available_soldier(self, soldier):
        """ Adds a soldier to the available soldier inventory """
        self._available_soldier[soldier.get_division()].append(soldier)

    def deploy_JTf2(self, the_operation):
        """ Moves JTF2 soldiers from Available Soldier Inventory to Deployed Soldier Inventory"""
        if len(self._available_soldier['JTF2']) == 0:
            print("JTF2 is already deployed to another mission")
        else:
            for soldier in self._available_soldier["JTF2"]:
                if soldier in the_operation.op_team['JTF2']:
                    print("JTF2 is already deployed on this operation")
                else:
                    the_operation.op_team['JTF2'].append(soldier)
                    self._available_soldier['JTF2'] = []
                    the_operation.refresh_troops()

    def deploy_CSOR(self, soldier, the_operation):
        """ Moves JTF2 soldiers from Available Soldier Inventory to Deployed Soldier Inventory"""
        if soldier in self._available_soldier['JTF2']:
            print("JTF2 soldiers can not deployed as CSOR")
        else:
            if soldier in self._deployed_soldier:
                print(f"{soldier.rank} {soldier.lastname} is already deployed")
            else:
                the_operation.op_team['CSOR'].append(soldier)
                self._available_soldier['CSOR'].remove(soldier)
                the_operation.refresh_troops()
