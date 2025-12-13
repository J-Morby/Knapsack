import unittest
from TimeSelectorQWidget import TimeSlider

class TestConvertTo(unittest.TestCase):

    def test_convert_to_hhmm(self):
        assert TimeSlider.convert_to_hhmm(0)    == "00:00"
        assert TimeSlider.convert_to_hhmm(15)   == "00:15"
        assert TimeSlider.convert_to_hhmm(30)   == "00:30"
        assert TimeSlider.convert_to_hhmm(75)   == "01:15"
        assert TimeSlider.convert_to_hhmm(1020) == "17:00"
        assert TimeSlider.convert_to_hhmm(1440) == "24:00"

    def test_convert_to_minutes_midnight(self):
        assert TimeSlider.convert_to_minutes("00:00") == 0
        assert TimeSlider.convert_to_minutes("00:15") == 15
        assert TimeSlider.convert_to_minutes("00:30") == 30
        assert TimeSlider.convert_to_minutes("01:15") == 75
        assert TimeSlider.convert_to_minutes("17:00") == 1020
        assert TimeSlider.convert_to_minutes("24:00") == 1440
        

if __name__ == "__main__":
    unittest.main()