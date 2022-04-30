import unittest
import employee_management_system.helper_functions as hf


class TestHelperFunctions(unittest.TestCase):
    def test_calc_salary(self):
        self.assertEqual(hf.calc_salary(10, 100, 0), 1600)
        self.assertEqual(hf.calc_salary(10, 100, 10), 1760)
        self.assertEqual(hf.calc_salary(-10, 100, 10), None)
        self.assertEqual(hf.calc_salary(10, 101, 10), None)
        self.assertEqual(hf.calc_salary(10, -1, 10), None)
        self.assertEqual(hf.calc_salary(10, 100, -10), None)
        self.assertEqual(hf.calc_salary(-10, -100, -10), None)
        self.assertEqual(hf.calc_salary(-10, 101, -10), None)


if __name__ == '__main__':
    unittest.main()

