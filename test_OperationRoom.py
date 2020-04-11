import unittest
from os import remove

from OperationRoom import OR
from CSOR import CSOR
from JTF2 import JTF2
from Operations import Operation
from peewee import SqliteDatabase

db = SqliteDatabase('test_OR.sqlite')


class TestOR(unittest.TestCase):
    """ Unit tests for the Operation Room (OR) Class """

    def setUp(self):
        """ set up fixture """
        db.connect()
        db.create_tables([JTF2, CSOR])
        self.OR1 = OR()

        self.CSOR1 = CSOR(_SIN='A23456789', _rank='General', _lname='Hashimi', _fname='Shabnam',
                              DIVISION='CSOR', _training_pay=500, _deployment_pay=900, _trainings='Training1',
                              _section_call_sign='ABC', _kill_count=3)
        self.CSOR1.save()
        self.JTF2_1 = JTF2(_SIN='A55555555', _rank='General', _lname='Chalamet', _fname='Timothee',
                               DIVISION='JTF2', TRAINING_PAY=350, DEPLOYMENT_PAY=700, _trainings='Training1', _role='Leader',
                               _missions=2)
        self.JTF2_1.save()
        self.JTF2_2 = JTF2(_SIN='A00000000', _rank='Soldier', _lname='Prinze Jr.', _fname='Freddie',
                           DIVISION='JTF2', TRAINING_PAY=350, DEPLOYMENT_PAY=700, _trainings='Training1',
                           _role='Sniper',
                           _missions=2)
        self.JTF2_2.save()
        self.OP1 = Operation('Indigo', 'Afghanistan')

    def test_available_soldiers(self):
        """ 030A - tests to see if soldiers get added to database """
        self.assertIsNotNone(self.OR1.get_available_soldiers())

    def test_deploy_JTF2(self):
        """ 030B - tests deploy_JTf2 method to ensure it adds soldier to operation team if soldier is available """
        self.OR1.add_available_soldier(self.JTF2_1)
        self.OR1.add_available_soldier(self.JTF2_2)
        self.OR1.deploy_JTf2(self.OP1)
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [],'JTF2': []})

    def test_deploy_CSOR(self):
        """ 030C - tests deploy_CSOR method to ensure it adds soldier to operation team if soldier is available
        then removes soldier from available soldiers list """
        self.OR1.add_available_soldier(self.CSOR1)
        self.OR1.deploy_CSOR(self.CSOR1, self.OP1)
        self.assertEqual(self.OP1.op_team, {'CSOR': [self.CSOR1], 'JTF2': []})
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [], 'JTF2': []})

    def tearDown(self):
        """ tear down fixture """
        db.drop_tables([JTF2, CSOR])
        db.close()
        remove('test_OR.sqlite')


if __name__ == '__main__':
    unittest.main()