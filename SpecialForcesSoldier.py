from peewee import FixedCharField, CharField, IntegerField, Model
from database import db


class SFS(Model):
    """ Abstract soldier class """
    _SIN = FixedCharField(9, primary_key=True)
    _trainings = CharField(null=True)
    _rank = CharField()
    _lname = CharField()
    _fname = CharField()

    def killed_in_action(self):
        """ When a soldier dies his instance gets deleted """
        del self

    def expire_training(self):
        """ Is not implemented at this level """
        raise NotImplementedError

    def train(self):
        """ Is not implemented at this level """
        raise NotImplementedError

    def to_dict(self):
        """ Is not implemented at this level """
        raise NotImplementedError

    class Meta:
        database = db
