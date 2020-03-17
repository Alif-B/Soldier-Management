class Operation:
    """ Operation Class """
    def __init__(self, operation_name, location):
        """ instance variables """
        self._operation_name = self.validate_operation_name(operation_name)
        self._location = self.validate_location(location)
        self._op_team = {'JTF2': [], 'CSOR': []}
        self._total_troops = 0
        self._number_of_JTF2 = 0
        self._number_of_CSOR = 0
        self._is_active = False

    def get_operation_name(self):
        """ Getter for the operation name """
        return self._operation_name

    def get_location(self):
        """ Getter for the location """
        return self._location

    def set_location(self, location):
        """ Setter for the location """
        self._location = location

    def get_is_active(self):
        """ Getter for the mission status """
        return self._is_active

    def activate(self):
        """ Activates the mission """
        self._is_active = True

    @property
    def op_team(self):
        """ Getter for the operation team """
        return self._op_team

    def __getitem__(self, item):
        """ Apparently need this to access the dictionary keys """
        return self._op_team[item]

    @op_team.setter
    def op_team(self, team):
        """ Setter for the operation team """
        self._op_team = team

    def get_total_troops(self):
        """ Getter for the total troop deployed in this operation """
        return self._total_troops

    def get_number_of_CSOR(self):
        """ Getter for the number of CSOR soldiers deployed """
        return self._number_of_CSOR

    def get_number_of_JTF2(self):
        """ Getter for the number of JTF2 soldiers deployed """
        return self._number_of_JTF2

    def refresh_troops(self):
        """ Every time we add a soldier, we refresh the number of soldiers """
        self._number_of_JTF2 = len(self._op_team['JTF2'])
        self._number_of_CSOR = len(self._op_team['CSOR'])
        self._total_troops = self._number_of_CSOR + self._number_of_JTF2

    def mission_report(self):
        """ prints mission report """
        if self._is_active:
            print(f"Information on Operation {self._operation_name} is classified.")
        else:
            print(
                f"Operation {self._operation_name} in location: {self._location}.\n"
                f"Total number of troops: {self._total_troops}\n"
                f"Total number of JTF2: {self._number_of_JTF2}\n"
                f"Total number of CSOR: {self._number_of_CSOR}"
            )

    @staticmethod
    def validate_operation_name(operation_name):
        """ validates operation name to ensure it's a string """
        if isinstance(operation_name, int) or isinstance(operation_name, float):
            raise TypeError("Operation name must be a string; not an int or float.")
        else:
            return operation_name

    @staticmethod
    def validate_location(location):
        """ validates location name to ensure it's a string """
        if isinstance(location, int) or isinstance(location, float):
            raise TypeError("Location must be a string. Not an int or float.")
        else:
            return location
