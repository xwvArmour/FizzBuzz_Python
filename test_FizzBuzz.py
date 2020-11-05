import pytest
from FizzBuzz import fizzbuzz

@pytest.mark.parametrize(
    "num", [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19]
)
def test_Num(num):
    # Arrange
    # from parametrize

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

@pytest.mark.parametrize(
    "num", range(3, 15, 3)
)
def test_Fizz(num):
    # Arrange
    # from parametrize

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Fizz'

@pytest.mark.parametrize(
    "num", [5, 10, 20, 25, 35]
)
def test_Buzz(num):
    # Arrange
    # from parametrize

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Buzz'

@pytest.mark.parametrize(
    "num", range(15, 100, 15)
)
def test_FizzBuzz(num):
    # Arrange
    # from parametrize

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'FizzBuzz'

def test_HugeNum():
    # Arrange
    num = 3*5**1000+1

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

def test_HugeFizz():
    # Arrange
    num = 3*5**1000 + 3

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Fizz'

def test_HugeBuzz():
    # Arrange
    num = 3*5**1000 + 5

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Buzz'

def test_HugeFizzBuzz():
    # Arrange
    num = 3*5**1000 + 15

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'FizzBuzz'
