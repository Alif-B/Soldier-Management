from SpecialForcesSoldier import SFS


class CSOR(SFS):
    """ CSOR Class """
    DIVISION = 'CSOR'

    def __init__(self, call_sign, kills, SIN, rank, lname, fname, tpay, dpay):
        """ instance variables """
        super().__init__(SIN, rank, lname, fname, self.DIVISION, tpay, dpay)
        self._section_call_sign = self.validate_call_sign(call_sign)
        self._kill_count = self.validate_kill_count(kills)

    @property
    def get_kill_count(self):
        """ returns kill count"""
        return self._kill_count

    def set_training_pay(self, new_tpay):
        """ sets instance training pay to new_tpay """
        self._training_pay = new_tpay

    def set_deployment_pay(self, new_dpay):
        """ sets instance deployment pay to new_dpay """
        self._deployment_pay = new_dpay

    @staticmethod
    def validate_call_sign(call_sign):
        """ validates value of call_sign as a string of 3 characters """
        if isinstance(call_sign, str):
            if len(call_sign) != 3:
                raise ValueError("Call sign must be three characters long.")
        else:
            raise TypeError("Call sign must be a string.")
        return call_sign

    @staticmethod
    def validate_kill_count(kills):
        """ validates value of kill count as a number greater than or equal to 0 """
        if isinstance(kills, int):
            if kills < 0:
                raise ValueError("Kill count must be a number equal or greater than 0.")
        else:
            raise TypeError("Kill count must be an integer; not a string or float.")
        return kills

    def expire_training(self, training):
        """ It adds the training to the training inventory """
        if training in self._trainings:
            self._trainings.remove(training)
        else:
            print(f"{self._rank} {self._lname} was never trained on {training}")

    def train(self, training):
        """ Adds training to the training inventory """
        self._trainings.append(self.validate_training(training))
