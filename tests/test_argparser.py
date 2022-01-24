from scripts.page_loader import create_parser


def test_parser1():
    parser = create_parser()
    parsed = parser.parse_args(['--output', 'test', '--webpage', 'page'])
    assert parsed.output == 'test'
    assert parsed.webpage == 'page'


def test_parser2():
    parser = create_parser()
    parsed = parser.parse_args(['-w', 'test', '-o', 'new'])
    assert parsed.output == 'new'
    assert parsed.webpage == 'test'


