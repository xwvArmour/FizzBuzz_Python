from FizzBuzz import fizzbuzz

def test_Num():
    # Arrange
    num = 1

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

def test_Fizz():
    # Arrange
    num = 3

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Fizz'

def test_Buzz():
    # Arrange
    num = 5

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Buzz'

def test_FizzBuzz():
    # Arrange
    num = 15

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'FizzBuzz'

def test_NumBetween35():
    # Arrange
    num = 4

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

def test_NumBetween59():
    # Arrange
    num = 7

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

def test_HugeNum():
    # Arrange
    num = 3*5**1000+1

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == str(num)

def test_HugFizz():
    # Arrange
    num = 3*5**1000 + 3

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Fizz'

def test_HugBuzz():
    # Arrange
    num = 3*5**1000 + 5

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'Buzz'

def test_HugFizzBuzz():
    # Arrange
    num = 3*5**1000 + 15

    # Act
    ans = fizzbuzz(num)

    # Assert
    assert ans == 'FizzBuzz'
