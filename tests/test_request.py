import os
from scripts.page_loader import download


def test_download_create(test_mock, test_dir):
    with test_dir as tmpd:
        ret_download = download('http://test.com', tmpd)
        assert ret_download == os.path.join(tmpd, 'test-com.html')
        
def test_download_data(test_mock, test_dir):
    with test_dir as tmpd:
        ret_download = download('http://test.com', tmpd)
        with open(ret_download, 'r') as f:
            assert f.read() == 'data'