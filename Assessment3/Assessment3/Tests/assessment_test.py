import pytest
from Code import python3

def test_one():
    assert python3.one("1,2,3,4,5") == "1,3,5"
    assert python3.one("2,4,6,8") == "null"
    assert python3.one("23,48,52,57") == "23,57"
    assert python3.one("66,67,68,70") == "67"
    assert python3.one("1,3,5,7,9") == "1,3,5,7,9"

def test_two():
    assert python3.two(["Dog"]) == ["Dog"]
    assert python3.two(["Dog","Cat"]) == ["Dog","Cat"]
    assert python3.two(["Dog","Dog","Cat"]) == ["Dog","Cat"]
    assert python3.two(["Dog","DoG","Cat"]) == ["Dog","DoG","Cat"]
    assert python3.two(["Cat","DOG","DOG"]) == ["Cat","DOG"]

def test_three():
    assert python3.three("Hello") == "el"
    assert python3.three("hi") == "i"
    assert python3.three("0H1e2l3l4o5w6o7r8l9d") == "Helloworld"
    assert python3.three("H1e2l3l4o5w6o7r8l9d") == "123456789"
    assert python3.three("ILovePython") == "LvPto"

def test_four():
    assert python3.four("Am I in Amsterdam") == 1
    assert python3.four("I am in Amsterdam am I?") == 2
    assert python3.four("I have been in Amsterdam") == 0
    assert python3.four("I love when I am in Amsterdam") == 1
    assert python3.four("Am I am in Amsterdam in the AM") == 3

def test_five():
    assert python3.five("0123-4567-8901-2345") == False
    assert python3.five("401234567890123") == False
    assert python3.five("4012 3456 7890 1234") == False
    assert python3.five("4444-0123-4567-8901") == False
    assert python3.five("4012-3456-7890-1234") == True
    assert python3.five("4012345678901234") == True

def test_six():
    assert python3.six("john@google.com", "person") == "john"
    assert python3.six("jane@Microsoft.com", "company") == "microsoft"
    assert python3.six("Dave@amazon.com", "person") == "dave"
    assert python3.six("FRied@mcdonalds.com", "person") == "fried"
    assert python3.six("doug@landscapegardening.com", "company") == "landscapegardening"

def test_seven():
    assert python3.seven("hoopplla") == 2
    assert python3.seven("abbCCCddDDDeeEEE") == 3
    assert python3.seven("") == 0
    assert python3.seven("python") == 1
    assert python3.seven("doom") == 2

def test_eight():
    assert python3.eight(3) == 2
    assert python3.eight(8) == 21
    assert python3.eight(0) == 0
    assert python3.eight(1) == 1
    assert python3.eight(2) == 1

def test_nine():
    assert python3.nine(35,94) == '(23,12)'
    assert python3.nine(2,6) == '(1,1)'
    assert python3.nine(12,63) == "no solutions"
    assert python3.nine(15,30) == '(15,0)'
    assert python3.nine(10,40) == '(0,10)'

def test_ten():
    assert python3.ten("bag,car,dog") == "bag,car,dog"
    assert python3.ten("dog,car,bag") == "bag,car,dog"
    assert python3.ten("car,bark,bag,dog") == "bag,bark,car,dog"
    assert python3.ten("fire,coat,sea") == "coat,fire,sea"
    assert python3.ten("cauliflower,cyber,bulb,bulk") == "bulb,bulk,cauliflower,cyber"
