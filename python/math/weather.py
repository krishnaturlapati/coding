"""
Develop a Python module called weather.py that contains a temperature class and associated
methods.

Your module should contain the necessary Exceptions
required to signal when the user requests a temperature
that is below absolute zero.

Furthermore, your temperature class should have methods
that convert the class’s temperature value (attribute) to Celsius
and to Fahrenheit.

Reference https://courses.ece.msstate.edu/ece4723/fall17/lab/t1/t1.pdf

"""


class Temperature:
    class OutOfRangeError(ValueError):
        pass

    def __init__(self, celsius=0, fahrenheit=0):
        self._celsius = celsius
        self._fahrenheit = fahrenheit
        if self._celsius < -273.15:
            raise self.OutOfRangeError('celsius cannot got below absolute zero ')

        if self._fahrenheit < -459.67:
            raise self.OutOfRangeError('fahrenheit cannot got below absolute zero ')

    def fahrenheit(self):
        return 9.0/5.0 * self._celsius + 32

    def celsius(self):
        return (self._fahrenheit - 32) * 5.0/9.0



