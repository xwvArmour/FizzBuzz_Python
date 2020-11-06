import time

def apiCall():
    timer.sleep(5)
    return 1

def getData():
    data = apiCall()
    # do other things
    return data

def test_getData(mocker):
    mocker.patch(
        'test_mocking.apiCall',
        return_value = 2
    )
    expected = 2
    actual = getData()

    assert expected == actual