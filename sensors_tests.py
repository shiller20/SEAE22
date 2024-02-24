import sensors_main
import unittest
import sys # needed for setting the command line parameters for test cases
from unittest.mock import patch # needed for the integration test case

# Unit tests implemented with Python's built-in unittest need to be classes,
# so here we use TestSensors class for the tests.
class TestSensors(unittest.TestCase):
    ###################
    # Unit test cases #
    ###################

    # Test case test_check_limits1 (UT1) that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # Test case test_check_limits2 (UT2) that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.
    def test_check_limits2(self):
        # TODO: implement the actual test case code
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)

    # TODO: Implement Test case test_check_limits3 (UT3) according to your
    # plan here. 
    def test_check_limits3(self):
        # TODO: test the check_limit function when inputs are the same
        limits = [18, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)

    def test_show_sensor_data(self):
        # TODO: Checks if there are corrupted values
        result = sensors_main.read_sensors()
        n = 0
        while n < len(result):
            for i in result[n]:
                if type(i) != float:
                    print(f"Invalid number occurred in Sensor{n+1}" )
            n+=1
        self.assertTrue(result,True)

    def test_sensor_timeline(self):
        # TODO: first run show_sensor_data to make sure no corrupted data.
        # This function checks if the data timeline is complete. (24 hours)
        result = sensors_main.read_sensors()
        n = 0
        while n < len(result):
            for i in result[n]:
                if len(result[n]) != 24:
                    print(f"Some data is missing in Sensor{n+1}. It contains {len(result[n])} values instead of 24" )
            n+=1
        self.assertTrue(result, True)
    

    ##########################
    # Integration test cases #
    ##########################

    # TODO: Complete test case test_check_limits_integration1 code so
    # that tests the check_limits function from main function.

    # NOTE: Redirect console output to sys.stdout in order to check it
    # from the test cases (here, from the integration test case). Also, use
    # mock_print as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        pass
        # 1. set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [{sensors_main.py}, {22}, {18}]
        # 2. call main with the command line parameters set up
        result = sensors_main.check_limits(sys.argv[1], sys.argv[2])
        # 3. check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")
        # 4. If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys (as this module has) because this
        # test case sets the command line arguments that are in sys.argv)
        #
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")

    @patch('builtins.print')
    def test_show_sensor_data_integration(self, mock_print):
        result = sensors_main.show_sensor_data()
        sys.argv = [{sensors_main.py}, {}]
        #check that the console output is the expected error message
        mock_print.assert_called_with("")
        sys.stdout.write(str(mock_print.call_args))

        if (sys.stdout.write(str(mock_print.call_args)) == str(result)):
            return True
        else:
            return False

if __name__ == '__main__':
    unittest.main()
