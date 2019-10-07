import unittest
import conversions
import conversions_refactored

# test cases: 
# passes correct conversions, 
# fails bad conversions, 
# fails non-float convertible inputs, 
# fails values below absolute zero (k = 0, c = -273.15, f = -459.67), 
# makes sure self conversions are working

class CelsiusToKelvinTestCase(unittest.TestCase):
    """Test Celsius to Kelvin Conversion"""
    correct = {
        500 : 773.15,
        450 : 723.15,
        400 : 673.15,
        300 : 573.15,
        200 : 473.15,
        100 : 373.15,
        0 : 273.15,
        -100 : 173.15,
        -200 : 73.15,
        -273.15 : 0
    }

    def test_correct_conversion(self): 
        '''convertCelsiusToKelvin should pass with correct conversions'''
        for x,y in CelsiusToKelvinTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertCelsiusToKelvin(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
        -1 : 1455,
        -175 : 77,
        -270 : 100
    }

    def test_incorrect_conversion(self): 
        '''convertCelsiusToKelvin should not create incorrect conversions'''
        for x,y in CelsiusToKelvinTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertCelsiusToKelvin(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertCelsiusToKelvinFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertCelsiusToKelvin, x)

    def test_floor_input(self):
        '''convertCelsiusToKelvin should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertCelsiusToKelvin, -273.16)

    def test_ceiling_input(self):
        '''convertCelsiusToKelvin should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(9999999999999999999999999999999999999999999999999999999999999999999999), 1*10**70)

class CelsiusToFahrenheitTestCase(unittest.TestCase):
    """Test Celsius to Fahrenheit Conversion"""
    correct = {
        500 : 932,
        450 : 842,
        400 : 752,
        300 : 572,
        200 : 392,
        100 : 212,
        0 : 32,
        -100 : -148,
        -200 : -328,
        -273.15 : -459.67
    }

    def test_correct_conversion(self): 
        '''convertCelsiusToFahrenheit should pass with correct conversions'''
        for x,y in CelsiusToFahrenheitTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
        -1 : 1455,
        -175 : 77,
        -270 : 100
    }

    def test_incorrect_conversion(self): 
        '''convertCelsiusToFahrenheit should not create incorrect conversions'''
        for x,y in CelsiusToFahrenheitTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertCelsiusToFahrenheit(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertCelsiusToFahrenheitFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertCelsiusToFahrenheit, x)

    def test_floor_input(self):
        '''convertCelsiusToFahrenheit should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertCelsiusToFahrenheit, -273.16)

    def test_ceiling_input(self):
        '''convertCelsiusToFahrenheit should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(9999999999999999999999999999999999999999999999999999999999999999999999), 1.8*10**70)

class FahrenheitToKelvinTestCase(unittest.TestCase):
    """Test Fahrenheit to Kelvin Conversion"""
    correct = {
        932 : 773.15,
        842 : 723.15,
        752 : 673.15,
        572 : 573.15,
        392 : 473.15,
        212 : 373.15,
        32 : 273.15,
        -148 : 173.15,
        -328 : 73.15,
        -459.67 : 0
    }

    def test_correct_conversion(self): 
        '''convertFahrenheitToKelvin should pass with correct conversions'''
        for x,y in FahrenheitToKelvinTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
        -1 : 1455,
        -175 : 77,
        -270 : 100
    }

    def test_incorrect_conversion(self): 
        '''convertFahrenheitToKelvin should not create incorrect conversions'''
        for x,y in FahrenheitToKelvinTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertFahrenheitToKelvin(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertFahrenheitToKelvinFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertFahrenheitToKelvin, x)

    def test_floor_input(self):
        '''convertFahrenheitToKelvin should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertFahrenheitToKelvin, -459.68)

    def test_ceiling_input(self):
        '''convertFahrenheitToKelvin should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(9999999999999999999999999999999999999999999999999999999999999999999999), 5.55555555555555555555555555555555555541388*10**69)

class FahrenheitToCelsiusTestCase(unittest.TestCase):
    """Test Fahrenheit to Celsius Conversion"""
    correct = {
        932 : 500,
        842 : 450,
        752 : 400,
        572 : 300,
        392 : 200,
        212 : 100,
        32 : 0,
        -148 : -100,
        -328 : -200,
        -459.67 : -273.15
    }

    def test_correct_conversion(self): 
        '''convertFahrenheitToCelsius should pass with correct conversions'''
        for x,y in FahrenheitToCelsiusTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
        -1 : 1455,
        -175 : 77,
        -270 : 100
    }

    def test_incorrect_conversion(self): 
        '''convertFahrenheitToCelsius should not create incorrect conversions'''
        for x,y in FahrenheitToCelsiusTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertFahrenheitToCelsius(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertFahrenheitToCelsiusFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertFahrenheitToCelsius, x)

    def test_floor_input(self):
        '''convertFahrenheitToCelsius should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertFahrenheitToCelsius, -459.68)

    def test_ceiling_input(self):
        '''convertFahrenheitToCelsius should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(9999999999999999999999999999999999999999999999999999999999999999999999), 5.55555555555555555555555555555555555541388*10**69)

