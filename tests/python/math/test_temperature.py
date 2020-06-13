from python.math.weather import Temperature
import pytest
import unittest
assertions = unittest.TestCase('__init__')

SIGNIFICANT_PLACES = 4

knownValues = ( (-273.15, -459.67),	# absolute zero
                (-89, -128.2),	# coldest recorded WX temp on earth's surface
                (-17.777777777, 0),	# temp of Daniel Gabriel Fahrenheit's ice/salt mixture
                (0, 32),		# H20 freezes
                (15, 59),		# average earth WX temp
                (36.8, 98.24),	# average body temperature
                (58, 136.4),	# warmest recorded WX temp on earth's surface
                (100, 212),		# H20 boils
                (5535, 9995) )	# average WX temp on the sun's surface


def test_to_fahrenheit_known_values():
    """converting to Fahrenheit should give known result with known input"""
    for tempC, tempF in knownValues:
        result = Temperature(celsius=tempC).fahrenheit()
        assertions.assertAlmostEqual(tempF, result, SIGNIFICANT_PLACES)


def test_to_celsius_known_values():
    """converting from Fahrenheit should give known back our known inputs"""
    for tempC, tempF in knownValues:
        result = Temperature(fahrenheit=tempF).celsius()
        assertions.assertAlmostEqual(tempC, result, SIGNIFICANT_PLACES)


def test_sanity_one():
    """Celsius(Fahrenheit(n))==n for all n"""
    for tempC in range(-273, 6000):
        tempF = Temperature(celsius=tempC).fahrenheit()
        result = Temperature(fahrenheit=tempF).celsius()
        assertions.assertAlmostEqual(tempC, result, SIGNIFICANT_PLACES)


def test_sanity_two():
        """Fahrenheit(Celsius(n))==n for all n"""
        for tempF in range(-459, 10000):
            tempC = Temperature(fahrenheit=tempF).celsius()
            result = Temperature(celsius=tempC).fahrenheit()
            assertions.assertAlmostEqual(tempF, result, SIGNIFICANT_PLACES)


def test_too_small_cel():
    """to Fahrenheit should fail with excessively negative Celsius input
    (below absolute zero)"""
    assertions.assertRaises(Temperature.OutOfRangeError, Temperature, celsius=-273.151)


def test_too_small_fah():
    """to Celsius should fail with excessively negative Fahrenheit input
    (below absolute zero)"""
    assertions.assertRaises(Temperature.OutOfRangeError, Temperature, fahrenheit=-459.671)
