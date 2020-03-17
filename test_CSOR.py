import unittest
from CSOR import CSOR


class TestCSOR(unittest.TestCase):

    def setUp(self):
        """ set up fixture """
        self.CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)

    def test_constructor(self):
        """ 010A - tests valid cases for constructor """
        self.assertIsNotNone(self.CSOR1)
        self.assertIsInstance(self.CSOR1, CSOR)

    def test_constructor_invalid(self):
        """ 010B - tests invalid cases for constructor """
        with self.assertRaises(TypeError):
            CSOR1 = CSOR(4, 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(ValueError):
            CSOR1 = CSOR('ABCD', 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3.5, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(ValueError):
            CSOR1 = CSOR('ABC', -3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(ValueError):
            CSOR1 = CSOR('ABC', 3, '12345678910', 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, 123456789, 'General', 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, '123456789', 3, 'Hashimi', 'Shabnam', 500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 5, 'Shabnam', 500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 5.2, 500, 900)
        with self.assertRaises(ValueError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', -500, 900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', '500', 900)
        with self.assertRaises(ValueError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, -900)
        with self.assertRaises(TypeError):
            CSOR1 = CSOR('ABC', 3, '123456789', 'General', 'Hashimi', 'Shabnam', 500, '900')

    def test_get_kill_count(self):
        """ 010C - tests if get_kill_count method works """
        self.assertEqual(self.CSOR1.get_kill_count, 3)

    def test_training_pay(self):
        """ 010D - tests setter and getter for training pay """
        self.CSOR1.set_training_pay(650)
        self.assertEqual(self.CSOR1.get_training_pay(), 650)

    def test_deployment_pay(self):
        """ 010E - tests setter and getter for deployment pay """
        self.CSOR1.set_deployment_pay(1000)
        self.assertEqual(self.CSOR1.get_deployment_pay(), 1000)

    def test_train(self):
        """ 010F - tests train method to ensure training gets added to list """
        self.CSOR1.train('DP1')
        self.assertEqual(self.CSOR1.get_trainings(), ['DP1'])

    def test_train_invalid(self):
        """ 010G - tests invalid parameter for train method """
        with self.assertRaises(ValueError):
            self.CSOR1.train(1)

    def test_expire_training(self):
        """ 010H - tests expire_training method to ensure training gets deleted """
        self.CSOR1.train('DP1')
        self.CSOR1.expire_training('DP1')
        self.assertEqual(self.CSOR1.get_trainings(), [])

    def test_to_dict(self):
        """ 010I - tests to_dict method to ensure a dictionary is returned """
        self.assertEqual(self.CSOR1.to_dict(), {'Call_Sign': 'ABC',
                                                'Deployment_Pay': 900,
                                                'Division': 'CSOR',
                                                'First_Name': 'Shabnam',
                                                'Kill_Count': 3,
                                                'Last_Name': 'Hashimi',
                                                'Rank': 'General',
                                                'Service_Number': '123456789',
                                                'Training_Pay': 500,
                                                'Trainings': []})

    def test_update_soldier_info(self):
        """ 010J - tests update_soldier_info method to ensure soldier info gets updated """
        self.CSOR1.update_soldier_info('DEF', 6, 'Soldier', 'Billah', 'Alif', 300, 750)
        self.assertEqual(self.CSOR1.get_kill_count, 6)
        self.assertEqual(self.CSOR1.get_last_name(), 'Billah')
        self.assertEqual(self.CSOR1.get_rank(), 'Soldier')
        self.assertEqual(self.CSOR1.get_training_pay(), 300)
        self.assertEqual(self.CSOR1.get_deployment_pay(), 750)
        self.assertEqual(self.CSOR1.get_call_sign(), 'DEF')
        self.assertEqual(self.CSOR1.get_first_name(), 'Alif')

    def test_get_call_sign(self):
        """ 010K - tests getter get_call_sign method """
        self.assertEqual(self.CSOR1.get_call_sign(), 'ABC')


if __name__ == '__main__':
    unittest.main()
