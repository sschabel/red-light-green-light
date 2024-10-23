import unittest
from unittest.mock import Mock, PropertyMock

import red_light_green_light
from red_light_green_light import RedLightGreenLight

class RedLightGreenLightTest(unittest.TestCase):

  redLight = Mock()
  yellowLight = Mock()
  greenLight = Mock()
  lcd = Mock()
  led_mock = PropertyMock()
  led_on_mock = Mock()

  cut = None # RedLightGreenLight is our CUT (Class Under Test)

  def setUp(self):
    self.cut = RedLightGreenLight(self.redLight, self.yellowLight, self.greenLight, self.lcd)

  def test_givenLightsAndLcd_whenInitRedLightGreenLight_thenPlayingIsFalse(self):
    # given
    # default args
    # when
    # RedLightGreenLight is instantiated
    # then
    self.assertFalse(self.cut.playing)

  @unittest.mock.patch('random.randint')
  def test_givenRandIntIs1_whenDetermineNextLight_thenReturnGreenLight(self, randint_mock):
    # given
    randint_mock.return_value = 1
    # when
    result = self.cut.determine_next_light()
    # then
    self.assertEqual(result, self.greenLight)

  @unittest.mock.patch('random.randint')
  def test_givenRandIntIs1_whenDetermineNextLight_thenReturnYellowLight(self, randint_mock):
    # given
    randint_mock.return_value = 2
    # when
    result = self.cut.determine_next_light()
    # then
    self.assertEqual(result, self.yellowLight)

  @unittest.mock.patch('random.randint')
  def test_givenRandIntIs1_whenDetermineNextLight_thenReturnRedLight(self, randint_mock):
    # given
    randint_mock.return_value = 3
    # when
    result = self.cut.determine_next_light()
    # then
    self.assertEqual(result, self.redLight)