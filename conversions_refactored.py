from conversions import AbsoluteZeroError, NotANumberError

class ConversionNotPossibleError(Exception):
    pass
class NotAStringError(TypeError):
    pass
class NotAValidUnitError(Exception):
    pass

temperature = {
    'celsius' : {
        'kelvin' : {
            'inner_add' : 0,
            'inner_multiplier' : 1,
            'outer_add' : 273.15,
            'outer_multiplier' : 1
        },
        'fahrenheit' : {
            'inner_add' : 0,
            'inner_multiplier' : 9/5,
            'outer_add' : 32,
            'outer_multiplier' : 1
        }
    },
    'kelvin' : {
        'celsius' : {
            'inner_add' : 0,
            'inner_multiplier' : 1,
            'outer_add' : -273.15,
            'outer_multiplier' : 1
        },
        'fahrenheit' : {
            'inner_add' : 0,
            'inner_multiplier' : 9/5,
            'outer_add' : -459.67,
            'outer_multiplier' : 1
        } 
    },        
    'fahrenheit' : {
        'kelvin' : {
            'inner_add' : 459.67,
            'inner_multiplier' : 1,
            'outer_add' : 0,
            'outer_multiplier' : 5/9
        },
        'celsius' : {
            'inner_add' : -32,
            'inner_multiplier' : 1,
            'outer_add' : 0,
            'outer_multiplier' : 5/9
        }
    }
}

distance = {
    'miles': {
        'yards' : 1760,
        'meters' : 1609.344
    },
    'yards' : {
        'miles' : 1/1760,
        'meters' : 1/1.094
    },
    'meters' : {
        'miles': 1/1609.344,
        'yards': 1.094
    }
}

def convert(fromUnit,toUnit,value):
    try:
        value = float(value)
    except:
        raise NotANumberError
    try:
        fromUnit = fromUnit.lower()
        toUnit = toUnit.lower()
    except:
        raise NotAStringError
    if fromUnit == toUnit:
        return value
    if fromUnit in temperature and toUnit in temperature:
        conversion = (value * temperature[fromUnit][toUnit]['inner_multiplier'] + temperature[fromUnit][toUnit]['inner_add']) * temperature[fromUnit][toUnit]['outer_multiplier'] + temperature[fromUnit][toUnit]['outer_add']
    elif fromUnit in distance and toUnit in distance:
        conversion = value * distance[fromUnit][toUnit]  
    else:
        raise ConversionNotPossibleError
    
    return conversion