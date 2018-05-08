def pytest_addoption(parser):
    parser.addoption("--pattern", action="append", default=[],
                     help="a string we find")
    parser.addoption("--text", action="append", default=[],
                     help="a text where we find")
    parser.addoption("--answer", action="append", default=[],
                     help="answer we want to get")


def pytest_generate_tests(metafunc):
    if 'pattern' in metafunc.fixturenames:
        metafunc.parametrize("pattern",
                             metafunc.config.getoption('pattern'))
    if 'text' in metafunc.fixturenames:
        metafunc.parametrize("text",
                             metafunc.config.getoption('text'))
    if 'answer' in metafunc.fixturenames:
        metafunc.parametrize("answer",
                             metafunc.config.getoption('answer'))
