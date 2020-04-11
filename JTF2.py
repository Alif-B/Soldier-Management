from SpecialForcesSoldier import SFS
from peewee import IntegerField, CharField, FixedCharField
from database import db


class JTF2(SFS):
    """ JTF2 Class """
    TRAINING_PAY = IntegerField(default=350)
    DEPLOYMENT_PAY = IntegerField(default=700)
    JTF2_TRAININGS = CharField(default='MMA, Arctic, Desert, Water, Forrest')
    DIVISION = FixedCharField(4, default='JTF2')

    _role = CharField()
    _missions = IntegerField(default=0)

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
            Division=self.DIVISION,
            Training_Pay=self.TRAINING_PAY,
            Deployment_Pay=self.DEPLOYMENT_PAY,
            Trainings=self._trainings,

            Role=self._role,
            Missions=self._missions
        )

    def update_soldier_info(self, missions, role, rank, lname, fname, tpay, dpay):
        """ Updates the solder info """
        self._missions = missions
        self._role = role
        self._rank = rank
        self._lname = lname
        self._fname = fname
        self._training_pay = tpay
        self._deployment_pay = dpay
