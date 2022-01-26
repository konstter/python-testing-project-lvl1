from scripts.page_loader import get_filename


def test_get_filename():
    '''
    Test filename create
    '''
    fn = get_filename('https://yandex.ru/')
    assert fn == 'yandex-ru-.html'
