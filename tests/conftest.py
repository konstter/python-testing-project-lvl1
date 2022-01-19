import pytest
import requests
import tempfile


@pytest.fixture
def test_mock(requests_mock):
    return requests_mock.get('http://test.com', text='data')


@pytest.fixture
def test_dir():
    return tempfile.TemporaryDirectory()