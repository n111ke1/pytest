import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome', help="browser type")

@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")


