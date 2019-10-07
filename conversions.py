class AbsoluteZeroError(ValueError):
    pass
class NotANumberError(TypeError):
    pass

def convertCelsiusToKelvin(degC):
    try:
        degC = float(degC)
    except:
        raise NotANumberError
    if degC < -273.15:
        raise AbsoluteZeroError
    degK = degC + 273.15
    return degK

def convertCelsiusToFahrenheit(degC):
    try:
        degC = float(degC)
    except:
        raise NotANumberError
    if degC < -273.15:
        raise AbsoluteZeroError
    degF = degC * (9/5) + 32
    return degF

def convertFahrenheitToKelvin(degF):
    try:
        degF = float(degF)
    except:
        raise NotANumberError        
    if degF < -459.67:
        raise AbsoluteZeroError
    degK = (degF + 459.67) * (5/9)
    return degK

def convertFahrenheitToCelsius(degF):
    try:
        degF = float(degF)
    except:
        raise NotANumberError
    if degF < -459.67:
        raise AbsoluteZeroError
    degC = (degF - 32) * (5/9)
    return degC

def convertKelvinToCelsius(degK):
    try:
        degK = float(degK)
    except:
        raise NotANumberError
    if degK < 0:
        raise AbsoluteZeroError
    degC = degK - 273.15
    return degC

def convertKelvinToFahrenheit(degK):
    try:
        degK = float(degK)
    except:
        raise NotANumberError
    if degK < 0:
        raise AbsoluteZeroError
    degF = degK * (9/5) - 459.67
    return degF