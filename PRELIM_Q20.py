# Prelim Exam Question 20 - Labado, Christian Vridge

def test_Conversion():
    tempInFahrenheit = 32 # With this input, output should be 0
    tempInCelcius = (tempInFahrenheit - 32) * (5/9) # Given Formula
    assert tempInCelcius == 0 # Successful test
    assert tempInCelcius == 32 # Failed test