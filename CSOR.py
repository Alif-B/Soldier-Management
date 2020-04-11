from SpecialForcesSoldier import SFS
from peewee import FixedCharField, IntegerField
from database import db


class CSOR(SFS):
    """ CSOR Class """
    DIVISION = FixedCharField(4, default='CSOR')

    _training_pay = IntegerField()
    _deployment_pay = IntegerField()
    _section_call_sign = FixedCharField(3)
    _kill_count = IntegerField(default=0)

    def expire_training(self, training):
        """ It adds the training to the training inventory """
        if training in self._trainings:
            self._trainings.remove(training)
        else:
            print(f"{self._rank} {self._lname} was never trained on {training}")

    def train(self, training):
        """ Adds training to the training inventory """
        self._trainings.append(self.validate_training(training))

    def to_dict(self):
        """ Returns a dictionary with the attributes of the CSOR Member """

        return dict(
            Service_Number=self._SIN,
            Rank=self._rank,
            Last_Name=self._lname,
            First_Name=self._fname,
            Division=self.DIVISION,
            Training_Pay=self._training_pay,
            Deployment_Pay=self._deployment_pay,
            Trainings=self._trainings,

            Call_Sign=self._section_call_sign,
            Kill_Count=self._kill_count
        )

    def update_soldier_info(self, call_sign, kills, rank, lname, fname, tpay, dpay):
        """ Updates the solder info """
        self._section_call_sign = call_sign
        self._kill_count = kills
        self._rank = rank
        self._lname = lname
        self._fname = fname
        self._training_pay = tpay
        self._deployment_pay = dpay
