class SFS:
    def __init__(self, SIN, rank, lname, fname, division, tpay, dpay):
        """ instance variables """
        self._SIN = self.validate_SIN(SIN)
        self._trainings = []
        self._rank = self.validate_rank(rank)
        self._lname = self.validate_lname(lname)
        self._fname = self.validate_fname(fname)
        self._division = self.validate_division(division)
        self._training_pay = self.validate_training_pay(tpay)
        self._deployment_pay = self.validate_deployment_pay(dpay)

    def set_training_pay(self, tpay):
        """ setter that sets training pay equal to tpay argument"""
        self._training_pay = tpay

    def set_deployment_pay(self, dpay):
        """ setter that sets deployment pay equal to dpay argument """
        self._deployment_pay = dpay

    @staticmethod
    def validate_SIN(SIN):
        """ Validates SIN to make sure it is a string of 9 characters """
        if isinstance(SIN, str):
            if len(SIN) != 9:
                raise ValueError("Length of SIN must be 9.")
        else:
            raise TypeError("SIN must be a string; not an int or float.")
        return SIN

    @staticmethod
    def validate_rank(rank):
        """ validates rank to make sure it's a string """
        if isinstance(rank, int) or isinstance(rank, float):
            raise TypeError("Rank must be a string; not an int or float.")
        return rank

    @staticmethod
    def validate_lname(lname):
        """ validates last name to make sure it's a string """
        if isinstance(lname, int) or isinstance(lname, float):
            raise TypeError("Last name must be a string; not an int or float.")
        return lname

    def killed_in_action(self):
        """ When a soldier dies his instance gets deleted """
        del self

    def expire_training(self):
        """ Is not implemented at this level """
        raise NotImplementedError

    def train(self):
        """ Is not implemented at this level """
        raise NotImplementedError

    @staticmethod
    def validate_training(training):
        """ Validate training input """
        if isinstance(training, str):
            return training
        else:
            raise ValueError("Training must be a string")

    def get_SIN(self):
        """ getter that returns the SIN """
        return self._SIN

    def get_rank(self):
        """ getter that returns the rank """
        return self._rank

    def set_rank(self, rank):
        """ setter that sets instance rank to argument rank"""
        self._rank = rank

    def get_last_name(self):
        """ getter that returns the full name of soldier """
        return self._lname

    def get_division(self):
        """ getter that returns the division """
        return self._division

    def get_deployment_pay(self):
        """ getter that returns the deployment pay """
        return self._deployment_pay

    def get_training_pay(self):
        """ getter that returns the training pay """
        return self._training_pay

    @staticmethod
    def validate_fname(fname):
        """ validates first name to make sure it's a string """
        if isinstance(fname, int) or isinstance(fname, float):
            raise TypeError("First name must be a string; not an int or float.")
        return fname

    @staticmethod
    def validate_division(division):
        """ validates division to make sure it's either JTF2 or CSOR """
        if division not in ["JTF2","CSOR"]:
            raise ValueError("Division must be either JTF2 or CSOR.")
        else:
            return division

    @staticmethod
    def validate_training_pay(tpay):
        """ validates training pay to make sure it's a float or int above 0 """
        if isinstance(tpay, float) or isinstance(tpay, int):
            if tpay < 0:
                raise ValueError("Training pay cannot be a negative number.")
        else:
            raise TypeError("Training pay must be an int or float; not a string.")
        return tpay

    @staticmethod
    def validate_deployment_pay(dpay):
        """ validates deployment pay to make sure it's a float or int above 0 """
        if isinstance(dpay, float) or isinstance(dpay, int):
            if dpay < 0:
                raise ValueError("Deployment pay cannot be a negative number.")
        else:
            raise TypeError("Deployment pay must be an int or float; not a string.")
        return dpay

    def get_trainings(self):
        """ Getter for the trainings """
        return self._trainings
