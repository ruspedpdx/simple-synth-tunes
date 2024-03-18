import unittest
from unittest.mock import patch
from synth import get_type
from synth import select_type
from synth import get_ampl
from synth import select_ampl
from synth import get_key
from synth import select_key

class TestGetType(unittest.TestCase):

    @patch('synth.random.choice')
    def test_get_type(self, mock_choice):
        # Define the possible choices for wave types
        possible_types = ["Sine", "Square", "Sawtooth", "Noise"]

        # Set up the mock to return a predefined value
        mock_choice.return_value = "Sine"

        # Call the function
        result = get_type()

        # Check if the result is one of the possible types
        self.assertIn(result, possible_types)

class TestSelectType(unittest.TestCase):

    # Call select type with valid input
    @patch('builtins.input', side_effect=["0"])
    def test_select_type_sine(self, mock_input):
        expected_output = "Sine"
        self.assertEqual(select_type(), expected_output)

    @patch('builtins.input', side_effect=["1"])
    def test_select_type_square(self, mock_input):
        expected_output = "Square"
        self.assertEqual(select_type(), expected_output)

    @patch('builtins.input', side_effect=["2"])
    def test_select_type_sawtooth(self, mock_input):
        expected_output = "Sawtooth"
        self.assertEqual(select_type(), expected_output)

    @patch('builtins.input', side_effect=["3"])
    def test_select_type_noise(self, mock_input):
        expected_output = "Noise"
        self.assertEqual(select_type(), expected_output)

    # Call select type with an invalid input first
    @patch('builtins.input', side_effect=["a", "1"])
    def test_select_type_invalid_then_valid(self, mock_input):
        expected_output = "Square"
        self.assertEqual(select_type(), expected_output)

class TestGetAmpl(unittest.TestCase):
    
    # Call get amplitude with a valid return 
    @patch('synth.random.choice', return_value=4096)
    def test_get_ampl(self, mock_choice):
        expected_ampl = 4096
        actual_ampl = get_ampl()
        self.assertEqual(actual_ampl, expected_ampl)

class TestSelectAmpl(unittest.TestCase):
    
    # Call select amplitude with a valid input
    @patch('builtins.input', side_effect=['1'])
    def test_select_ampl_normal(self, mock_input):
        expected_output = 8192
        actual_output = select_ampl()
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['0'])
    def test_select_ampl_half(self, mock_input):
        expected_output = 4096
        actual_output = select_ampl()
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['2'])
    def test_select_ampl_double(self, mock_input):
        expected_output = 16384
        actual_output = select_ampl()
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['invalid', '2'])
    def test_select_ampl_invalid_then_valid(self, mock_input):
        expected_output = 16384
        actual_output = select_ampl()
        self.assertEqual(actual_output, expected_output)

    # Call select amplitude with an invalid input first
    @patch('builtins.input', side_effect=['4', '2'])
    def test_select_ampl_out_of_range_then_valid(self, mock_input):
        expected_output = 16384
        actual_output = select_ampl()
        self.assertEqual(actual_output, expected_output)

class TestGetKey(unittest.TestCase):

    # Call get key to verify that key returned is one of the valid choices
    def test_get_key(self):
        keys = ["C", "G", "D", "A", "E", "B", "F", "F#", "Db", "Ab", "Eb", "Bb"]
        key = get_key()
        self.assertIn(key, keys, f"Key returned '{key}' is not in the list of keys")

class TestSelectKey(unittest.TestCase):

    # Call select key with a valid input
    @patch('builtins.input', side_effect=['0'])
    def test_select_key_valid_input(self, mock_input):
        expected_output = "C"
        self.assertEqual(select_key(), expected_output)

    @patch('builtins.input', side_effect=['13', '5'])
    def test_select_key_invalid_input_then_valid(self, mock_input):
        expected_output = "B"
        self.assertEqual(select_key(), expected_output)

    # Call select key with an invalid input first
    @patch('builtins.input', side_effect=['invalid', '4'])
    def test_select_key_invalid_then_valid_input(self, mock_input):
        expected_output = "E"
        self.assertEqual(select_key(), expected_output)


if __name__ == '__main__':
    unittest.main()
