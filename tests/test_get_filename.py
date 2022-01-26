from scripts.page_loader import get_filename


def test_get_filename():
    fn = get_filename('https://yandex.ru/')
    assert fn == 'yandex-ru-.html'
