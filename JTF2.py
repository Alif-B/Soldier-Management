from SpecialForcesSoldier import SFS


class JTF2(SFS):
    """ JTF2 Class """
    TRAINING_PAY = 250
    DEPLOYMENT_PAY = 700
    JTF2_TRAININGS = ('MMA', 'Arctic', 'Desert', 'Water', 'Forrest')
    DIVISION = 'JTF2'

    def __init__(self, SIN, rank, lname, fname, role):
        """ instance variables """
        super().__init__(SIN, rank, lname, fname, self.DIVISION, self.TRAINING_PAY, self.DEPLOYMENT_PAY)
        self._role = self.validate_role(role)
        self._missions = 0

    def get_missions(self):
        """ returns number of missions """
        return self._missions

    def set_role(self, role):
        """ returns role """
        self._role = role

    def set_training_pay(self):
        """ sets instance training pay to class variable TRAINING_PAY """
        self._training_pay = self.TRAINING_PAY

    def set_deployment_pay(self):
        """ sets instance deployment pay to class variable DEPLOYMENT_PAY """
        self._deployment_pay = self.DEPLOYMENT_PAY

    @staticmethod
    def validate_role(role):
        """ validates role to ensure it's a string"""
        if isinstance(role, int) or isinstance(role, float):
            raise ValueError("Role must be a string.")
        else:
            return role

    def expire_training(self):
        """ JTF2 Have a certain training list so all the trainings expire together """
        [self._trainings.remove(i) for i in self._trainings]

    def train(self):
        """ JTF2 Soldiers have a required list of trainings so they train on them together """
        [self._trainings.append(i) for i in self.JTF2_TRAININGS]
