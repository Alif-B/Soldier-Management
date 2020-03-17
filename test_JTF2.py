import unittest
from JTF2 import JTF2


class TestJTF2(unittest.TestCase):

    def setUp(self):
        """ set up fixture """
        self.JTF2_1 = JTF2('123456789', 'General', 'Hashimi', 'Shabnam', 'Leader')

    def test_constructor(self):
        """ 020A - tests valid cases for constructor """
        self.assertIsNotNone(self.JTF2_1)
        self.assertIsInstance(self.JTF2_1, JTF2)

    def test_constructor_invalid(self):
        """ 020B - tests invalid cases for constructor """
        with self.assertRaises(TypeError):
            JTF2_1 = JTF2(123456789, 'General', 'Hashimi', 'Shabnam', 'Leader')
        with self.assertRaises(ValueError):
            JTF2_1 = JTF2('12345678910', 'General', 'Hashimi', 'Shabnam', 'Leader')
        with self.assertRaises(TypeError):
            JTF2_1 = JTF2('123456789', 1, 'Hashimi', 'Shabnam', 'Leader')
        with self.assertRaises(TypeError):
            JTF2_1 = JTF2('123456789', 'General', 1, 'Shabnam', 'Leader')
        with self.assertRaises(TypeError):
            JTF2_1 = JTF2('123456789', 'General', 'Hashimi', 1, 'Leader')
        with self.assertRaises(ValueError):
            JTF2_1 = JTF2('123456789', 'General', 'Hashimi', 'Shabnam', 1)

    def test_get_missions(self):
        """ 020C - tests get_mission method """
        self.assertEqual(self.JTF2_1.get_missions(), 0)

    def test_role(self):
        """ 020D - tests validate_role method with valid parameter and getter get_role method """
        self.assertEqual(self.JTF2_1.get_role(), 'Leader')
        self.assertEqual(self.JTF2_1.validate_role('Second-In-Charge'), 'Second-In-Charge')

    def test_training_pay(self):
        """ 020E - tests setter and getter for training pay """
        self.assertEqual(self.JTF2_1.get_training_pay(), 250)

    def test_deployment_pay(self):
        """ 020F - tests setter and getter for deployment pay """
        self.assertEqual(self.JTF2_1.get_deployment_pay(), 700)

    def test_train(self):
        """ 020G - tests train method to ensure all trainings are added """
        self.JTF2_1.train()
        self.assertEqual(self.JTF2_1.get_trainings(), ['MMA', 'Arctic', 'Desert', 'Water', 'Forrest'])

    def test_expire_training(self):
        """ 020H - tests expire_training method to ensure all trainings get deleted """
        self.JTF2_1.expire_training()
        self.assertEqual(self.JTF2_1.get_trainings(), [])

    def test_to_dict(self):
        """ 020I - tests to_dict method to ensure a dictionary is returned """
        self.assertEqual(self.JTF2_1.to_dict(), {'Deployment_Pay': 700,
                                                 'Division': 'JTF2',
                                                 'First_Name': 'Shabnam',
                                                 'Last_Name': 'Hashimi',
                                                 'Missions': 0,
                                                 'Rank': 'General',
                                                 'Role': 'Leader',
                                                 'Service_Number': '123456789',
                                                 'Training_Pay': 250,
                                                 'Trainings': []})

    def test_update_soldier_info(self):
        """ 020J - tests update_soldier_info method to ensure soldier info gets updated """
        self.JTF2_1.update_soldier_info(2, 'Sniper', 'Private', 'Billah', 'Alif', 400, 850)
        self.assertEqual(self.JTF2_1.get_missions(), 2)
        self.assertEqual(self.JTF2_1.get_rank(), 'Private')
        self.assertEqual(self.JTF2_1.get_role(), 'Sniper')
        self.assertEqual(self.JTF2_1.get_last_name(), 'Billah')
        self.assertEqual(self.JTF2_1.get_first_name(), 'Alif')
        self.assertEqual(self.JTF2_1.get_training_pay(), 400)
        self.assertEqual(self.JTF2_1.get_deployment_pay(), 850)


if __name__ == '__main__':
    unittest.main()