class KelvinToCelsiusTestCase(unittest.TestCase):
    """Test Kelvin to Celsius Conversion"""
    correct = {
        500 : 773.15,
        450 : 723.15,
        400 : 673.15,
        300 : 573.15,
        200 : 473.15,
        100 : 373.15,
        0 : 273.15,
        -100 : 173.15,
        -200 : 73.15,
        -273.15 : 0
    }

    correct = {v: k for k, v in correct.items()}

    def test_correct_conversion(self): 
        '''convertKelvinToCelsius should pass with correct conversions'''
        for x,y in KelvinToCelsiusTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertKelvinToCelsius(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
    }

    def test_incorrect_conversion(self): 
        '''convertKelvinToCelsius should not create incorrect conversions'''
        for x,y in KelvinToCelsiusTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertKelvinToCelsius(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertKelvinToCelsiusFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertKelvinToCelsius, x)

    def test_floor_input(self):
        '''convertKelvinToCelsius should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertKelvinToCelsius, -0.1)

    def test_ceiling_input(self):
        '''convertKelvinToCelsius should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(9999999999999999999999999999999999999999999999999999999999999999999999), 1*10**70)

class KelvinToFahrenheitTestCase(unittest.TestCase):
    """Test Kelvin to Fahrenheit Conversion"""
    correct = {
        932 : 773.15,
        842 : 723.15,
        752 : 673.15,
        572 : 573.15,
        392 : 473.15,
        212 : 373.15,
        32 : 273.15,
        -148 : 173.15,
        -328 : 73.15,
        -459.67 : 0
    }

    correct = {v: k for k, v in correct.items()}

    def test_correct_conversion(self): 
        '''convertKelvinToFahrenheit should pass with correct conversions'''
        for x,y in KelvinToFahrenheitTestCase.correct.items():
            self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(x),y)

    incorrect = {
        499 : 709,
        433 : 722,
        412 : 633,
        377 : 553,
        234 : 4734,
        199 : 3756,
        1 : 2645,
    }

    def test_incorrect_conversion(self): 
        '''convertKelvinToFahrenheit should not create incorrect conversions'''
        for x,y in KelvinToFahrenheitTestCase.incorrect.items():
            self.assertNotEqual(conversions.convertKelvinToFahrenheit(x),y)
    
    bad_input = [
        'test',
        [1,2,3],
        {1:2,3:4},
        '',
        'zero'
    ]

    def test_type_input(self):
        '''convertKelvinToFahrenheitFails should fail non-float convertible inputs'''
        for x in self.bad_input:
            self.assertRaises(conversions.NotANumberError, conversions.convertKelvinToFahrenheit, x)

    def test_floor_input(self):
        '''convertKelvinToFahrenheit should fail values below absolute zero'''
        self.assertRaises(conversions.AbsoluteZeroError, conversions.convertKelvinToFahrenheit, -459.68)

    def test_ceiling_input(self):
        '''convertKelvinToFahrenheit should pass extremely large numbers'''
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(9999999999999999999999999999999999999999999999999999999999999999999999), 1.8*10**70)

