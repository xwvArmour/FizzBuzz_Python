import time

class Dataset(object):
    def getItems(self):
        time.sleep(5)
        return ['A', 'B', 'C'] 

def doSomething():
    dataset = Dataset()
    return dataset.getItems()

def test_doSomething(mocker):
    expected = ['X', 'Y', 'Z']

    def mock_getItems(self):
        return expected

    mocker.patch(
        'test_mockingClass.Dataset.getItems',
        mock_getItems
    )

    actual = doSomething()

    assert expected == actual