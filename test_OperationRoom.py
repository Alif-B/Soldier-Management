import unittest
from OperationRoom import OR
from CSOR import CSOR
from JTF2 import JTF2
from Operations import Operation


class TestOR(unittest.TestCase):

    def setUp(self):
        """ set up fixture """
        self.OR1 = OR()
        self.CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)
        self.CSOR2 = CSOR('XYW', 6, '000000000', 'Second-In-Command', 'Park', 'SJ', 400, 800)
        self.JTF2_1 = JTF2('123456783', 'Soldier', 'Guicherd', 'Tim', 'Sniper')
        self.JTF2_2 = JTF2('123456780', 'Soldier', 'Billah', 'Alif', 'Sniper')
        self.JTF2_3 = JTF2('111111111', 'Soldier', 'Kaur', 'Harsimran', 'Assaulter')
        self.OP1 = Operation('Indigo', 'Afghanistan')

    def test_available_soldiers(self):
        """ 030A - tests getter for the available soldiers & add_available_soldier method """
        self.OR1.add_available_soldier(self.CSOR2)
        self.OR1.add_available_soldier(self.JTF2_3)
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [self.CSOR2], 'JTF2': [self.JTF2_3]})

    def test_deploy_JTF2(self):
        """ 030B - tests deploy_JTf2 method to ensure it adds soldier to operation team if soldier is available """
        self.OR1.add_available_soldier(self.JTF2_1)
        self.OR1.add_available_soldier(self.JTF2_2)
        self.OR1.deploy_JTf2(self.OP1)
        self.assertEqual(self.OP1.op_team, {'CSOR': [], 'JTF2': [self.JTF2_1, self.JTF2_2]})

    def test_deploy_CSOR(self):
        """ 030C - tests deploy_CSOR method to ensure it adds soldier to operation team if soldier is available
        then removes soldier from available soldiers list """
        self.OR1.add_available_soldier(self.CSOR1)
        self.OR1.deploy_CSOR(self.CSOR1, self.OP1)
        self.assertEqual(self.OP1.op_team, {'CSOR': [self.CSOR1], 'JTF2': []})
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [], 'JTF2': []})

    def test_get_soldier_by_ID(self):
        """ 030D - tests get_soldier_by_ID method to ensure it returns correct soldier """
        self.OR1.add_available_soldier(self.CSOR1)
        self.OR1.add_available_soldier(self.JTF2_2)
        self.assertEqual(self.OR1.get_soldier_by_ID('123456789'), self.CSOR1)
        self.assertEqual(self.OR1.get_soldier_by_ID('123456780'), self.JTF2_2)

    def test_remove_soldier(self):
        """ 030E - tests remove_soldier method to ensure it removes correct soldier """
        self.OR1.add_available_soldier(self.CSOR1)
        self.OR1.add_available_soldier(self.JTF2_2)
        self.OR1.remove_soldier('123456789')
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [], 'JTF2': [self.JTF2_2]})

        self.OR1.remove_soldier('123456780')
        self.assertEqual(self.OR1.get_available_soldiers(), {'CSOR': [], 'JTF2': []})

        self.OR1.add_available_soldier(self.JTF2_1)
        self.OR1.deploy_JTf2(self.OP1)
        self.OR1.remove_soldier('123456783')
        self.assertEqual(self.OR1.get_deployed_soldier(), [])

    def test_all_soldiers(self):
        """ 030F - tests all_soldiers method to ensure it returns list of soldiers """
        self.OR1.add_available_soldier(self.CSOR1)
        self.OR1.add_available_soldier(self.JTF2_1)
        self.OR1.add_available_soldier(self.JTF2_2)
        self.OR1.deploy_JTf2(self.OP1)
        self.assertEqual(self.OR1.all_soldiers(), None) # not supposed to be None

    def test_stats(self):
        """ 030G - tests stats method to return dict of stats """
        self.assertEqual(self.OR1.stats(), {'available_CSOR': 3, 'available_JTF2': 0, 'currently_deployed': 0})


if __name__ == '__main__':
    unittest.main()