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
        """ sets instance of role to role """
        self._role = role

    def get_role(self):
        """ returns role """
        return self._role

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

    def to_dict(self):
        """ Returns a dictionary with the attributes of the JTF2 Member """
        return dict(
            Service_Number=self._SIN,
            Rank=self._rank,
            Last_Name=self._lname,
            First_Name=self._fname,
            Division=self._division,
            Training_Pay=self._training_pay,
            Deployment_Pay=self._deployment_pay,
            Trainings=self._trainings,

            Role=self._role,
            Missions=self._missions
        )

    def update_soldier_info(self, missions, role, rank, lname, fname, tpay, dpay):
        """ Updates the solder info """
        self._missions = missions
        self._role = self.validate_role(role)
        self._rank = self.validate_rank(rank)
        self._lname = self.validate_lname(lname)
        self._fname = self.validate_fname(fname)
        self._training_pay = self.validate_training_pay(tpay)
        self._deployment_pay = self.validate_deployment_pay(dpay)