class convertTestCase(unittest.TestCase):
    '''Tests the all in one conversion method'''

    correct_kelvin_fahrenheit = {
        773.15 : 932,
        723.15 : 842,
        673.15 : 752,
        573.15 : 572,
        473.15 : 392,
        373.15 : 212,
        273.15 : 32,
        173.15 : -148,
        73.15 : -328,
        0 : -459.67
    }

    correct_kelvin_celsius = {
        773.15: 500,
        723.15: 450,
        673.15: 400,
        573.15: 300,
        473.15: 200,
        373.15: 100,
        273.15: 0,
        173.15: -100,
        73.15: -200,
        0: -273.15
    }

    correct_fahrenheit_celsius = {
        932 : 500,
        842 : 450,
        752 : 400,
        572 : 300,
        392 : 200,
        212 : 100,
        32 : 0,
        -148 : -100,
        -328 : -200,
        -459.67 : -273.15
    }

    correct_fahrenheit_kelvin = {
        932 : 773.15,
        842 : 723.15,
        752 : 673.15,
        572 : 573.15,
        392 : 473.15,
        212 : 373.15,
        32 : 273.15,
        -148 : 173.15,
        -328 : 73.15,
        -459.67 : 0
    }
    
    correct_celsius_fahrenheit = {
        500 : 932,
        450 : 842,
        400 : 752,
        300 : 572,
        200 : 392,
        100 : 212,
        0 : 32,
        -100 : -148,
        -200 : -328,
        -273.15 : -459.67
    }

    correct_celsius_kelvin = {
        500 : 773.15,
        450 : 723.15,
        400 : 673.15,
        300 : 573.15,
        200 : 473.15,
        100 : 373.15,
        0 : 273.15,
        -100 : 173.15,
        -200 : 73.15,
        -273.15 : 0
    }    

    def test_correct_k_f_conversion(self):
        '''convert should pass with correct conversions for kelvin to fahrenheit'''
        for x,y in self.correct_kelvin_fahrenheit.items():
            self.assertAlmostEqual(conversions_refactored.convert('kelvin','fahrenheit',x),y)

    def test_correct_k_c_conversion(self):
        '''convert should pass with correct conversions for kelvin to celsius'''
        for x,y in self.correct_kelvin_celsius.items():
            self.assertAlmostEqual(conversions_refactored.convert('kelvin','celsius',x),y)

    def test_correct_f_c_conversion(self):
        '''convert should pass with correct conversions for fahrenheit to celsius'''
        for x,y in self.correct_fahrenheit_celsius.items():
            self.assertAlmostEqual(conversions_refactored.convert('fahrenheit','celsius',x),y)

    def test_correct_f_k_conversion(self):
        '''convert should pass with correct conversions for fahrenheit to kelvin'''
        for x,y in self.correct_fahrenheit_kelvin.items():
            self.assertAlmostEqual(conversions_refactored.convert('fahrenheit','kelvin',x),y)

    def test_correct_c_f_conversion(self):
        '''convert should pass with correct conversions for celsius to fahrenheit'''
        for x,y in self.correct_celsius_fahrenheit.items():
            self.assertAlmostEqual(conversions_refactored.convert('celsius','fahrenheit',x),y)

    def test_correct_c_k_conversion(self):
        '''convert should pass with correct conversions for celsius to kelvin'''
        for x,y in self.correct_celsius_kelvin.items():
            self.assertAlmostEqual(conversions_refactored.convert('celsius','kelvin',x),y)

    correct_miles_yards = {
        0:0,
        1:1760,
        2:3520,
        3:5280,
        10:17600
    }

    correct_miles_meters = {
        0:0,
        1:1609.44,
        2:3218.69,
        3:4828.03,
        10:16093.4
    }

    correct_yards_miles = {
        0:0,
        1760:1,
        3520:2,
        5280:3,
        17600:10
    }

    correct_yards_meters = {
        0:0,
        1:0.9141,
        2:1.8288,
        3:2.7432,
        10:9.144
    }

    correct_meters_miles = {
        0:0,
        1609.34:1,
        3218.69:2,
        4828.03:3,
        16093.44:10
    }

    correct_meters_yards = {
        0:0,
        0.941:1,
        1.83:2,
        2.74:3,
        9.144:10
    }

    def test_correct_mi_y_conversion(self):
        ''''convert should pass with correct conversions for miles to yards'''
        for x,y in self.correct_miles_yards.items():
            self.assertEqual(round(conversions_refactored.convert('miles','yards',x)),round(y))

    def test_correct_mi_m_conversion(self):
        ''''convert should pass with correct conversions for miles to meters'''
        for x,y in self.correct_miles_meters.items():
            self.assertEqual(round(conversions_refactored.convert('miles','meters',x)),round(y))

    def test_correct_y_mi_conversion(self):
        ''''convert should pass with correct conversions for yards to miles'''
        for x,y in self.correct_yards_miles.items():
            self.assertEqual(round(conversions_refactored.convert('yards','miles',x)),round(y))

    def test_correct_y_m_conversion(self):
        ''''convert should pass with correct conversions for yards to meters'''
        for x,y in self.correct_yards_meters.items():
            self.assertEqual(round(conversions_refactored.convert('yards','meters',x)),round(y))

    def test_correct_m_mi_conversion(self):
        ''''convert should pass with correct conversions for meters to miles'''
        for x,y in self.correct_meters_miles.items():
            self.assertEqual(round(conversions_refactored.convert('meters','miles',x)),round(y))

    def test_correct_m_y_conversion(self):
        ''''convert should pass with correct conversions for meters to yards'''
        for x,y in self.correct_meters_yards.items():
            self.assertEqual(round(conversions_refactored.convert('meters','yards',x)),round(y))

    units = [
        'kelvin',
        'fahrenheit',
        'celsius',
        'miles',
        'meters',
        'yards'
    ]

    def test_self_conversion(self):
        '''convert should pass with correct self-conversions with all compatible units'''
        for x in self.units:
            conversions_refactored.convert(x,x,1)

    incompatible_units = [ 
        ['meters', 'celsius'],
        ['celsius', 'meters'],
        ['celsius', 'yards'],
        ['celsius', 'miles'],
        ['fahrenheit', 'meters'],
        ['fahrenheit', 'yards'],
        ['fahrenheit', 'miles'],
        ['kelvin', 'meters'],
        ['kelvin', 'yards'],
        ['kelvin', 'miles'],
    ]

    def test_incompatible_units(self):
        '''conver should fail with incompatible units and raise an exception'''
        for x,y in self.incompatible_units:
            self.assertRaises(conversions_refactored.ConversionNotPossibleError, conversions_refactored.convert, x,y,1)
    

if __name__ == '__main__':
    unittest.main()