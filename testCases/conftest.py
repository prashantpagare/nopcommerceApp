from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Chrome Browser Launching..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox Browser Launching..........")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



############### Pytest HTML Report ###############

# it is hooks for adding Enviorement info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Prashant'


# It is hooks for delete/modify Enviroment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)