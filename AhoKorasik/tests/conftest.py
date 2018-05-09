def pytest_addoption(parser):
    parser.addoption("--patterns", action="append", default=[],
                     help="a strings we find")
    parser.addoption("--text", action="append", default=[],
                     help="a text where we find")
    parser.addoption("--answer", action="append", default=[],
                     help="answer we want to get")
    parser.addoption("--count", action="append", default=[],
                     help="answer we want to get")


def pytest_generate_tests(metafunc):
    if 'patterns' in metafunc.fixturenames:
        metafunc.parametrize("patterns",
                             metafunc.config.getoption('patterns'))
    if 'text' in metafunc.fixturenames:
        metafunc.parametrize("text",
                             metafunc.config.getoption('text'))
    if 'count' in metafunc.fixturenames:
        metafunc.parametrize("count",
                             metafunc.config.getoption('count'))
    if 'answer' in metafunc.fixturenames:
        metafunc.parametrize("answer",
                             metafunc.config.getoption('answer'))
